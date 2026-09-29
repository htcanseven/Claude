# 4. MATLAB/Simulink'te Arızalı Makine Modelleme ve MCSA Simülasyonu

[← Ana yol haritası](README.md)

Bu dosya, yol haritasının uygulama aşaması olan **Aşama 4**'ün ayrıntılı rehberidir.
Kaynaklar Eylül 2026'da doğrulandı; MathWorks belgeleri R2026b sürümüne aittir. Gösterim [01 numaralı dosyadaki](01-temeller-ve-okuma-listesi.md) ile aynıdır.
- **Erişim:** `Açık`, `Ücretsiz kopya`, `Ücretli`.
- **Seviye:** **B** başlangıç, **O** orta, **İ** ileri.

---

## 4.0 Başlamadan önce: planı değiştiren üç önemli gerçek

1. **Specialized Power Systems (eski SimPowerSystems) kütüphanesi R2026a'da kaldırıldı.**
   - Eski "MCSA in Simulink" makalelerinin ve File Exchange modellerinin çoğu bu kütüphanedeki *Asynchronous Machine* bloğunu kullanır.
   - MathWorks'ün [Upgrade SPS models](https://www.mathworks.com/help/simscape-electrical/ug/upgrade-sps-models-to-use-simscape-blocks.html) sayfası bunu açıkça söyler (doğrulandı). Seçenekleriniz:
     - Bu modelleri R2025b ya da daha eski bir sürümde açmak.
     - `spsConversionAssistant` ile Simscape bloklarına dönüştürmek.
     - MathWorks'ün [Simscape Electrical Support Library for Power Systems](https://www.mathworks.com/matlabcentral/fileexchange/182785-simscape-electrical-support-library-for-power-systems) paketini kullanmak.
2. **Hazır asenkron motor ya da PMSM bloklarında iç arıza parametresi yoktur.**
   - Kırık çubuk, eksantriklik ya da sarım kısa devresi için bloğa bir "arıza" ayarı giremezsiniz.
   - Simscape'in [arıza modelleme desteği](https://www.mathworks.com/help/simscape/ug/block-support.html) makine tarafında yalnızca DA motor sargı arızalarını ve manyetik alandaki *Winding* / *Magnetic Rotor* bloklarını kapsar.
   - Bu nedenle **asenkron motordaki arızaları kendi kurduğunuz denklem tabanlı modellerle** üretmeniz gerekir.
   - PMSM için başlangıç noktası MathWorks'ün [Model Faulted PMSM](https://www.mathworks.com/help/simscape-electrical/ug/motor-pmsm-faulted.html) örneğidir (§4.4).
3. **Simülasyonda sağlam motorun spektrumu gerçekte olduğundan çok daha temiz çıkar.**
   - Pineda-Sanchez vd. (2018, Tablo 1): simüle edilen sağlam motorda (1−2s)f yan bandı −160 dB, ölçülen motorda −63 dB.
   - Bir arızanın "tespit edilebilir" olduğuna karar vermeden önce modele biraz doğal asimetri, besleme dengesizliği ve gürültü ekleyin.

---

## 4.1 Model hiyerarşisi: hangi model hangi arızayı üretebilir?

| Model | Neyi temsil eder? | Üretebildiği MCSA imzaları | Simulink zorluğu | Ana kaynaklar |
|---|---|---|---|---|
| **dq (Park) modeli, simetrik** | Sağlam makinenin temel dinamiği | Arıza imzası üretemez. Yük tork salınımı eklenirse f ± f_yük yan bantları oluşur | Düşük | Ozpineci & Tolbert 2003; Krause; Ong |
| **abc faz değişkenli model, asimetrik parametreli** | Rotor fazlarından birinin direnci artırılarak kırık çubuk yaklaşık olarak temsil edilir; bir faz sargısı bölünerek sarımlar arası kısa devre modellenir | (1±2s)f yan bantları, hız dalgalanması etkisi, negatif bileşen akımı | Orta | Filippetti 1998; Bellini 2001; Tallam 2002; Arkan 2005; Bachir 2006 |
| **Çok bağlaşımlı devre modeli (MCCM) + sargı fonksiyonu (WFA)** | Her rotor çubuğu ya da çevresi ayrı bir devredir; L(θ) sargı dağılımından hesaplanır | Kırık çubuk ve uç halka arızaları; **uzay harmonikleri ve oluk harmonikleri**; WFA/MWFA ile eksantriklik | Orta–yüksek | Luo vd. 1995; Toliyat & Lipo 1995; Joksimović 2000; Faiz & Ojaghi 2009 |
| **Manyetik eşdeğer devre (MEC)** | Doyma, oluk yapısı | Doymayla birlikte arızalar | Yüksek | Ostović 1987/88; Sudhoff 2007; Sizov 2009 |
| **Sonlu elemanlar (FEM)** | En doğru model: oluklar, doyma, her tür arıza | Hepsi (referans ve doğrulama için) | Çok yüksek hesap yükü | Faiz 2007/2008; Bangura & Demerdash 1999 |
| **FEM → tablo → devre modeli (hibrit)** | FEM doğruluğunu devre modeli hızında sunar | Hepsi (özellikle PMSM için) | Yüksek | Mohammed 2007; Delfa-Baena 2026; Almandoz 2012 |

> **Kural:** dq modelleri oluk ve eksantriklik harmoniklerini **üretemez**; doğrusal modeller doymayı hesaba katmaz.
> Eksantriklik ve oluk harmoniği çalışacaksanız MCCM+WFA ya da FEM gerekir.

---

## 4.2 Sağlam makine modelleri: başlangıç noktası

