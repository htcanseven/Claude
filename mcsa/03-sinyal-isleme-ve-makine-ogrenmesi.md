# 3. Sinyal İşleme, Makine Öğrenmesi ve MATLAB Araçları

[← Ana yol haritası](README.md)

Bu dosya **Aşama 3**'ün ayrıntılarını içerir. Sıra şöyle: temel FFT'den ileri yöntemlere, oradan makine öğrenmesine ve bunların MATLAB karşılıklarına.
Gösterim [01 numaralı dosyadaki](01-temeller-ve-okuma-listesi.md) ile aynıdır.
- **Erişim:** `Açık`, `Ücretsiz kopya`, `Ücretli`.
- **Seviye:** **B** başlangıç, **O** orta, **İ** ileri.

---

## 3.1 Önerilen öğrenme sırası

1. **Örnekleme, örtüşme (aliasing), `fft` ve `periodogram`, Δf = 1/T, pencereleme, sıfır dolgusu, dB ölçeği.** MCSA'daki hataların neredeyse hepsi bu temellerden kaynaklanır.
2. **`pwelch` / `pspectrum`, `findpeaks`, `faultBands` / `faultBandMetrics`.** Kararlı rejimde sağlam arıza göstergeleri çıkarmak için.
3. **Arıza frekansı formülleri ve akımdan kayma kestirimi.** Yan bantları nerede arayacağınızı bilmek için kaymayı bilmeniz gerekir.
4. **Demodülasyon: Hilbert zarfı, Park vektörü / EPVA, anlık güç, MSCSA.** Ucuz yöntemlerdir ve temel bileşeni ortadan kaldırırlar. Düşük kaymadaki sorunların çoğunu çözerler.
5. **Zoom FFT / CZT, ardından MUSIC, root-MUSIC ve ESPRIT.** Kayıt kısa ya da kayma çok küçükse kullanılır.
6. **Geçici rejim MCSA.** Sırasıyla STFT, DWT/CWT (kalkıştaki yan bant desenleri), WVD/ZAM, EMD/VMD/HHT. Gerçek sürücüler durağan çalışmaz.
7. **Zarf spektrumu ile spektral kurtosis / kurtogram; ardından bispektrum (MSB) ve çevrimsel durağan yöntemler.** Rulman ve mekanik arızalar akımda çok zayıf modülasyonlar üretir.
8. **Elle tasarlanmış öznitelikler ve Classification Learner.** Model, eğitimde görmediği yük seviyelerinde test edilmelidir (Martin-Diaz 2018). Derin öğrenmeden önce yorumlanabilir bir temel oluşturur.
9. **Ham akımda 1-D CNN, CWT skalogramı ile CNN, ardından simülasyondan gerçeğe (sim-to-real) aktarım.** Bu adım yukarıdaki her şeyi gerektirir. Sonuçları mutlaka gerçek veride test edin (Paderborn, Treml).

---

## 3.2 MCSA için spektral analizin temelleri

**Pratik kurallar**
- **Frekans çözünürlüğü: Δf = Fs/N = 1/T** (T = kayıt süresi).
  - Kırık çubuk yan bantları temel bileşenden yalnızca 2s·f uzaktadır.
  - Örnek: f = 50 Hz ve s = %1 için yan bant 1 Hz uzaktadır. T = 10 s ile Δf = 0,1 Hz olur.
  - s = %0,3 gibi çok hafif yükte onlarca saniyelik, kararlı yükte alınmış kayıt gerekir.
- **Örnekleme ve örtüşme önleme.**
  - Fs'yi ihtiyaç duyduğunuz en yüksek çizgiye göre seçin. Rotor oluk harmonikleri, eksantriklik ve rulman çizgileri birkaç kHz'e çıkabilir.
  - ADC'den önce analog bir örtüşme önleme süzgeci kullanın.
  - Uzun kayıtları küçültmek için `decimate` kullanın; içinde örtüşme önleme süzgeci vardır.
- **Pencere seçimi.**
  - Varsayılan olarak Hann uygundur.
  - Temel bileşenden onlarca dB küçük bir yan bant birkaç kutu (bin) uzaktaysa yan lobu düşük bir pencere seçin: yüksek β'lı Kaiser (`pspectrum` fonksiyonunun `Leakage` seçeneği) ya da Blackman–Harris.
  - Flat-top penceresini yalnızca iyi ayrışmış tepelerin genliğini doğru ölçmek için kullanın. Ana lobu Hann'ınkinin yaklaşık 2,5 katıdır.
