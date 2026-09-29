# 5. Veri Setleri, Türkçe Kaynaklar ve Eğitimler

[← Ana yol haritası](README.md)

Bu dosya üç bölümden oluşur:
- **Aşama 5** için gerçek ölçüm veri setleri (§5.1)
- Türkçe kaynaklar ve Türk araştırmacılar (§5.2)
- Ücretsiz dersler ve videolar (§5.3)

Tüm bağlantılar Eylül 2026'da kontrol edildi.

---

## 5.1 Stator akımı içeren açık veri setleri

Simülasyon sonuçlarınızı gerçek motor verisiyle karşılaştırmak için kullanın. Hepsi **akım sinyali** içerir.

| # | Veri seti | Makine | Arızalar | Sinyaller | Lisans | Açıklayan yayın |
|---|---|---|---|---|---|---|
| 1 | **IEEE DataPort:** Experimental database for detecting and diagnosing rotor broken bar in a three-phase induction motor ([sayfa](https://ieee-dataport.org/open-access/experimental-database-detecting-and-diagnosing-rotor-broken-bar-three-phase-induction), DOI [10.21227/fmnm-bn95](https://doi.org/10.21227/fmnm-bn95)) | Asenkron motor, 1 hp, 4 kutup, 60 Hz, 1715 d/d, 34 çubuk | Sağlam ve 1–4 bitişik kırık çubuk; %12,5–100 arası 8 yük seviyesi; her koşul 10 tekrar | 3 faz gerilim ve akım (~50 kHz), 5 titreşim kanalı; ~18 s kayıtlar; .mat, 6,7 GB | Açık erişim (ücretsiz IEEE hesabı gerekir) | Treml vd. 2020. **MathWorks'ün hazır örneği bu veriyi kullanır** |
| 2 | **Paderborn KAt-DataCenter** ([sayfa](https://mb.uni-paderborn.de/kat/forschung/bearing-datacenter/data-sets-and-download)) | İnverterle beslenen PMSM, 425 W | 32 rulman: 6 sağlam, 12 yapay hasarlı, 14 gerçek (hızlandırılmış ömür testinden) hasarlı | **2 faz akım** ve titreşim, 64 kHz; hız, tork, sıcaklık | CC BY-NC 4.0 | Lessmeier vd. 2016, PHME, [doi:10.36001/phme.2016.v3i1.1577](https://doi.org/10.36001/phme.2016.v3i1.1577) |
| 3 | **KAIST** titreşim, akustik, sıcaklık ve motor akımı ([Mendeley](https://data.mendeley.com/datasets/ztmf3m7h5x/6)) | Asenkron motor, 3 hp, 4 kutup, 60 Hz | Rulman iç ve dış bilezik; hizasızlık; dengesizlik | **3 faz akım** (25,6 kHz), titreşim, mikrofon | CC BY 4.0 | Jung vd. 2023, *Data in Brief* 48:109049, [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC10036499/) |
| 4 | **KAIST PMSM stator arızaları** ([Mendeley](https://data.mendeley.com/datasets/rgn5brrgrn/5)) | 1,0 / 1,5 / 3,0 kW PMSM | Sarımlar arası kısa devre (8 seviye, %21,69'a kadar); bobinler arası kısa devre | **3 faz akım** (100 kHz), titreşim | CC BY 4.0 | Jung vd. 2023, *Data in Brief* 47:108952, [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC9957734/) |
| 5 | **NLN-EMP** pompa motoru veri seti ([4TU](https://data.4tu.nl/datasets/2b61183e-c14f-4131-829b-cc4822c369d0)) | İnverterle beslenen 11 kW ve 22 kW asenkron motor + santrifüj pompa | 11 arıza türü: **stator kısa devresi, kırık çubuk**, rulman, hizasızlık, dengesizlik, kavitasyon vb. | **3 faz akım ve gerilim** (20 kHz), titreşim | CC0 | Bruinsma vd. 2024, *Data in Brief* 52:109987, [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC10751838/) |
| 6 | **Current Signature Dataset under Varying Load** ([Mendeley](https://data.mendeley.com/datasets/gxdd74czwh/1)) | 3 fazlı asenkron motor | Rulman iç ve dış bilezik (6 hasar boyutu), kırık çubuk; 3 yük | **3 faz akım**, 10 kHz | CC BY 4.0 | — |
| 7 | **LIMAN-C** ([Mendeley](https://data.mendeley.com/datasets/kccmrf3864/1)) | 3 fazlı asenkron motorlar | Rotor çubuğu, rulman, sarımlar arası kısa devre, sağlam (480 kayıt) | **Yalnızca 3 faz akım**, ~4,1 kHz, ~4 s | CC BY 4.0 | — |
| 8 | **ITSC dataset, Guanajuato Üniv.** ([GitHub](https://github.com/ibarram/ITSC)) | Asenkron motor, 0,75 hp | Her fazda %10/20/30/40 kısa devre edilmiş sarım (13 sınıf) | 3 faz akım, yalnızca 1 kHz, 5 s | MIT | Cardenas-Cornejo vd. 2023, *Measurement* 222:113680 |
| 9 | **Zenodo: kalkış akımları** ([kayıt](https://zenodo.org/records/17048028)) | 4 özdeş asenkron motor | Sağlam, 1 ve 2 kırık çubuk, hasarlı uç halka | **Kalkış akımı**, 1150 Hz | CC BY 4.0 | Kayıtta 2 makale listeleniyor |
| 10 | **BBIM2023 (MATLAB ile simüle edilmiş)** ([Mendeley](https://data.mendeley.com/datasets/f5ksvkrp73/1)) | 2,2 kW asenkron motor (2 farklı oluk kombinasyonu) | Sağlam, 1–3 kırık çubuk | Stator, çubuk ve halka akımları, hız, 2 kHz | CC BY 4.0 | [doi:10.1016/j.iswa.2022.200167](https://doi.org/10.1016/j.iswa.2022.200167). **Kendi Simulink modelinizi kontrol etmek için yararlı** |
| 11 | **Endüstriyel ölçekli motorlar** (akım, titreşim, tork, devir; Mendeley Data) | Endüstriyel motorlar | Sargı, rulman, hizasızlık | Akım, titreşim, tork, devir | Makale açık erişimli; verinin lisansını veri sayfasından kontrol edin | Jung vd. 2025, *Data in Brief* 62:111954, [doi:10.1016/j.dib.2025.111954](https://doi.org/10.1016/j.dib.2025.111954) |

**Dikkat**
- **Akım içermeyen, ama sık kullanılan setler:** CWRU (yalnızca titreşim), MAFAULDA (titreşim ve mikrofon), University of Ottawa UOEMD-VAFCVS (titreşim, mikrofon ve sıcaklık). Bunlar MCSA için uygun değildir.
- **Ücretli ya da sorunlu IEEE DataPort setleri:**
  - Chen vd. 2026 ([10.21227/gm72-j779](https://doi.org/10.21227/gm72-j779)): abonelik gerektirir.
  - HUST PMSM ITSC 2026 ([10.21227/4jpc-qh81](https://doi.org/10.21227/4jpc-qh81)): abonelik gerektirir; kodu [GitHub](https://github.com/XHX-HUST/PMSM-ITSC)'da açık.
  - Carletti vd. 2024, sentetik kırık çubuk seti ([10.21227/5q9w-5t53](https://doi.org/10.21227/5q9w-5t53)): abonelik gerektirir.
  - Goh 2025 ([10.21227/0kwj-g017](https://doi.org/10.21227/0kwj-g017)): sayfada "dosyalar yüklenmedi" yazıyor, kaçının.

**Öneri**
- **İlk veri seti olarak #1'i (IEEE DataPort) seçin.** Kırık çubuk içeriyor, akım 50 kHz'te örneklenmiş ve MathWorks'ün [hazır örneği](https://www.mathworks.com/help/predmaint/ug/broken-rotor-fault-detection-in-ac-induction-motors-using-vibration-and-electrical-signals.html) var.
- Rulman ve stator arızaları için #3 ve #4'ü (KAIST, CC BY) ekleyin.
- İnverterle beslenen motorda çok sayıda arıza türü için #5'i (CC0) kullanın.

---

## 5.2 Türkçe kaynaklar

### a) Makaleler (DergiPark ve EMO)

| Başlık | Yazarlar, dergi, yıl | Neden yararlı? |
|---|---|---|
| **Asenkron Motorların Elektriksel ve Mekaniksel Arızalarının Değerlendirilmesi** ([DergiPark](https://dergipark.org.tr/tr/pub/tbed/article/300598)) | Koca & Ünsal, SDÜ Teknik Bilimler Dergisi 7(2):37–46, 2017 | **Başlangıç için Türkçe derleme:** stator, rotor ve rulman arızaları. Buradan başlayın |
| **Motor Akım İmza Analizinde Park Dönüşümüyle Temel Harmonik Bastırımı** ([PDF](https://www.emo.org.tr/ekler/6a06bf0de91d353_ek.pdf?dergi=882)) | Güran & Eren, EMO Bilimsel Dergi 2(3):45–49, 2012 | Kırık çubuk yan bantlarını görmek için temel bileşeni Park d-ekseniyle bastırma |
| **Asenkron motorlarda eşzamanlı kırık rotor çubukları ve statik eksenel kaçıklık arızalarının stator akımı ve titreşim sinyalleri analizi ile tespiti** ([DergiPark](https://dergipark.org.tr/tr/pub/gazimmfd/article/697785)) | Kabul & Ünsal, Gazi Üniv. MMF Dergisi 36(4), 2021 | Kırık çubuk ve statik eksantriklik birlikte; Hilbert zarfı; 4 yük seviyesi |
| **Sürücüden Beslenen Asenkron Motorlarda Rulman Arızalarının Stator Akımı Kullanarak Tespiti** ([DergiPark](https://dergipark.org.tr/tr/pub/ijeased/issue/47170/578464)) | Akkurt & Arabacı, 2019 | İnverterle beslenen motorda stator akımından rulman arızası; yapay sinir ağı |
| **Yapay Sinir Ağlarıyla Asenkron Motor Çoklu Arızalarının Tespiti ve Sınıflandırılması** ([DergiPark](https://dergipark.org.tr/tr/pub/politeknik/article/933826)) | Kaya & Ünsal, Politeknik Dergisi 25(4), 2022 | 3 kW motor: stator kısa devresi, kırık çubuk, rulman |
| **Kırık Rotor Çubuğu Sayısının Ampirik Mod Ayrışımı ve Makine Öğrenmesi Yaklaşımları İle Belirlenmesi** ([DergiPark](https://dergipark.org.tr/tr/pub/fumbd/article/1289156)) | Dişli, Gedikpınar & Şengür, FÜ Müh. Bil. Dergisi 35(2), 2023 | EMD ile SVM, kNN ve karar ağacı |
| **Kırık Rotor Çubuğu Arızalarının Belirlenmesinde Derin Öğrenme Yaklaşımları ve Motor Akım İmza Analizi** ([DergiPark](https://dergipark.org.tr/tr/pub/tdfd/article/1487442)) | Aydın & Akın, Türk Doğa ve Fen Dergisi 13(3), 2024 | Açık bir veri setinde derin öğrenme ile MCSA |
| **Asenkron Motor Rotor Arızalarının Analizi** ([DergiPark](https://dergipark.org.tr/en/pub/dpufbed/article/402936)) | Ünsal & Karakaya, DPÜ Fen Bil. Enst. Dergisi 34, 2015 | Kırık çubukta FEM (Maxwell 2D/3D); akım ve tork spektrumları |
| **Asenkron Motorlarda Kırık Rotor Çubuğu Arızası Analizi İçin Bir Deney Seti Geliştirilmesi** ([PDF](https://www.emo.org.tr/ekler/3e11524fd294406_ek.pdf)) | Tezcan & Çanakoğlu, EMO bildirisi | Kırık çubuk deney düzeneği nasıl kurulur |

### b) YÖK tezleri

Açmak için [tez.yok.gov.tr](https://tez.yok.gov.tr/UlusalTezMerkezi/) → **Detaylı Tarama** → **Tez No** ile arayın. Bazı PDF'lere yazar erişim kısıtı koymuş olabilir.

**MATLAB/Simulink ile modelleme (sizin için öncelikli):**

| Tez No | Başlık | Yazar (yıl), üniversite, tür; danışman | İçerik |
|---|---|---|---|
| 232341 | **Asenkron motorlarda oluşan arızaların modellenmesi ve analizi** | Şenol M. (2008), İnönü, YL; dan. M. Arkan | Stator sarım kısa devreli motor modeli **MATLAB Simulink**'te; akımın FFT'si |
| 292511 | **Asenkron motorlarda rotor kırıkları analizi ve modellenmesi** | Kara Ö. (2011), Dumlupınar, YL; dan. A. Ünsal | Kırık çubuk **MATLAB/Simulink**'te modellenmiş ve deneyle karşılaştırılmış; öğretici |
| 668570 | **Asenkron motorun dinamik davranışlarının dq referans sistemleri çerçevesinde matlab/simulink ile eğitim amaçlı incelenmesi** | Rahmatullah R. (2021), Marmara, YL | Sağlam ve arızalı motor qd0 çerçevesinde, Simulink'te |
| 718185 | Asenkron motorlarda motor akım sinyali analiz yöntemine göre stator sargı hatasının ön tespiti (İngilizce) | Deniz B. (2021), Lefke Avrupa Üniv., YL; dan. S. Biricik | Sağlam ve sarım kısa devreli **Simulink** modeli; %0–100 yük; MCSA |
| 152766 | **MATLAB/SIMULINK ortamında asenkron motor simülasyonu** | Şimşek M. (2004), Sakarya, YL | Temel qd0 modeli; arızaları ekleyeceğiniz iskelet |
| 523538 | **Stator kısa devre arızasının sürekli mıknatıslı senkron motor performansına etkilerinin araştırılması** | Lale T. (2018), Dicle, YL | Vektör kontrollü PMSM'de %2 / %12,5 / %25 sarım kısa devresi, Simulink |
| 477668 | **Sürekli mıknatıslı senkron motorun stator kısa devre arızasının tespiti ve arıza şiddetinin otomatik olarak belirlenmesi** | Çıra F. (2017), İnönü, Doktora; dan. M. Arkan | PMSM sarım kısa devresi: tespit ve şiddet kestirimi |
| 223359 | **Asenkron motor arızalarının dinamik parametrelere etkisi ve frekans analizi ile tanısı** | Özelgin İ. (2006), İTÜ, YL | Eksantriklik ve rulman için sargı fonksiyonu endüktansları; akım spektrumları |
| 712636 | **Asenkron motor rotor arızlarının modellenmesi, simulasyonu ve analizi** | Ekinci İ. (2022), İnönü, YL; dan. M. Arkan | Kırık çubuğun Maxwell FEM modeli; MCSA ile kaçak akı karşılaştırması |

**Deneysel MCSA ve sinyal işleme:**

| Tez No | Başlık | Yazar (yıl), üniversite |
|---|---|---|
| 424287 | **Yük salınımı durumunda asenkron motorda rotor çubuk arızasının gerçek zamanlı tespiti** (kırık çubuğu yük salınımından ayırmak; DTC sürücüler) | Göktaş T. (2015), İnönü, Doktora; dan. M. Arkan |
| 337878 | **Asenkron motorlarda rotor arızalarının stator akımı verileri yardımıyla analizi ve tespiti** | Kabul A. (2013), Dumlupınar, YL |
| 599779 | Detection of broken rotor bars in induction motors using MCSA (İngilizce) | Mohamed M.A. (2019), Selçuk, YL |
| 167519 | **Asenkron motorlarda kırık rotor çubuğu arızalarının yapay sinir ağları ile teşhisi** | Arabacı H. (2005), Selçuk, YL |
| 322707 | **Evirici ile sürülen asenkron motorlarda rotor çubuğu kırık arızasının tespiti** | Doğruer T. (2012), Gaziosmanpaşa, YL |
| 292821 | Park dönüşümü ve dalgacık paketi ile kırık çubuk tespiti (İngilizce) | Güran F. (2011), Bahçeşehir, YL; dan. L. Eren |
| 821853 | **Asenkron motorlarda çoklu hataların akım sıfır geçiş anı ile gerçek zamanlı tahmini** | Çakı E. (2023), SDÜ, Doktora |
| 835668 | **Asenkron motorlarda çoklu rotor çubuğu arızalarının evrişimsel sinir ağları yaklaşımı ile teşhisi** | Dişli F. (2023), Fırat, Doktora |
| 223188 | Monitoring of the incipient bearing damage in induction motors using intelligent techniques | Şengüler T. (2008), İTÜ, YL; dan. S. Şeker |
| 352404 | **Asenkron motorda eksen kaçıklığının analizi** | Polat A. (2013), İTÜ, YL |
| 606205 | **Sürekli mıknatıslı senkron motorlarda eksantriklik arızasının tespiti** | Gür M. (2019), İnönü, YL; dan. T. Göktaş |

### c) Uluslararası yayın yapan Türk araştırmacılar

- **Müslüm Arkan** (İnönü Üniv.). Not: bazı kaynaklarda "Muhammet" diye geçiyor; YÖK kayıtlarında "Müslüm".
  - Arkan, Kostic-Perovic & Unsworth (2005). Modelling and simulation of induction motors with inter-turn faults for diagnostics. *EPSR* 75:57–66. [doi:10.1016/j.epsr.2004.08.015](https://doi.org/10.1016/j.epsr.2004.08.015)
  - Göktaş, Arkan & Özgüven (2015). *Electrical Engineering* 97:337–345. [doi:10.1007/s00202-015-0342-5](https://doi.org/10.1007/s00202-015-0342-5). Yük salınımı altında kırık çubuk.
  - Göktaş & Arkan (2018). *Trans. Inst. Meas. Control*. [doi:10.1177/0142331216654964](https://doi.org/10.1177/0142331216654964). DTC sürücüler.
- **Taner Göktaş** (İnönü, 2021'den beri Dokuz Eylül).
  - Göktaş, Zafarani & Akın (2016). Discernment of broken magnet and static eccentricity faults in PMSMs. *IEEE TEC* 31:578–587. [doi:10.1109/TEC.2015.2512602](https://doi.org/10.1109/TEC.2015.2512602)
- **Serhat Şeker ve Emine Ayaz** (İTÜ).
  - Şeker & Ayaz (2003). *J. Franklin Inst.* 340(2):125–134. Dalgacıklarla rulman hasarı.
  - Ayaz vd. (2009). *EPCS* 37(5):533–546. Akım ve titreşim arasındaki koherans.
- **Levent Eren** (İzmir Ekonomi Üniv.).
  - Eren & Devaney (2004). Bearing damage detection via wavelet packet decomposition of the stator current. *IEEE TIM* 53(2):431–436.
  - Ince, Kiranyaz, Eren, Askar & Gabbouj (2016). *IEEE TIE* 63(11):7067–7075. [doi:10.1109/TIE.2016.2582729](https://doi.org/10.1109/TIE.2016.2582729). Motor akımında 1-D CNN.
- **Hakan Çalış** (SDÜ).
  - Çalış & Çakır (2007). Rotor bar fault diagnosis … by monitoring fluctuations of motor current zero crossing instants. *EPSR* 77(5–6):385–392. [doi:10.1016/j.epsr.2006.03.017](https://doi.org/10.1016/j.epsr.2006.03.017)
- **Hayri Arabacı** (Selçuk).
  - Arabacı & Bilgin (2010). *Neural Comput. Appl.* 19:713–723. [doi:10.1007/s00521-009-0330-7](https://doi.org/10.1007/s00521-009-0330-7)
- **Abdurrahman Ünsal ve Ahmet Kabul** (Kütahya Dumlupınar).
  - Kabul & Ünsal (2021). *tm – Technisches Messen* 88(1):45–58. [doi:10.1515/teme-2020-0066](https://doi.org/10.1515/teme-2020-0066)
- **İzzet Y. Önel** (YTÜ).
  - Önel & Benbouzid (2008). *IEEE/ASME TMECH* 13(2):257–262. [doi:10.1109/TMECH.2008.918535](https://doi.org/10.1109/TMECH.2008.918535). Park ve Concordia yaklaşımlarıyla rulman arızası.
- **Mehmet Akar** (Tokat GOP).
  - Akar & Çankaya (2012). *Turk J Elec Eng & Comp Sci* 20:1077–1089. [doi:10.3906/elk-1102-1050](https://doi.org/10.3906/elk-1102-1050). İnverterle beslenen motorda kırık çubuk.
- **Zafer Doğan** (Tokat GOP).
  - Doğan & Tetik (2021). *IEEE Access* 9:92101–92112. Şebekeden kalkışlı PMSM'de sarım kısa devresi.
- **Ozan Keysan** (ODTÜ).
  - Sahin, Bayazit & Keysan (2020). *ICEM*. Açık kaynak Simulink sarım kısa devresi modeli; bkz. [04 numaralı dosya](04-matlab-simulink-modelleme.md).
- **Bilal Akın.**
  - Akın, Orguner, Toliyat & Rayner (2008). *IEEE TIE* 55(2):610–619. İnverter harmoniklerinin arıza imzalarına etkisi.

**Özet:** İnönü Üniversitesi grubu (Arkan, Göktaş), arıza modelleme ve MCSA konusunda en aktif Türk ekibidir.

### d) Türkçe kitaplar

Doğrudan arıza teşhisine ya da MCSA'ya ayrılmış bir Türkçe ders kitabı **bulunamadı**. Bu alandaki en yakın Türkçe kaynaklar Koca & Ünsal derlemesi ve yukarıdaki tezlerdir.
Makine modelleme için:
- Sarıoğlu, Gökaşan & Boğosyan. *Asenkron Makinalar ve Kontrolü*. Birsen, 2003. Tanıtımına göre MATLAB/Simulink simülasyonları içeriyor.
- İ. Çolak. *Elektrik Makinaları – 2 (Asenkron Motorlar – Senkron Makinalar)*. Seçkin, 4. baskı 2017. MATLAB programları içeriyor.
- Chapman. *Elektrik Makinalarının Temelleri*. Türkçe çevirisi E. Akın & A. Orhan.
- U. Arifoğlu. *Güç Elektroniği Devreleri MATLAB ve Simulink Çözümleri*. Palme.

---

## 5.3 Dersler, videolar ve web seminerleri

### a) MathWorks (ücretsiz)

**Onramp kursları.** Tarayıcıda, sertifikalı, her biri yaklaşık 2 saat. Önerilen sıra:
1. [MATLAB Onramp](https://matlabacademy.mathworks.com/details/matlab-onramp/gettingstarted)
2. [Simulink Onramp](https://matlabacademy.mathworks.com/details/simulink-onramp/simulink)
3. [Signal Processing Onramp](https://matlabacademy.mathworks.com/details/signal-processing-onramp/signalprocessing)
4. [Simscape Onramp](https://matlabacademy.mathworks.com/details/simscape-onramp/simscape)
5. [Machine Learning Onramp](https://matlabacademy.mathworks.com/details/machine-learning-onramp/machinelearning)

Ek kurslar: [Power Electronics Simulation Onramp](https://matlabacademy.mathworks.com/details/power-electronics-simulation-onramp/powerelectronics), [Deep Learning Onramp](https://matlabacademy.mathworks.com/details/deep-learning-onramp/deeplearning).

**Videolar**
- [Predictive Maintenance Tech Talks](https://www.mathworks.com/videos/series/predictive-maintenance-tech-talk-series.html): akım öznitelikleriyle kullanacağınız iş akışı, Diagnostic Feature Designer dahil.
- [Understanding Wavelets](https://www.mathworks.com/videos/series/understanding-wavelets-121287.html): 4 bölüm.
- [Motor Control Tech Talks](https://www.mathworks.com/videos/series/brushless-dc-motors.html): Clarke ve Park dönüşümleri; Park vektörü teşhisinde kullanılan dönüşümün aynısı.
- MATLAB kanalı:
  - [Understanding the DFT and the FFT](https://www.youtube.com/watch?v=QmgJmh2I3Fw) (19 dk)
  - [How to Do FFT in MATLAB](https://www.youtube.com/watch?v=XEbV7WfoOSE) (5 dk)
- Web semineri: [Identifying Motor Faults using Machine Learning for Predictive Maintenance](https://www.mathworks.com/videos/identifying-motor-faults-using-machine-learning-for-predictive-maintenance-1665008342485.html) (37 dk, 2023). Asenkron motor verisi, öznitelik sıralama, modelden sentetik veri üretimi.

### b) Üniversite dersleri

- **NPTEL, IIT Kharagpur (Prof. A. R. Mohanty): *Machinery Fault Diagnosis and Signal Processing***
  - [NPTEL](https://nptel.ac.in/courses/112105232) · [YouTube listesi](https://www.youtube.com/playlist?list=PLbMVogVj5nJQBOIBP4eAQSqkFvZ9vDuSb)
  - Doğrudan ilgili dersler:
    - [Lec-35 Motor Current Signature Analysis](https://www.youtube.com/watch?v=nrDPbTvICZg) (47 dk)
    - [Lec-34 Fault Detection in Motors and Transformers](https://www.youtube.com/watch?v=JO4wlkcBtls)
    - Yeni sürümden: [Lec 46 Principles of MCSA](https://www.youtube.com/watch?v=lY6LbfNbfsY) ve [Lec 47 Faults in Electrical Machines](https://www.youtube.com/watch?v=qd1uaGu_PjU)
- **NPTEL, *Modelling and Analysis of Electric Machines*** ([liste](https://www.youtube.com/playlist?list=PLbMVogVj5nJQBG9363J1uq5Fnq4m1yGXL)): Simulink motor modellerinin temeli olan dq modelleme.
- **MIT OCW 6.685 Electric Machines** (Kirtley): [ders](https://ocw.mit.edu/courses/6-685-electric-machines-fall-2013/). Bölüm 10, [Induction Machine Control and Simulation](https://ocw.mit.edu/courses/6-685-electric-machines-fall-2013/resources/mit6_685f13_chapter10/), Simulink için doğrudan yararlı.
- **ODTÜ OCW EE362** (Doç. Dr. Ozan Keysan, İngilizce): [OCW](https://ocw.metu.edu.tr/course/view.php?id=336) · [YouTube](https://www.youtube.com/playlist?list=PLCo39oJ_0NZ6p_x84g0-aziUpNtYWQhpd). Asenkron makine eşdeğer devresi ve testleri.
- **Coursera** (ücretsiz izlenebilir):
  - EPFL [Digital Signal Processing 1](https://www.coursera.org/learn/dsp1)
  - CU Boulder [Motors and Motor Control Circuits](https://www.coursera.org/learn/motors-circuits-design)

### c) Türkçe YouTube

- **Emrah Zerdali**, "Asenkron Motor Modelinin Matlab/Simulink ile Gerçekleştirilmesi": [#1](https://www.youtube.com/watch?v=f2XaBVDQH9U), [#2](https://www.youtube.com/watch?v=6t-LlNF9Rg4), [#3](https://www.youtube.com/watch?v=v_CAqf-uizc). Arızaları ekleyeceğiniz modeli adım adım kuruyor.
- **Prof. Dr. Mustafa Engin Başoğlu**:
  - [Asenkron Motorlar](https://www.youtube.com/watch?v=jopt_vkT6zY)
  - [Elektrik Makineleri II listesi](https://www.youtube.com/playlist?list=PL6do-XK0UIoCPlwtfWJDgiguiqQUa3l5Y)
- **Prof. Dr. Ahmet Orhan**: [Elektrik Makinaları II listesi](https://www.youtube.com/playlist?list=PLJsoj4b_RgXFY3LoeBW5Wy4QPo--KlXYB)
- **FİGES**: [MATLAB & Simulink ile Modelleme](https://www.youtube.com/watch?v=H2ale2CFIy0) (Türkçe)
- **Fourier ve FFT**:
  - BUders [Fourier Dönüşümü listesi](https://www.youtube.com/playlist?list=PLcNWqzWzYG2ux-p7sRKdSFcJxJc2TFp7R)
  - [DTFT Matlab Örneği](https://www.youtube.com/watch?v=oliiLMFyFEA)

### d) Endüstriden web seminerleri

- Fluke Reliability: ["How today's advanced electric motor testing technologies expose motor failure"](https://www.youtube.com/watch?v=zj9h_6GGUZk) (62 dk)
- Howard Penrose: ["Electrical and Current Signature Analysis"](https://www.youtube.com/watch?v=_SAHGrieSEI) (15 dk, başlangıç)
- motordoc: ["Electrical Signature Analysis Part 1"](https://www.youtube.com/watch?v=14BQMPYnMY4) (10 dk)
- IEEE PES Thailand: ["Diagnostics on Motors & Generators Webinar"](https://www.youtube.com/watch?v=S89nTXqQALw) (78 dk)

Not: Antonino-Daviu, Thomson, Habetler ya da Toliyat'ın ücretsiz kaydedilmiş bir dersi bulunamadı. Bu isimler için yazılı eserlerine başvurun ([01 numaralı dosya](01-temeller-ve-okuma-listesi.md)).