| Kaynak | Erişim | Seviye | Simulink kullanıcısına ne kazandırır? |
|---|---|---|---|
| **Ozpineci, B., Tolbert, L.M. (2003).** Simulink implementation of induction machine model – a modular approach. *IEEE IEMDC 2003*, 728–734. [doi:10.1109/IEMDC.2003.1210317](https://doi.org/10.1109/IEMDC.2003.1210317) | [Ücretsiz PDF (SciSpace)](https://scispace.com/pdf/simulink-implementation-of-induction-machine-model-a-modular-zaa86u43fw.pdf) | B | **İlk adım için ideal iskelet.** Krause'un akı halkalanmalı dq modelini her denklem ayrı blok olacak şekilde kurar; abc↔dq dönüşüm blokları da içinde |
| **Ong, C.-M. (1998).** *Dynamic Simulation of Electric Machinery Using MATLAB/SIMULINK.* Prentice Hall. | Kitap | B–O | Transformatör, asenkron, senkron ve PM makine modellerini Simulink'te adım adım kurmayı öğreten klasik kitap |
| **Krause, Wasynczuk, Sudhoff, Pekarek.** *Analysis of Electric Machinery and Drive Systems*, Wiley-IEEE. 3. baskı 2013: [doi:10.1002/9781118524336](https://doi.org/10.1002/9781118524336). 4. baskı 2025: [doi:10.1002/9781394293896](https://doi.org/10.1002/9781394293896) | Kitap | O | Referans çerçevesi teorisi, abc ve qd0 modelleri. **Arıza eklerken değiştireceğiniz denklemler bunlardır** |
| **Mohan, N. (2014).** *Advanced Electric Drives: Analysis, Control, and Modeling Using MATLAB/Simulink.* Wiley. [doi:10.1002/9781118910962](https://doi.org/10.1002/9781118910962) | Kitap | B–O | Asenkron motor ve PMSM için kompakt uzay vektörü modelleri, Simulink örnekleriyle |
| **Gönen, T. (2011).** *Electrical Machines with MATLAB*, 2. baskı, CRC. [doi:10.1201/b11685](https://doi.org/10.1201/b11685) | Kitap | B | Kararlı rejim teorisi MATLAB'da; modelinizin kararlı rejimini doğrulamak için |
| **Pillay, P., Krishnan, R. (1989).** *IEEE TIA* 25(2):265–273. [doi:10.1109/28.25541](https://doi.org/10.1109/28.25541) | Ücretli | O | Klasik PMSM dq modeli |
| **Leedy (2013)**, *IEEE SoutheastCon*, [doi:10.1109/SECON.2013.6567399](https://doi.org/10.1109/SECON.2013.6567399). **Ayasun & Nwankpa (2005)**, *IEEE Trans. Educ.* 48(1):37–46, [doi:10.1109/TE.2004.832885](https://doi.org/10.1109/TE.2004.832885) | Ücretli | B | Eğitim amaçlı Simulink modelleri; boşta ve kilitli rotor testlerinden parametre bulma |
| [**File Exchange 79260** – Implementation of Induction Machine Model](https://www.mathworks.com/matlabcentral/fileexchange/79260-implementation-of-induction-machine-model) | Ücretsiz | B | Ozpineci–Tolbert tarzında modüler Simulink modeli (5,0/5 puan) |
| [**File Exchange 42174** – Modelling of Induction Motor in (a,b,c) Variables](https://www.mathworks.com/matlabcentral/fileexchange/42174-modelling-of-induction-motor-in-a-b-c-variables) | Ücretsiz | B | Hazır abc modeli; **rotor asimetrisi eklemek için iyi bir başlangıç** (eski ve küçük bir model) |
| [Simscape: Induction Machine (Squirrel Cage)](https://www.mathworks.com/help/simscape-electrical/ref/inductionmachinesquirrelcage.html) | MathWorks | B | Kendi modelinizi doğrulamak için referans blok. Arıza parametresi yok |

**Türkçe kaynaklar**
- Emrah Zerdali'nin videoları: "Asenkron Motor Modelinin Matlab/Simulink ile Gerçekleştirilmesi" [#1](https://www.youtube.com/watch?v=f2XaBVDQH9U), [#2](https://www.youtube.com/watch?v=6t-LlNF9Rg4), [#3](https://www.youtube.com/watch?v=v_CAqf-uizc).
- YÖK tezleri 152766 (Şimşek 2004, Sakarya) ve 668570 (Rahmatullah 2021, Marmara). Ayrıntılar için bkz. [05 numaralı dosya](05-veri-setleri-turkce-kaynaklar-egitimler.md).

---

## 4.3 Arızalı makine modelleme yaklaşımları

**Anahtar kitap: Toliyat, Nandi, Choi, Meshgin-Kelk (2012).** *Electric Machines: Modeling, Condition Monitoring, and Fault Diagnosis*, CRC. [doi:10.1201/b13008](https://doi.org/10.1201/b13008).
Bu aşama için en iyi tek kaynaktır. İlgili bölümler:
- Bölüm 3: sargı fonksiyonu yaklaşımı (WFA) ve değiştirilmiş WFA (MWFA)
- Bölüm 4: manyetik eşdeğer devre (MEC)
- Bölüm 5: arızalı asenkron motorun FEM ile analizi
- Bölüm 6: frekans ortamında MCSA ile teşhis
- Bölüm 9: MCSA'nın DSP üzerinde uygulanması

### a) Basitleştirilmiş kırık çubuk modelleri (dq ya da abc'de rotor asimetrisi)
**Başlangıç için önerilir.**
- **Filippetti, Franceschini, Tassoni, Vas (1998).** *IEEE TIA* 34(1):98–108.
  - [doi:10.1109/28.658729](https://doi.org/10.1109/28.658729) · **O**
  - Hız dalgalanması etkisini içeren basit bir arızalı model.
- **Bellini, Filippetti, Franceschini, Tassoni, Kliman (2001).** *IEEE TIA* 37(5):1248–1255.
  - [doi:10.1109/28.952499](https://doi.org/10.1109/28.952499) · **O**
  - Akımdaki (1±2s)f yan bantlarını, tork ve güçteki 2sf çizgisini kırık çubuk sayısıyla nicel olarak ilişkilendirir.
- **Bachir, Tnani, Trigeassou, Champenois (2006).** *IEEE TIE* 53(3):963–973.
  - [doi:10.1109/TIE.2006.874258](https://doi.org/10.1109/TIE.2006.874258) · **O**
  - Sarım kısa devresi ve kırık çubuk için kompakt modeller; minimal model kurmak için iyi.
- **Rahmatullah, Oyman Serteller, Topuz (2023).** *Int. J. Educ. Inf. Technol.* 17:7–20.
  - [doi:10.46300/9109.2023.17.2](https://doi.org/10.46300/9109.2023.17.2) · `Açık` · **B**
  - Marmara Üniversitesi. Stator kısa devresi ve kırık çubuk için dq0 modelleri Simulink'te kurulmuş; her alt sistem ayrıntılı açıklanmış.
- **Sınır:** Bu modeller yan bantları ve hız dalgalanması etkisini üretir, ama **oluk ve uzay harmoniği imzalarını üretemez**.

### b) Çok bağlaşımlı devre modeli (MCCM) ve WFA: kırık çubuk ve uç halka (İ)
- **Toliyat, Lipo, White (1991).** *IEEE TEC* 6(4):679–692.
  - [doi:10.1109/60.103641](https://doi.org/10.1109/60.103641)
  - Uzay harmoniklerini de içeren WFA endüktans hesabının kökeni.
- **Toliyat, Lipo (1995).** Transient analysis of cage induction machines under stator, rotor bar and end ring faults. *IEEE TEC* 10(2):241–247.
  - [doi:10.1109/60.391888](https://doi.org/10.1109/60.391888)
- **Luo, Liao, Toliyat, El-Antably, Lipo (1995).** Multiple coupled circuit modeling of induction machines. *IEEE TIA* 31(2):311–318.
  - [doi:10.1109/28.370279](https://doi.org/10.1109/28.370279)
  - **MCCM'nin temel kaynağı.** Her rotor çevresi bir devredir; parametreler geometriden elde edilir. Simulink'te L(θ) durum uzayı modeli kurmanın planı budur.
- **Bangura, Demerdash (1999).** *IEEE TEC* 14(4):1167–1176.
  - [doi:10.1109/60.815043](https://doi.org/10.1109/60.815043)
  - FEM ve durum uzayını birleştiren bir yaklaşım.
- **Fu vd. (2019).** *IET EPA* 13(7):889–900.
  - [doi:10.1049/iet-epa.2018.5397](https://doi.org/10.1049/iet-epa.2018.5397)
  - Tek kırık çubuk için MCCM ve rotor-dq ayrıştırması.

### c) Eksantriklik: WFA ve değiştirilmiş WFA (MWFA) (İ)
- **Toliyat, Arefeen, Parlos (1996).** *IEEE TIA* 32(4):910–918.
  - [doi:10.1109/28.511649](https://doi.org/10.1109/28.511649)
  - İlk dinamik eksantriklik simülasyonu.
- **Al-Nuaim, Toliyat (1998).** *IEEE TEC* 13(2):156–162.
  - [doi:10.1109/60.678979](https://doi.org/10.1109/60.678979)
  - Düzgün olmayan hava aralığı için MWFA.
- **Joksimović, Durović, Penman, Arthur (2000).** *IEEE TEC* 15(2):143–148.
  - [doi:10.1109/60.866991](https://doi.org/10.1109/60.866991)
  - Simetrik makinenin endüktans eğrilerini ölçekleyerek dinamik eksantrikliği ucuz yoldan modeller.
- **Faiz, Tabatabaei (2002).** *IEEE Trans. Magn.* 38(6):3654–3657.
  - [doi:10.1109/TMAG.2002.804805](https://doi.org/10.1109/TMAG.2002.804805)
  - Düzgün hava aralığı için türetilen sargı fonksiyonunun eksantrik makinede **yanlış** sonuç verdiğini gösterir. Sık yapılan bir hatadır.
- **Nandi, Bharadwaj, Toliyat (2002).** *IEEE TEC* 17(3):392–399.
  - [doi:10.1109/TEC.2002.801995](https://doi.org/10.1109/TEC.2002.801995)
  - Karma eksantriklik.
- **UPV (Valencia) grubunun hızlı modelleri:**
  - Sapena-Bano vd. 2020, *IJEPES* 117:105625, [doi:10.1016/j.ijepes.2019.105625](https://doi.org/10.1016/j.ijepes.2019.105625). [Ücretsiz kopya](https://riunet.upv.es/handle/10251/169060).
  - Terron-Santiago vd. 2022, *Sensors* 22(9):3150, [doi:10.3390/s22093150](https://doi.org/10.3390/s22093150). `Açık`.

### d) Stator sarımlar arası kısa devre
- **Tallam, Habetler, Harley (2002).** Transient model for induction machines with stator winding turn faults. *IEEE TIA* 38(3):632–637.
  - [doi:10.1109/TIA.2002.1003411](https://doi.org/10.1109/TIA.2002.1003411) · **O**
  - **Simulink sarım arızası modeli için standart temel.** Sayısal simülasyona uygun bir durum uzayı modeli ve bileşen devreleri sunar.
- **Arkan, Kostic-Perovic, Unsworth (2005).** Modelling and simulation of induction motors with inter-turn faults for diagnostics. *Electr. Power Syst. Res.* 75(1):57–66.
  - [doi:10.1016/j.epsr.2004.08.015](https://doi.org/10.1016/j.epsr.2004.08.015) · **O**
  - İki qd modeli sunar; gösterge olarak negatif bileşen akımını kullanır. İlk yazar İnönü Üniversitesi'nden M. Arkan.
- **Joksimović, Penman (2000).** *IEEE TIE* 47(5):1078–1084.
  - [doi:10.1109/41.873216](https://doi.org/10.1109/41.873216) · **İ**
  - Sarım kısa devresinde hangi akım harmoniklerinin **oluşmadığını** da açıklar.
- **Vaseghi, Takorabet, Meibody-Tabar (2009).** *PIER* 95:1–18.
  - [doi:10.2528/PIER09052004](https://doi.org/10.2528/PIER09052004) · [Ücretsiz PDF](https://www.jpier.org/ac_api/download.php?id=09052004) · **O–İ**
  - Endüktansları FEM'den alan bir sarım kısa devresi modeli.
- **Sahin, Bayazit, Keysan (2020).** *ICEM 2020*, 1273–1279.
  - [doi:10.1109/ICEM49940.2020.9270853](https://doi.org/10.1109/ICEM49940.2020.9270853) · Makale ücretli, model ücretsiz · **B–O**
  - ODTÜ. FEA ve deneyle doğrulanmış bir model; **Simulink modeli GitHub'da açık** (§4.6).

### e) PMSM sarım kısa devresi ve mıknatıs arızaları
- **Mohammed, Liu, Liu, Abed (2007).** *IEEE Trans. Magn.* 43(4):1729–1732.
  - [doi:10.1109/TMAG.2006.892301](https://doi.org/10.1109/TMAG.2006.892301) · **İ**
  - FEM'den alınan endüktans ve zıt EMK tablolarıyla hızlı devre modeli. "FEM → tablo → Simulink" iş akışının şablonu.
- **Vaseghi, Nahid-Mobarakeh, Takorabet, Meibody-Tabar (2008).** *IEEE IAS 2008*.
  - [doi:10.1109/08IAS.2008.24](https://doi.org/10.1109/08IAS.2008.24) · **O**
- **Romeral, Urresty, Riba Ruiz, Garcia Espinosa (2011).** *IEEE TIE* 58(5):1576–1585.
  - [doi:10.1109/TIE.2010.2062480](https://doi.org/10.1109/TIE.2010.2062480) · **O–İ**
  - Uzay harmoniklerini içeren PMSM modeli.
- **Jeong, Hyon, Nam (2013).** *IEEE TPEL* 28(7):3495–3508.
  - [doi:10.1109/TPEL.2012.2222049](https://doi.org/10.1109/TPEL.2012.2222049) · **İ**
- **Otava, Graf, Buchta (2015).** *IFAC-PapersOnLine* 48(4):324–329.
  - [doi:10.1016/j.ifacol.2015.07.055](https://doi.org/10.1016/j.ifacol.2015.07.055) · `Açık` · **O**
  - Simscape'te arızalı iç mıknatıslı PMSM modeli.

### f) Rulman arızaları
- **Blodt, Granjon, Raison, Rostaing (2008).** *IEEE TIE* 55(4):1813–1822.
  - [doi:10.1109/TIE.2008.917108](https://doi.org/10.1109/TIE.2008.917108) · [HAL'da ücretsiz](https://hal.science/hal-00270747/document) · **O**
  - Rulman arızası iki mekanizmayla etki eder:
    1. Radyal rotor kayması: zamanla değişen eksantriklik olarak MWFA ile modellenir.
    2. Yük tork salınımı: **Simulink'te çok kolay**, karakteristik rulman frekansında bir tork dalgalanması eklersiniz.
- **Schoen, Habetler, Kamran, Bartheld (1995).** *IEEE TIA* 31(6):1274–1279.
  - [doi:10.1109/28.475697](https://doi.org/10.1109/28.475697)
- **Salnikov, Solodkiy, Vishnyakov (2021).** *J. Phys.: Conf. Ser.* 1886:012009.
  - [doi:10.1088/1742-6596/1886/1/012009](https://doi.org/10.1088/1742-6596/1886/1/012009) · `Açık` · **B**
  - Rulman frekanslarını kullanan Simulink αβ modeli. Kısa bir çalışma, doğrulaması sınırlı.

### g) Manyetik eşdeğer devre (MEC) (İ)
- **Ostović (1988).** *IEEE TIA* 24(2):308–316. [doi:10.1109/28.2871](https://doi.org/10.1109/28.2871)
- **Sudhoff, Kuhn, Corzine, Branecky (2007).** *IEEE TEC* 22(2):259–270. [doi:10.1109/TEC.2006.875471](https://doi.org/10.1109/TEC.2006.875471)
- **Sizov, Yeh, Demerdash (2009).** *IEEE IEMDC*, 119–124. [doi:10.1109/IEMDC.2009.5075193](https://doi.org/10.1109/IEMDC.2009.5075193)
  - MEC ile sarım kısa devresi ve kırık çubuk.

### h) FEM ve eş-simülasyon (co-simulation)
- **Faiz, Ebrahimi, Sharifian (2007).** *PIER* 68:53–70.
  - [doi:10.2528/PIER06080903](https://doi.org/10.2528/PIER06080903) · [Ücretsiz PDF](https://www.jpier.org/ac_api/download.php?id=06080903)
  - Kırık çubuklu motorun zaman adımlı FEM analizi.
- **Faiz, Ebrahimi, Akin, Toliyat (2008).** *IEEE Trans. Magn.* 44(1):66–74.
  - [doi:10.1109/TMAG.2007.908479](https://doi.org/10.1109/TMAG.2007.908479)
  - Karma eksantriklik: simüle edilen spektrumu ölçümle karşılaştırır.
- **Almandoz, Ugalde, Poza, Julia (2012).** Matlab-Simulink coupling to finite element software for design and analysis of electrical machines. InTech.
  - [doi:10.5772/46476](https://doi.org/10.5772/46476) · [IntechOpen](https://www.intechopen.com/chapters/39370) · `Açık` · **B–O**
  - Tablo ile bağlama ile tam eş-simülasyonu karşılaştıran bir eğitim bölümü.
- **Di Leonardo, Popescu, Tursini, Villani (2019).** *IECON 2019*.
  - [doi:10.1109/IECON.2019.8926853](https://doi.org/10.1109/IECON.2019.8926853) · [Ücretsiz PDF](https://www.research.unipd.it/bitstream/11577/3565276/1/IECON2019%20Finite%20Elements%20Model%20Co-Simulation%20of%20an%20Induction%20Motor%20Drive%20for%20Traction%20Application.pdf)
  - ANSYS Simplorer ve Simulink eş-simülasyonunun nasıl kurulduğunu gösterir.
- **Zaabi, Bensalem, Trabelsi (2015).** *IEEE SSD*.
  - [doi:10.1109/SSD.2015.7348155](https://doi.org/10.1109/SSD.2015.7348155)
  - Maxwell 2D ve Simplorer ile PWM beslemeli, kırık çubuklu motor.
- **Delfa-Baena, Terron-Santiago, Pineda-Sanchez, Sapena-Bano (2026).** *IEEE TEC* 41(2):1740–1752.
  - [doi:10.1109/TEC.2025.3640396](https://doi.org/10.1109/TEC.2025.3640396)
  - L(θ) sağlam makine için bir kez **ücretsiz FEMM** ile çıkarılır; arızalar tensör cebiriyle eklenir; model Simulink'te çalışır.
- **Taher, Malekpour (2011).** *Math. Probl. Eng.* 2011:620689.
  - [doi:10.1155/2011/620689](https://doi.org/10.1155/2011/620689) · `Açık`
  - Zincir: Maxwell FEM, genetik algoritmayla eşdeğer rotor empedansı, Simulink.

---

## 4.4 Arızalı modelleri MATLAB/Simulink'te **uygulayan** makaleler

| # | Makale | Arıza | Model | Yeniden üretilebilir mi? | Erişim | Seviye |
|---|---|---|---|---|---|---|
| 1 | Chen, Živanović (2010). *Eur. Trans. Electr. Power* 20(5):611–629. [doi:10.1002/etep.342](https://doi.org/10.1002/etep.342) | Kırık çubuk ve stator kısa devresi | Simulink'te bağlaşımlı devre modeli | Özete göre Simulink kurulumu ayrıntılı anlatılıyor | Ücretli | O |
| 2 | Pineda-Sanchez vd. (2012). Enhanced Simulink induction motor model for education and maintenance training. *J. Syst. Cybern. Inform.* 10(2):92–97 | Rotor asimetrisi, eksantriklik | Çok devreli model + teşhis aracı | Genel denklemler var | [Ücretsiz PDF](https://www.iiisci.org/Journal/pdv/sci/pdfs/HEB064IU.pdf) | B–O |
| 3 | Rahmatullah, Oyman Serteller, Topuz (2023). [doi:10.46300/9109.2023.17.2](https://doi.org/10.46300/9109.2023.17.2) | Stator kısa devresi, kırık çubuk | dq0 + MATLAB GUI | Alt sistemler ayrıntılı açıklanmış | Açık | B |
| 4 | Sahin, Bayazit, Keysan (2020). ICEM. [doi:10.1109/ICEM49940.2020.9270853](https://doi.org/10.1109/ICEM49940.2020.9270853) | Sarım kısa devresi | VBR modeli; FEA ve deneyle doğrulanmış | **Model GitHub'da açık** | Model ücretsiz | B–O |
| 5 | Rajamany vd. (2019). *J. Electr. Comput. Eng.* 2019:4825787. [doi:10.1155/2019/4825787](https://doi.org/10.1155/2019/4825787) | Sarım kısa devresi | Simulink modeli + bileşen akımları + yapay sinir ağı | Matematiksel model verilmiş | Açık | B |
| 6 | Taher, Malekpour (2011). [doi:10.1155/2011/620689](https://doi.org/10.1155/2011/620689) | Kırık çubuk | FEM → Simulink + DWT | Hibrit iş akışını gösterir | Açık | O |
| 7 | Faiz, Ojaghi (2009). *IET EPA* 3(5):461–470. [doi:10.1049/iet-epa.2008.0206](https://doi.org/10.1049/iet-epa.2008.0206) | Statik, dinamik ve karma eksantriklik | MCCM + MWFA; tek bir Simulink programı | Analitik endüktans denklemleri verilmiş | Ücretli | İ |
| 8 | Martinez-Roman vd. (2020). *Sensors* 20(11):3058. [doi:10.3390/s20113058](https://doi.org/10.3390/s20113058) | Karma eksantriklik | Sargı tensörlü çok devreli model; Simulink | **Motor verisi Ek A'da, deneysel doğrulama var; yeniden üretilebilir** | Açık | İ |
| 9 | Pineda-Sanchez vd. (2018). *Sensors* 18(7):2340. [doi:10.3390/s18072340](https://doi.org/10.3390/s18072340) | 1 ve 2 kırık çubuk | FFT ile kurulan çok devreli model | **Motor verisi Ek A'da, deneysel karşılaştırma var** | Açık | O–İ |
| 10 | Delfa-Baena vd. (2026). [doi:10.1109/TEC.2025.3640396](https://doi.org/10.1109/TEC.2025.3640396) | Kırık çubuk | FEMM → L(θ) → Simulink | Özete göre FEMM ve Simulink kullanılmış | Açık | İ |
| 11 | Otava vd. (2015). [doi:10.1016/j.ifacol.2015.07.055](https://doi.org/10.1016/j.ifacol.2015.07.055) | PMSM: açık faz, sarım kısa devresi | Simscape | Denklemler var; GitHub'da yeniden uygulanmış | Açık | O |
| 12 | Salnikov vd. (2021). [doi:10.1088/1742-6596/1886/1/012009](https://doi.org/10.1088/1742-6596/1886/1/012009) | Rulman | Simulink αβ modeli | Kısa bir çalışma | Açık | B |

---

## 4.5 Resmî MathWorks kaynakları

**Makine blokları**
- [Induction Machine (Squirrel Cage)](https://www.mathworks.com/help/simscape-electrical/ref/inductionmachinesquirrelcage.html): tek ya da çift kafes, doyma, termal portlar. **Arıza parametresi yok.**
- [PMSM](https://www.mathworks.com/help/simscape-electrical/ref/pmsm.html): arıza parametresi yok; sayfa *Model Faulted PMSM* örneğine yönlendirir.
- [FEM-Parameterized Induction Machine](https://www.mathworks.com/help/simscape-electrical/ref/femparameterizedinductionmachinesquirrelcage.html) (R2023a+) ve [FEM-Parameterized PMSM](https://www.mathworks.com/help/simscape-electrical/ref/femparameterizedpmsm.html): FEM akı tablolarıyla çalışır. Yalnızca sağlam makine.
- *Asynchronous Machine* (Specialized Power Systems): **R2026a'da kaldırıldı.** Arşiv sayfası: [R2025b](https://www.mathworks.com/help/releases/R2025b/sps/powersys/ref/asynchronousmachine.html).

**Arıza modelleme**
- [**Model Faulted PMSM**](https://www.mathworks.com/help/simscape-electrical/ug/motor-pmsm-faulted.html) (doğrulandı)
  - 10 kutuplu, 9 oluklu yüzey mıknatıslı bir PMSM, manyetik alan blokları (Winding, Rotating Air Gap, Magnetic Rotor) ile kurulmuş.
  - Simüle ettiği arızalar: diş 1'de açık devre, diş 1'in topraklanması, diş 1'de yalıtılmış sarımlar, birinci kutbun demanyetizasyonu.
  - Sonuçlar kütüphanedeki PMSM bloğuyla karşılaştırılıyor.
  - **Sargı düzeyinde arıza içeren tek resmî makine örneği**; asenkron makine için benzer bir model kurmanın da şablonu.
- [**Classify Motor Faults Using Deep Learning**](https://www.mathworks.com/help/deeplearning/ug/classify-motor-faults-using-deep-learning.html)
  - Arızalı PMSM modelinden etiketli veri üretir ve 1-D CNN eğitir.
- Simscape arızaları: [Introduction to Simscape Faults](https://www.mathworks.com/help/simscape/ug/about-simscape-faults.html), [Analyze a DC Armature Winding Fault](https://www.mathworks.com/help/simscape/ug/add-a-fault.html).
- [Simulink Fault Analyzer](https://www.mathworks.com/products/simulink-fault-analyzer.html)
  - Modeli değiştirmeden sinyallere ve Simscape bloklarına arıza ekler.
  - Sensör ve sürücü düzeyindeki arızalar için uygundur; makinenin **içindeki** arızalar için değil.

**Predictive Maintenance Toolbox örnekleri**
- [**Broken Rotor Fault Detection in AC Induction Motors**](https://www.mathworks.com/help/predmaint/ug/broken-rotor-fault-detection-in-ac-induction-motors-using-vibration-and-electrical-signals.html): gerçek veriyle (IEEE DataPort) MCSA ve sınıflandırma. **En ilgili örnek.**
- [Motor Current Signature Analysis for Gear Train Fault Detection](https://www.mathworks.com/help/predmaint/ug/motor-current-signature-analysis-for-gear-train-fault-detection.html): spektral son işleme için şablon.
- [**Use Simulink to Generate Fault Data**](https://www.mathworks.com/help/predmaint/ug/Use-Simulink-to-Generate-Fault-Data.html)
  - Arızalar parametre ve varyant alt sistemleriyle tanımlanıyor.
  - `generateSimulationEnsemble` ile 208 simülasyon koşturulup `simulationEnsembleDatastore`'a aktarılıyor.
  - **Arıza şiddeti taramaları için bu kalıbı kopyalayın.**
  - İlgili sayfa: [Generate and Use Simulated Data Ensemble](https://www.mathworks.com/help/predmaint/ug/generate-and-use-simulated-data-ensemble.html).
- [Multi-Class Fault Detection Using Simulated Data](https://www.mathworks.com/help/predmaint/ug/multi-class-fault-detection-using-simulated-data.html): üçlü pompa modeli, 1.000 senaryo ve SVM.
- Not: Taranan belgelerde **simüle edilmiş asenkron motorda kırık çubuk, eksantriklik ya da sarım arızası gösteren resmî bir örnek bulunamadı**. Bu boşluk, kendi katkınız için bir fırsat olabilir.

**Öğrenme materyali**
- Tech Talk dizileri:
  - [Predictive Maintenance](https://www.mathworks.com/videos/series/predictive-maintenance-tech-talk-series.html)
  - [Model-Based Design for Predictive Maintenance](https://www.mathworks.com/videos/series/model-based-design-for-predictive-maintenance.html): 7 video; biri fiziksel modellerle arıza verisi üretmeyi anlatıyor.
- E-kitaplar:
  - [Predictive Maintenance with MATLAB](https://www.mathworks.com/campaigns/offers/predictive-maintenance-with-matlab.html)
  - [Introduction to Predictive Maintenance (PDF)](https://www.mathworks.com/content/dam/mathworks/ebook/predictive-maintenance-ebook-part1.pdf)
- Çözücü seçimi:
  - [Choose a Solver](https://www.mathworks.com/help/simulink/ug/choose-a-solver.html)
  - [Setting Up Solvers for Physical Models](https://www.mathworks.com/help/simscape/ug/setting-up-solvers-for-physical-models.html)

---

## 4.6 File Exchange ve GitHub

Beğeni ve tarih bilgileri Eylül 2026 itibarıyladır.

| Kaynak | İçerik | Son güncelleme | Değerlendirme |
|---|---|---|---|
| [ilkersahin78/A-Simulink-Model-for-the-Induction-Machine-with-an-Inter-Turn-Short-Circuit-Fault](https://github.com/ilkersahin78/A-Simulink-Model-for-the-Induction-Machine-with-an-Inter-Turn-Short-Circuit-Fault) | Sahin vd. (ICEM 2020) makalesinin `.slx` modeli; sağlam referans model de var | 2020-03 | **En güvenilir kaynak:** hakemli makaleye bağlı, FEA ve deneyle doğrulanmış. README'deki ipucu: "sağlam" durumu simüle etmek için arıza oranını 0,005, direnci 1000 Ω alın (sayısal hataları önler) |
| [magborresen/simscape-pmsm](https://github.com/magborresen/simscape-pmsm) | Otava 2015 temelli arızalı ve sağlam PMSM (Simscape dili) | 2023-07 | Küçük ve kullanışlı. Yazar sensörsüz FOC ile yakınsama sorunları olduğunu belirtiyor |
| [UTD-DOES/WT-ITSCF-Benchmark](https://github.com/UTD-DOES/WT-ITSCF-Benchmark) | Rüzgâr türbini jeneratörü için Simulink'te üretilmiş sarım kısa devresi verisi (76 dosya) ve modeli | 2024-06 | Kullanışlı, ama makale ve lisans belirtilmemiş |
| [dbr-ufs/machines](https://github.com/dbr-ufs/machines) / [FEX 101465](https://www.mathworks.com/matlabcentral/fileexchange/101465) | Kalkışta kırık çubuk tespiti için live script ve **gerçek akım verisi** (Souza vd. 2021, *Machines*, [doi:10.3390/machines9110250](https://doi.org/10.3390/machines9110250)) | 2021-11 | Hakemli makaleye bağlı; analiz kodunuzu test etmek için iyi |
| [jsdaiustc/BBR_fault_learning](https://github.com/jsdaiustc/BBR_fault_learning) | Ma vd., *IEEE TIM* 2023 makalesinin MATLAB kodu | 2023-07 | Güvenilir ama **ileri düzey** (yüksek çözünürlüklü kestirim). Sonraki aşamalar için |
| [FEX 79260](https://www.mathworks.com/matlabcentral/fileexchange/79260-implementation-of-induction-machine-model) | Modüler asenkron makine modeli | 2020-08 | Sağlam model için iyi bir başlangıç |
| [FEX 42174](https://www.mathworks.com/matlabcentral/fileexchange/42174-modelling-of-induction-motor-in-a-b-c-variables) | abc modeli | 2013-06 | Eski ama rotor asimetrisi eklemek için uygun |
| [FEX 9941](https://www.mathworks.com/matlabcentral/fileexchange/9941-dynamic-simulations-of-electric-machinery-using-matlab-simulink) | "Dynamic Simulations of Electric Machinery" dosyaları (40 bin indirme) | 2006 | Popüler, ama Ong'un resmî kitap dosyaları olup olmadığı *doğrulanmadı*; güncelleme gerekebilir |
| [FEX 182785](https://www.mathworks.com/matlabcentral/fileexchange/182785-simscape-electrical-support-library-for-power-systems) | MathWorks'ün SPS geçiş kütüphanesi | 2026-01 | Eski SPS modellerini R2026a ve sonrasına taşımak için |
| *Dikkat:* [FEX 49848](https://www.mathworks.com/matlabcentral/fileexchange/49848-induction-motor-fault-detection) ve arıza modellemesini belgelemeyen öğrenci depoları | — | — | Öğrenme değeri düşük |

---

## 4.7 Adım adım uygulama yolu

Tüm aşamalarda **parametreleri tam yayımlanmış tek bir motor** kullanın; böylece her aşamayı bir öncekiyle karşılaştırabilirsiniz.
Uygun seçenekler: Martinez-Roman 2020 (Ek A), Pineda-Sanchez 2018 (Ek A) ya da Sahin deposundaki parametreler.

| Aşama | Hedef ve kontrol noktası | Ana kaynaklar |
|---|---|---|
| **0. Sentetik sinyalde MCSA** | i(t) = cos(2πft) + a·cos(2π(1±2s)ft) + gürültü sinyalini `fft`, `pspectrum` ve `faultBands` ile analiz edin. Δf = 1/T ilişkisini, sızıntıyı, pencere seçimini ve dB ölçeğini öğrenin | [`matlab/mcsa_ilk_adim.m`](matlab/mcsa_ilk_adim.m); Onramp'ler; MathWorks dişli kutusu MCSA örneği |
| **1. Sağlam dq modeli** | Ozpineci–Tolbert modelini kurun. Aynı parametrelerle Simscape *Induction Machine* bloğuyla, kararlı rejimi de eşdeğer devreyle karşılaştırın | Ozpineci & Tolbert 2003; Krause; Ong; FEX 79260 |
| **2. abc modeli ve rotor asimetrisi** | Bir rotor fazının direncini artırıp (1−2s)f ve (1+2s)f yan bantlarını arayın. Yük ve eylemsizliği değiştirerek üst yan banttaki hız dalgalanması etkisini görün | FEX 42174; Filippetti 1998; Bellini 2001; Bachir 2006; Rahmatullah 2023 |
| **3. Stator sarım kısa devresi** | Önce Sahin modelini çalıştırın, sonra Tallam'ı izleyerek kendi modelinizi yazın. Kısa devre edilen sarım oranını ve arıza direncini tarayın; negatif bileşen akımını ve spektral çizgileri izleyin | Tallam 2002; Arkan 2005; Sahin 2020 ve deposu; Rajamany 2019 |
| **4. MCCM ile kırık çubuk** | 3 stator devresi, Nb rotor çevresi ve uç halka; L(θ) WFA'dan. Kırık çubuk çok büyük bir çubuk direnciyle temsil edilir. Yan bantları kırık çubuk sayısı ve konumuyla, ayrıca Aşama 2 ile karşılaştırın | Luo 1995; Toliyat & Lipo 1995; Chen & Živanović 2010; Pineda-Sanchez 2012/2018; Toliyat kitabı Böl. 3 |
| **5. MWFA ile eksantriklik** | Gerçek sargı yerleşimi ve oluk sayıları gerekir. Oluk harmoniklerini ve eksantriklik bileşenlerini arayın | Faiz & Tabatabaei 2002; Joksimović 2000; Nandi 2002; Faiz & Ojaghi 2009; Martinez-Roman 2020 |
| **6. Rulman ve PMSM** | Rulman için karakteristik frekansta tork salınımı ekleyin; isterseniz zamanla değişen eksantriklik de. PMSM için MathWorks'ün arızalı PMSM modelini kullanın | Blodt 2008; Schoen 1995; Salnikov 2021; *Model Faulted PMSM*; Otava 2015 |
| **7. Doğrulama ve veri seti üretimi** | FEMM ya da Maxwell/JMAG ile karşılaştırın, açık veri setleriyle kıyaslayın. `generateSimulationEnsemble` ya da `parsim` ile simülasyon toplulukları üretin | Delfa-Baena 2026; Faiz 2007; Almandoz 2012; veri setleri için [05 numaralı dosya](05-veri-setleri-turkce-kaynaklar-egitimler.md) |

---

## 4.8 Tipik tuzaklar

Bunlar pratik kurallardır, tek bir kaynaktan alınmamıştır.

1. **MATLAB sürümü.** Specialized Power Systems tabanlı modeller R2025b ya da öncesini veya dönüştürmeyi gerektirir. Hazır bloklar makine içindeki arızaları temsil edemez.
2. **Çözücü seçimi.** Arıza modelleri (MCCM, WFA, küçük arıza dirençleri) katıdır (stiff).
   - `ode23tb` ya da `ode15s` kullanın; RelTol 1e-5 ile 1e-6, MaxStep yaklaşık 1e-5 ile 1e-4 s arasında olsun.
   - Adımı yarıya indirince spektrum değişmiyorsa sonuç güvenilirdir.
3. **Düzgün örnekleme.** Değişken adımlı çözücünün çıktısına **doğrudan FFT uygulamayın**. Sabit örnek zamanıyla kaydedin (ör. "To Workspace", Ts = 1/Fs) ya da önce yeniden örnekleyin.
4. **Örnekleme hızı.** 50 Hz çevresindeki yan bantlar için 1–5 kHz yeterlidir.
   - Oluk ve eksantriklik harmonikleri birkaç yüz Hz ile 1–2 kHz arasındadır; bunlar için en az 5–10 kHz kullanın.
   - Örnek: 28 çubuk, 2 kutup çifti, s = 0,03, 50 Hz için temel oluk harmonikleri yaklaşık 629 ve 729 Hz'dedir.
5. **Simülasyon süresi (çözünürlük).** Δf = 1/T.
   - s = 0,03 ve 50 Hz'de yan bantlar temel bileşenden ±3 Hz uzaktadır. T = 1 s ise yalnızca 3 kutu (bin) uzakta kalırlar ve pencere sızıntısında kaybolabilirler.
   - Pratikte **T ≥ 10 s** kullanılır; hafif yükte daha uzun (s = 0,005 için ±0,5 Hz).
   - Uzun MCCM simülasyonları için Accelerator modu ya da `parsim` kullanın.
6. **Kararlı rejim.** Kalkış geçici rejimini atın; hızın ve torkun oturduğunu kontrol edin ya da simülasyonu kararlı rejim başlangıç koşullarıyla başlatın.
7. **Yük ve eylemsizlik.** Yan bant genlikleri yüke bağlıdır.
   - (1+2s)f yan bandı hız dalgalanmasına, dolayısıyla eylemsizliğe bağlıdır (Filippetti 1998; Bellini 2001).
   - İnverter harmonikleri ve kontrol döngüsü imzaları maskeleyebilir; önce sinüzoidal besleme ile çalışın.
8. **Model gerçekçiliği.** Sağlam simülasyonlar gerçekçi olmayacak kadar temizdir (−160 dB ile −63 dB örneği). Doğal asimetri, besleme dengesizliği ve gürültü ekleyin.