- **Sıfır dolgusu (zero padding)** spektrumu yalnızca ara değerleriyle doldurur, **çözünürlüğü artırmaz**.
- **Welch ortalaması** gürültü tabanını düşürür, ama çözünürlüğü **segment uzunluğu** belirler.
  - `pwelch` varsayılan olarak 8 segment kullanır, bu da çözünürlüğü 8 kat kötüleştirir.
  - MCSA'da segment uzunluğunu kendiniz ayarlayın.
- **Yan bant seviyesi (dB):** 20·log10(I_yb / I_temel). Bu ölçekte temel bileşen 0 dB olur.
  - Karşılaştırdığınız tüm ölçümlerde aynı pencereyi ve aynı ölçeklemeyi kullanın.
  - (1−2s)f ve (1+2s)f yan bantlarının **ikisini birden** izleyin. Hız dalgalanması enerjiyi ikisi arasında aktarır (Bellini 2001).
- **Kaymayı akımdan kestirmek.**
  - Temel oluk harmoniği f_PSH = f·[R(1−s)/p ± 1] formülüyle verilir; R rotor oluk sayısı, p kutup çifti sayısıdır.
  - Buradan s = 1 − p(f_PSH/f ∓ 1)/R elde edilir.
  - Oluk harmoniklerinin görünüp görünmemesi R–p kombinasyonuna bağlıdır (Nandi 2001).
- **Düşük kaymada maskelenme.** Hafif yükte temel bileşenin sızıntısı yan bantları gömer. Çözümler:
  - daha uzun T ve daha iyi bir pencere;
  - demodülasyon (Hilbert ya da Park vektörü modülü), arıza çizgisini 2s·f'ye taşır;
  - zoom FFT, MUSIC ya da ESPRIT;
  - kalkış (geçici rejim) analizi.

> Bu kuralların çoğunu [`matlab/mcsa_ilk_adim.m`](matlab/mcsa_ilk_adim.m) betiğinde deneyerek görebilirsiniz.

**Kaynaklar**

| Kaynak | Erişim | Seviye | Ne öğretir? |
|---|---|---|---|
| Harris, F.J. (1978). On the use of windows for harmonic analysis with the DFT. *Proc. IEEE* 66(1):51–83. [doi:10.1109/PROC.1978.10837](https://doi.org/10.1109/PROC.1978.10837) | Ücretli | B/O | Pencerelerin klasik kaynağı: sızıntı, scalloping, ana lob ile yan lob dengesi |
| Welch, P.D. (1967). *IEEE Trans. Audio Electroacoust.* 15(2):70–73. [doi:10.1109/TAU.1967.1161901](https://doi.org/10.1109/TAU.1967.1161901) | Ücretli | O | Ortalamalı periodogramın kökeni (`pwelch`) |
| Heinzel, G., Rüdiger, A., Schilling, R. (2002). *Spectrum and spectral density estimation by the DFT…* MPI teknik raporu. [PDF](https://holometer.fnal.gov/GH_FFT.pdf) · [MPG.PuRe kaydı](https://pure.mpg.de/view/item_152164) | Açık | B/O | **Çok pratik:** genlik ve yoğunluk ölçeklemesi, eşdeğer gürültü bant genişliği (ENBW), flat-top pencereler |
| Hurst, K.D., Habetler, T.G. (1996). Sensorless speed measurement using current harmonic spectral estimation in induction machine drives. *IEEE TPEL* 11(1):66–73. [doi:10.1109/63.484418](https://doi.org/10.1109/63.484418) | Ücretli | O | Hızı rotor oluk ve eksantriklik harmoniklerinden bulmak |
| Hurst & Habetler (1997). *IEEE TIA* 33(4):898–905. [doi:10.1109/28.605730](https://doi.org/10.1109/28.605730) | Ücretli | O | Kısa kayıtlarda FFT ile parametrik kestiricilerin karşılaştırması |
| Nandi, S., Ahmed, S., Toliyat, H.A. (2001). *IEEE TEC* 16(3):253–260. [doi:10.1109/60.937205](https://doi.org/10.1109/60.937205) | Ücretli | O | Hangi rotor oluk / kutup kombinasyonlarında oluk harmoniği oluştuğu |
| Puche-Panadero, R. vd. (2009). Improved resolution of the MCSA method via Hilbert transform, enabling the diagnosis of rotor asymmetries at very low slip. *IEEE TEC* 24(1):52–59. [doi:10.1109/TEC.2008.2003207](https://doi.org/10.1109/TEC.2008.2003207) | Ücretli (depo kopyası ambargolu) | O | Düşük kaymadaki sızıntı sorunu; çözüm olarak Hilbert modülü ve ardından FFT |
| Sapena-Bano, A. vd. (2015). *IEEE TEC* 30(4):1409–1419. [doi:10.1109/TEC.2015.2445216](https://doi.org/10.1109/TEC.2015.2445216) | [Ücretsiz kopya](http://hdl.handle.net/10251/99468) | O | Uzun kayıtlarda veri boyutunu küçültmek ("reduced envelope"), düşük maliyetli teşhis |

**MathWorks eğitim sayfaları**
- [Practical Introduction to Frequency-Domain Analysis](https://www.mathworks.com/help/signal/ug/practical-introduction-to-frequency-domain-analysis.html)
- [Amplitude Estimation and Zero Padding](https://www.mathworks.com/help/signal/ug/amplitude-estimation-and-zero-padding.html)
- [Spectral Analysis](https://www.mathworks.com/help/signal/ug/spectral-analysis.html)
- [Windows](https://www.mathworks.com/help/signal/ug/windows.html)
- [Measure the Power of a Signal](https://www.mathworks.com/help/signal/ug/measure-the-power-of-a-signal.html)

---

## 3.3 Gelişmiş yöntemler

### Zoom FFT / chirp-z
- **Rabiner, Schafer, Rader (1969).** The chirp z-transform algorithm. *IEEE Trans. Audio Electroacoust.* 17(2):86–92.
  - [doi:10.1109/TAU.1969.1162034](https://doi.org/10.1109/TAU.1969.1162034) · **O**
  - Spektrumu yalnızca dar bir bantta yoğun hesaplamanın yolu.
- **Bellini, Yazidi, Filippetti, Rossi, Capolino (2008).** High frequency resolution techniques for rotor fault detection of induction machines. *IEEE TIE* 55(12):4200–4209.
  - [doi:10.1109/TIE.2008.2007004](https://doi.org/10.1109/TIE.2008.2007004) · `Ücretli` · **O**
  - Şebeke frekansını ve kaymayı zaman ortamında izleyip zoom FFT'yi buna göre ayarlar.

### Yüksek çözünürlüklü alt uzay yöntemleri (MUSIC / ESPRIT)
- **Kia, S.H., Henao, H., Capolino, G.-A. (2007).** A high-resolution frequency estimation method for three-phase induction machine fault detection. *IEEE TIE* 54(4):2305–2314.
  - [doi:10.1109/TIE.2007.899826](https://doi.org/10.1109/TIE.2007.899826) · `Ücretli` · **İ**
  - Önce bir banda yakınlaşır, sonra MUSIC uygular. Kırık çubuk, farklı yüklerde test edilmiş.
- **García-Pérez, Romero-Troncoso, Cabal-Yépez, Osornio-Ríos (2011).** The application of high-resolution spectral analysis for identifying multiple combined faults in induction motors. *IEEE TIE* 58(5):2002–2010.
  - [doi:10.1109/TIE.2010.2051398](https://doi.org/10.1109/TIE.2010.2051398) · `Ücretli` · **İ**
  - Bir süzgeç bankası ve MUSIC ile **birden fazla eşzamanlı arızayı** birbirinden ayırır.
- **Xu, B., Sun, L., Xu, L., Xu, G. (2013).** Improvement of the Hilbert method via ESPRIT for detecting rotor fault in induction motors at low slip. *IEEE TEC* 28(1):225–233.
  - [doi:10.1109/TEC.2012.2236557](https://doi.org/10.1109/TEC.2012.2236557) · `Ücretli` · **İ**
  - Hilbert adımından sonra FFT yerine ESPRIT kullanır.
  - MATLAB'da hazır bir ESPRIT fonksiyonu yok; birkaç satır lineer cebirle kendiniz yazabilirsiniz.

### Demodülasyon tabanlı sinyaller

*Hilbert zarfı*
- Puche-Panadero 2009 ve Sapena-Bano 2015 (bkz. §3.2).

*Park vektörü ve genişletilmiş Park vektörü (EPVA)*
- **Cardoso, A.J.M., Saraiva, E.S. (1993).** Computer-aided detection of airgap eccentricity in operating three-phase induction motors by Park's vector approach. *IEEE TIA* 29(5):897–901.
  - [doi:10.1109/28.245712](https://doi.org/10.1109/28.245712) · **B/O**
  - Park vektörü yönteminin ilk hali: id–iq deseni.
- **Cardoso, Cruz, Fonseca (1999).** *IEEE TEC* 14(3):595–598.
  - [doi:10.1109/60.790920](https://doi.org/10.1109/60.790920) · [Ücretsiz PDF (Coimbra Üniv.)](https://estudogeral.uc.pt/bitstream/10316/12916/1/Inter-turn%20stator%20winding%20fault%20diagnosis.pdf) · **B/O**
  - Aynı yaklaşım sarımlar arası kısa devreye uygulanıyor.
- **Cruz & Cardoso (2000).** Rotor cage fault diagnosis … by extended Park's vector approach. *Electr. Mach. Power Syst.* 28(4):289–299.
  - [doi:10.1080/073135600268261](https://doi.org/10.1080/073135600268261) · **O**
- **Cruz & Cardoso (2001).** *IEEE TIA* 37(5):1227–1233.
  - [doi:10.1109/28.952496](https://doi.org/10.1109/28.952496) · **O**
  - Stator arızasında EPVA spektrumunda 2f bileşeni belirir. 5 MW'a kadar motorlarda sahada denenmiş.

*Anlık güç*
- **Legowski, Ula, Trzynadlowski (1996).** Instantaneous power as a medium for the signature analysis of induction motors. *IEEE TIA* 32(4):904–909.
  - [doi:10.1109/28.511648](https://doi.org/10.1109/28.511648) · **O**
- **Trzynadlowski & Ritchie (2000).** Comparative investigation of diagnostic media for induction motors: a case of rotor cage faults. *IEEE TIE* 47(5):1092–1099.
  - [doi:10.1109/41.873218](https://doi.org/10.1109/41.873218) · **O**
  - Karşılaştırmalı bir çalışma: rotor arızasında en duyarlı sinyal kısmi güç çıkmış.

*MSCSA:* bkz. [01 numaralı dosya, §1.1](01-temeller-ve-okuma-listesi.md).

### Spektral kurtosis ve zarf analizi (özellikle rulman için)
- **Antoni, J. (2006).** The spectral kurtosis: a useful tool for characterising non-stationary signals. *MSSP* 20(2):282–307.
  - [doi:10.1016/j.ymssp.2004.09.001](https://doi.org/10.1016/j.ymssp.2004.09.001) · **İ**
- **Antoni, J. (2007).** Fast computation of the kurtogram for the detection of transient faults. *MSSP* 21(1):108–124.
  - [doi:10.1016/j.ymssp.2005.12.002](https://doi.org/10.1016/j.ymssp.2005.12.002) · **İ**
- **Leite, V.C.M.N. vd. (2015).** Detection of localized bearing faults in induction machines by spectral kurtosis and envelope analysis of stator current. *IEEE TIE* 62(3):1855–1865.
  - [doi:10.1109/TIE.2014.2345330](https://doi.org/10.1109/TIE.2014.2345330) · **O/İ**
  - Ücretsiz kitap bölümü sürümü: [doi:10.5772/67145](https://doi.org/10.5772/67145).
- **Fournier, E. vd. (2015).** *IEEE TIE* 62(3):1879–1887.
  - [doi:10.1109/TIE.2014.2341561](https://doi.org/10.1109/TIE.2014.2341561) · [Listelenmiş ücretsiz kopya (OATAO; erişim doğrulanamadı)](https://oatao.univ-toulouse.fr/14327/7/fournier_14327.pdf) · **İ**
  - Akımdan mekanik dengesizlik tespiti.
- **Immovilli, Cocconcelli, Bellini, Rubini (2009).** *IEEE TIE* 56(11):4710–4717.
  - [doi:10.1109/TIE.2009.2025288](https://doi.org/10.1109/TIE.2009.2025288) · `Ücretli` · **O**

### Uyarlamalı ayrıştırmalar (EMD / HHT / VMD)
- **Huang, N.E. vd. (1998).** *Proc. R. Soc. A* 454:903–995.
  - [doi:10.1098/rspa.1998.0193](https://doi.org/10.1098/rspa.1998.0193) · [HAL](https://hal.science/hal-04014501/document) · **İ**
  - EMD'nin kökeni.
- **Antonino-Daviu, Riera-Guasp, Pineda-Sánchez, Pérez (2009).** A critical comparison between DWT and Hilbert–Huang-based methods for the diagnosis of rotor bar failures in induction machines. *IEEE TIA* 45(5):1794–1803.
  - [doi:10.1109/TIA.2009.2027558](https://doi.org/10.1109/TIA.2009.2027558) · [Ücretsiz kopya](http://hdl.handle.net/10251/99458) · **O**
- **Valles-Novo, R. vd. (2015).** *IEEE TIM* 64(5):1118–1128.
  - [doi:10.1109/TIM.2014.2373513](https://doi.org/10.1109/TIM.2014.2373513) · **O**
- **Dragomiretskiy & Zosso (2014).** Variational mode decomposition. *IEEE TSP* 62(3):531–544.
  - [doi:10.1109/TSP.2013.2288675](https://doi.org/10.1109/TSP.2013.2288675) · **İ**
- **Liu, X. vd. (2022).** *Energies* 15(3):1196.
  - [doi:10.3390/en15031196](https://doi.org/10.3390/en15031196) · `Açık` · **O**
  - Kalkış akımında art arda uygulanan VMD; alt yan bandın V-biçimli izi.

### Dalgacıklar ve geçici rejim (kalkış) MCSA
- **Ye, Wu, Sadeghian (2003).** *IEEE TIE* 50(6):1217–1228.
  - [doi:10.1109/TIE.2003.819682](https://doi.org/10.1109/TIE.2003.819682) · **O**
  - Mekanik arızalarda akımın dalgacık paketi ayrıştırması.
- **Douglas, Pillay, Ziarani (2004).** A new algorithm for transient motor current signature analysis using wavelets. *IEEE TIA* 40(5):1361–1368.
  - [doi:10.1109/TIA.2004.834130](https://doi.org/10.1109/TIA.2004.834130) · **O**
- **Antonino-Daviu, Riera-Guasp, Roger-Folch, Molina Palomares (2006).** *IEEE TIA* 42(4):990–996.
  - [doi:10.1109/TIA.2006.876082](https://doi.org/10.1109/TIA.2006.876082) · [Ücretsiz kopya](http://hdl.handle.net/10251/98700) · **O**
  - Kalkış akımının ayrık dalgacık dönüşümü (DWT). Ana dalgacık, örnekleme hızı ve seviye sayısının etkisini tartışır.
- **Riera-Guasp vd. (2008).** A general approach for the transient detection of slip-dependent fault components based on the DWT. *IEEE TIE* 55(12):4167–4180.
  - [doi:10.1109/TIE.2008.2004378](https://doi.org/10.1109/TIE.2008.2004378) · [Ücretsiz kopya](http://hdl.handle.net/10251/98644) · **O**
- **Pons-Llinares vd. (2011).** *IEEE TIE* 58(5):1530–1544.
  - [doi:10.1109/TIE.2010.2081955](https://doi.org/10.1109/TIE.2010.2081955) · `Ücretli` (depo kopyası ambargolu) · **İ**
- **Antonino-Daviu (2020).** *Appl. Sci.* 10(17):6137.
  - [doi:10.3390/app10176137](https://doi.org/10.3390/app10176137) · `Açık` · **B/O**
  - Geçici rejim tabanlı teşhise genel bakış.

### Karesel zaman–frekans dağılımları (Wigner–Ville, ZAM)
- **Rajagopalan, Restrepo, Aller, Habetler, Harley (2008).** *IEEE TIA* 44(3):735–744.
  - [doi:10.1109/TIA.2008.921431](https://doi.org/10.1109/TIA.2008.921431) · **İ**
- **Blodt, Bonacci, Regnier, Chabert, Faucher (2008).** *IEEE TIE* 55(2):522–533.
  - [doi:10.1109/TIE.2007.911941](https://doi.org/10.1109/TIE.2007.911941) · **İ**
  - Değişken hızlı sürücülerde mekanik arızalar.
- **Climente-Alarcón vd. (2014).** *IEEE TIE* 61(8):4217–4227.
  - [doi:10.1109/TIE.2013.2286581](https://doi.org/10.1109/TIE.2013.2286581) · [Ücretsiz kopya](http://hdl.handle.net/10251/95460) · **İ**

### Bispektrum ve çevrimsel durağanlık
- **Gu, F. vd. (2015).** A new method of accurate broken rotor bar diagnosis based on modulation signal bispectrum analysis of motor current signals. *MSSP* 50–51:400–413.
  - [doi:10.1016/j.ymssp.2014.05.017](https://doi.org/10.1016/j.ymssp.2014.05.017) · [Ücretsiz kopya](http://eprints.hud.ac.uk/id/eprint/20882/1/Current_MSB_Motor_BRB_with_Impedence_chanegs-Submmitted_to_MSSP_R1_1.pdf) · **İ**
- **Gu, F. vd. (2011).** *MSSP* 25(1):360–372.
  - [doi:10.1016/j.ymssp.2010.07.004](https://doi.org/10.1016/j.ymssp.2010.07.004) · **İ**
  - Motor akımından, motorun sürdüğü kompresördeki arızaları teşhis eder.
- **Antoni, J. (2009).** Cyclostationarity by examples. *MSSP* 23(4):987–1036.
  - [doi:10.1016/j.ymssp.2008.10.010](https://doi.org/10.1016/j.ymssp.2008.10.010) · **İ**
- Not: Çevrimsel durağan yöntemlerin motor **akımına** uygulandığı çalışma azdır; bu alandaki makalelerin çoğu titreşim üzerinedir.

### Karşılaştırmalı çalışmalar
- **Fernández-Cavero, Moríñigo-Sotelo, Duque-Pérez, Pons-Llinares (2017).** A comparison of techniques for fault detection in inverter-fed induction motors in transient regime. *IEEE Access* 5:8048–8063.
  - [doi:10.1109/ACCESS.2017.2702643](https://doi.org/10.1109/ACCESS.2017.2702643) · `Açık` · **O**
- **Immovilli, Bellini, Rubini, Tassoni (2010).** Diagnosis of bearing faults in induction machines by vibration or current signals: a critical comparison. *IEEE TIA* 46(4):1350–1359.
  - [doi:10.1109/TIA.2010.2049623](https://doi.org/10.1109/TIA.2010.2049623) · `Ücretli` · **O**

---

## 3.4 Motor akımıyla makine öğrenmesi ve derin öğrenme

**Temel ve yöntem makaleleri**
- **Filippetti, Franceschini, Tassoni, Vas (2000).** Recent developments of induction motor drives fault diagnosis using AI techniques. *IEEE TIE* 47(5):994–1004.
  - [doi:10.1109/41.873207](https://doi.org/10.1109/41.873207) · `Ücretli` · **B**
  - Arıza simülasyon modellerinin eğitim verisi sağladığını vurgular.
- **Ince, Kiranyaz, Eren, Askar, Gabbouj (2016).** Real-time motor fault detection by 1-D convolutional neural networks. *IEEE TIE* 63(11):7067–7075.
  - [doi:10.1109/TIE.2016.2582729](https://doi.org/10.1109/TIE.2016.2582729) · `Ücretli` · **O**
  - Ham motor akımı üzerinde çalışan kompakt bir 1-D CNN. Yazarlar arasında Türk araştırmacılar (L. Eren, M. Askar) var.
- **Kiranyaz vd. (2021).** 1D convolutional neural networks and applications: a survey. *MSSP* 151:107398.
  - [doi:10.1016/j.ymssp.2020.107398](https://doi.org/10.1016/j.ymssp.2020.107398) · [arXiv](https://arxiv.org/abs/1905.03554) · **B/O**
- **Martin-Diaz, Moríñigo-Sotelo, Duque-Pérez, Romero-Troncoso (2018).** *IEEE TIA* 54(3):2215–2224.
  - [doi:10.1109/TIA.2018.2801863](https://doi.org/10.1109/TIA.2018.2801863) · [Listelenmiş ücretsiz kopya (UVaDOC; erişim doğrulanamadı)](https://uvadoc.uva.es/handle/10324/64938) · **O**
  - Sınıflandırıcıları **eğitimde görülmemiş çalışma koşullarında** test eder. Gerçekçi değerlendirme protokolü budur.
- **Ali, Shabbir, Liang, Zhang, Hu (2019).** Machine learning-based fault diagnosis for single- and multi-faults in induction motors using measured stator currents and vibration signals. *IEEE TIA* 55(3):2378–2391.
  - [doi:10.1109/TIA.2019.2895797](https://doi.org/10.1109/TIA.2019.2895797) · `Ücretli` · **O**
  - 17 sınıflandırıcıyı **MATLAB Classification Learner** ile karşılaştırır. Sizin çalışmanız için doğrudan bir şablon.
- **Skowron, Orłowska-Kowalska, Wolkiewicz, Kowalski (2020).** *Energies* 13(6):1475.
  - [doi:10.3390/en13061475](https://doi.org/10.3390/en13061475) · `Açık` · **O**
  - İnverterle beslenen motorda ham akım üzerinde CNN ile sarımlar arası arıza teşhisi.
- **Ayankoso vd. (2026).** *Struct. Health Monit.* 25(1):196–212.
  - [doi:10.1177/14759217241289874](https://doi.org/10.1177/14759217241289874) · `Açık` · **O**
  - Gerçekçi bir karşılaştırma: mekanik arızalarda titreşim yaklaşık %100, akım %87,4 doğruluk vermiş.

**Derlemeler**
- **Niu, Dong, Chen (2023).** Motor fault diagnostics based on current signatures: a review. *IEEE TIM* 72:1–19.
  - [doi:10.1109/TIM.2023.3285999](https://doi.org/10.1109/TIM.2023.3285999) · **B/O**
- **Kumar vd. (2022).** *Energies* 15(23):8938 · `Açık` · **B**
- **González-Jiménez vd. (2021).** *Sensors* 21(12):4024 · `Açık` · **B**
- **Zhang, Zhang, Wang, Habetler (2020).** *IEEE Access* 8:29857–29881 · `Açık` · **O**
- **AlShorman vd. (2020).** *Shock Vib.* 2020:8843759.
  - [doi:10.1155/2020/8843759](https://doi.org/10.1155/2020/8843759) · `Açık` · **B**

**Simüle veriyle eğitip gerçek veride test etmek (sim-to-real)**
- **Ji, Wang, Inoue, Kanemaru (2025).** Simulation-to-reality domain adaptation for motor fault detection. *IEEE SDEMPED 2025*.
  - [doi:10.1109/SDEMPED53223.2025.11154252](https://doi.org/10.1109/SDEMPED53223.2025.11154252) · [Ücretsiz PDF (MERL)](https://www.merl.com/publications/docs/TR2025-126.pdf) · **İ**
  - Fizik tabanlı arıza modeliyle veri üretir, sonra az sayıda gerçek ölçümle alan uyarlaması yapar. Konu: stator akımından eksantriklik.
- **Xia vd. (2023).** *Reliab. Eng. Syst. Saf.* 235:109256.
  - [doi:10.1016/j.ress.2023.109256](https://doi.org/10.1016/j.ress.2023.109256) · **İ**
  - Dijital ikiz destekli, yarı denetimli bir yaklaşım.
- **Ali, Khizhik, Svirin, Ryzhikov, Derkach (2026).** Learning to hear broken motors: signature-guided data augmentation for induction motor diagnostics. *Eng. Appl. Artif. Intell.* 170:114137.
  - [doi:10.1016/j.engappai.2026.114137](https://doi.org/10.1016/j.engappai.2026.114137) · [arXiv](https://arxiv.org/abs/2506.08412) · **O/İ**
  - Simülasyon yerine sağlam motorun gerçek akım spektrumuna fiziksel olarak tutarlı MCSA imzaları ekler.
- **Barrera-Llanga vd. (2023).** *Sensors* 23(19):8196.
  - [doi:10.3390/s23198196](https://doi.org/10.3390/s23198196) · `Açık` · **O**
  - **Uyarıcı örnek:** Model yalnızca FEM (FEMM) verisiyle eğitilmiş ve yaklaşık %99,8 doğruluk bildirilmiş, ama **gerçek motorda test edilmemiş**.
- **Liang, Ali, Zhang (2020).** Induction motors fault diagnosis using finite element method: a review. *IEEE TIA* 56(2):1205–1217.
  - [doi:10.1109/TIA.2019.2958908](https://doi.org/10.1109/TIA.2019.2958908) · **O**
- **Hu, Xiao, Ye, Luo, Zhou (2025).** Digital twin-based fault diagnosis of electric machines. *Sensors* 25(8):2625.
  - [doi:10.3390/s25082625](https://doi.org/10.3390/s25082625) · `Açık` · **B/O**

---

## 3.5 MATLAB fonksiyonları ve uygulamaları

Bu sayfaların hepsi açılarak doğrulandı (MathWorks belgeleri R2026b).

| Fonksiyon / uygulama | Toolbox | Amaç |
|---|---|---|
| [`fft`](https://www.mathworks.com/help/matlab/ref/fft.html) | MATLAB | Ayrık Fourier dönüşümü |
| [`periodogram`](https://www.mathworks.com/help/signal/ref/periodogram.html) | Signal Processing | Tek kayıttan, seçilen pencereyle PSD ya da güç spektrumu |
| [`pwelch`](https://www.mathworks.com/help/signal/ref/pwelch.html) | Signal Processing | Welch ortalamalı PSD. Segment uzunluğunu kendiniz ayarlayın |
| [`pspectrum`](https://www.mathworks.com/help/signal/ref/pspectrum.html) | Signal Processing | Spektrum ve spektrogram; `Leakage` ve `FrequencyResolution` ayarları |
| [`hann`](https://www.mathworks.com/help/signal/ref/hann.html), [`flattopwin`](https://www.mathworks.com/help/signal/ref/flattopwin.html), [`decimate`](https://www.mathworks.com/help/signal/ref/decimate.html) | Signal Processing | Pencereler; örtüşme önleme süzgeçli alt örnekleme |
| [`czt`](https://www.mathworks.com/help/signal/ref/czt.html), [`dsp.ZoomFFT`](https://www.mathworks.com/help/dsp/ref/dsp.zoomfft-system-object.html) | Signal Processing / DSP System | Dar bir banda yakınlaşma (zoom) |
| [`pmusic`](https://www.mathworks.com/help/signal/ref/pmusic.html), [`rootmusic`](https://www.mathworks.com/help/signal/ref/rootmusic.html) | Signal Processing | MUSIC ve root-MUSIC |
| [`hilbert`](https://www.mathworks.com/help/signal/ref/hilbert.html), [`envelope`](https://www.mathworks.com/help/signal/ref/envelope.html), [`envspectrum`](https://www.mathworks.com/help/signal/ref/envspectrum.html) | Signal Processing | Analitik sinyal, zarf ve zarf spektrumu |
| [`kurtogram`](https://www.mathworks.com/help/signal/ref/kurtogram.html), [`spectralKurtosis`](https://www.mathworks.com/help/signal/ref/spectralkurtosis.html) | Signal Processing | Hızlı kurtogram ve spektral kurtosis. `pkurtosis` artık önerilmiyor |
| [`emd`](https://www.mathworks.com/help/signal/ref/emd.html), [`vmd`](https://www.mathworks.com/help/signal/ref/vmd.html), [`hht`](https://www.mathworks.com/help/signal/ref/hht.html) | Signal Processing | EMD, VMD ve Hilbert spektrumu |
| [`stft`](https://www.mathworks.com/help/signal/ref/stft.html), [`wvd`](https://www.mathworks.com/help/signal/ref/wvd.html) | Signal Processing | STFT ve Wigner–Ville |
| [`cwt`](https://www.mathworks.com/help/wavelet/ref/cwt.html), [`modwt`](https://www.mathworks.com/help/wavelet/ref/modwt.html), [`wavedec`](https://www.mathworks.com/help/wavelet/ref/wavedec.html), [`wpdec`](https://www.mathworks.com/help/wavelet/ref/wpdec.html), [`modwpt`](https://www.mathworks.com/help/wavelet/ref/modwpt.html) | Wavelet | Skalogram (CWT); kalkış analizi için DWT ve MODWT; dalgacık paketleri |
| [`findpeaks`](https://www.mathworks.com/help/signal/ref/findpeaks.html) | Signal Processing | Yan bant ve oluk harmoniği tepelerini bulmak |
| [`faultBands`](https://www.mathworks.com/help/predmaint/ref/faultbands.html), [`faultBandMetrics`](https://www.mathworks.com/help/predmaint/ref/faultbandmetrics.html), [`bearingFaultBands`](https://www.mathworks.com/help/predmaint/ref/bearingfaultbands.html) | Predictive Maintenance | Arıza bantları (belgede **kırık çubuk örneği** var: F1 = 2·s·F0) ve bant metrikleri |
| [Diagnostic Feature Designer](https://www.mathworks.com/help/predmaint/ref/diagnosticfeaturedesigner-app.html) | Predictive Maintenance | Ölçülmüş ya da simüle edilmiş veriden etkileşimli öznitelik çıkarma ve sıralama |
| [Signal Analyzer](https://www.mathworks.com/help/signal/ref/signalanalyzer-app.html) | Signal Processing | Zaman, frekans ve zaman–frekans ortamında etkileşimli inceleme |
| [Classification Learner](https://www.mathworks.com/help/stats/classificationlearner-app.html) | Statistics & ML | SVM, KNN, topluluk (ensemble) sınıflandırıcıları |
| [Deep Network Designer](https://www.mathworks.com/help/deeplearning/ref/deepnetworkdesigner-app.html) | Deep Learning | CNN ve LSTM ağları kurmak |

**Kopyalayıp uyarlayabileceğiniz MathWorks örnekleri**
- [**Broken Rotor Fault Detection in AC Induction Motors Using Vibration and Electrical Signals**](https://www.mathworks.com/help/predmaint/ug/broken-rotor-fault-detection-in-ac-induction-motors-using-vibration-and-electrical-signals.html)
  - IEEE DataPort kırık çubuk veri setini kullanır.
  - 60 Hz ve harmonikleri çevresindeki arıza bantlarından öznitelik çıkarır, ANOVA ile sıralar, KNN ile yaklaşık %98 doğruluk elde eder.
  - **Asenkron motor ve MCSA için en ilgili resmî örnek.**
- [Motor Current Signature Analysis for Gear Train Fault Detection](https://www.mathworks.com/help/predmaint/ug/motor-current-signature-analysis-for-gear-train-fault-detection.html)
  - Bir DA motorlu servo dişli kutusu.
  - Zincir: `pspectrum`, ardından `faultBands`, ardından `faultBandMetrics`.
- [Using Simulink to Generate Fault Data](https://www.mathworks.com/help/predmaint/ug/Use-Simulink-to-Generate-Fault-Data.html)
  - Simülasyonla etiketli arıza verisi üretme iş akışı. Örnekteki sistem bir şanzıman, ama yöntem motora aynen uygulanır.
- [Classify Time Series Using Wavelet Analysis and Deep Learning](https://www.mathworks.com/help/wavelet/ug/classify-time-series-using-wavelet-analysis-and-deep-learning.html)
  - CWT skalogramı ve CNN. Aynı tarif kalkış akımlarına da uygulanabilir.
