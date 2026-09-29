# Elektrik Makinelerinde MCSA ile Arıza Teşhisi: Öğrenme ve Uygulama Yol Haritası

Bu belge, **Motor Akım İmza Analizi (MCSA)** ile elektrik makinelerinde arıza teşhisi çalışmak isteyen, konuya yeni başlayan bir araştırmacı için hazırlandı.
Amaç iki aşamalıdır:
1. Konuyu **derinlemesine anlamak**.
2. Öğrendiklerinizi **MATLAB/Simulink ortamında uygulamak**.

Kaynaklar Eylül 2026'da tek tek doğrulandı (DOI, URL, erişim durumu). Ayrıntılı listeler ayrı dosyalardadır:

| Dosya | İçerik |
|---|---|
| **README.md** (bu dosya) | Büyük resim, temel bağıntılar, aşamalar, takvim, araştırma fikirleri |
| [01-temeller-ve-okuma-listesi.md](01-temeller-ve-okuma-listesi.md) | Kısaltmalar, arıza istatistikleri, sıralı okuma listesi, derlemeler, kitaplar, standartlar, arama dizeleri |
| [02-ariza-turleri-ve-imzalari.md](02-ariza-turleri-ve-imzalari.md) | Her arıza türünün fiziği, akım spektrumundaki formülü, tuzakları ve temel makaleleri |
| [03-sinyal-isleme-ve-makine-ogrenmesi.md](03-sinyal-isleme-ve-makine-ogrenmesi.md) | FFT temelleri, ileri yöntemler (Hilbert, MUSIC, dalgacık…), makine öğrenmesi, MATLAB fonksiyonları |
| [04-matlab-simulink-modelleme.md](04-matlab-simulink-modelleme.md) | Arızalı makine modelleri, Simulink uygulama makaleleri, MathWorks kaynakları, GitHub/File Exchange, tuzaklar |
| [05-veri-setleri-turkce-kaynaklar-egitimler.md](05-veri-setleri-turkce-kaynaklar-egitimler.md) | Akım içeren açık veri setleri, Türkçe makale/tez/video kaynakları, ücretsiz dersler |
| [matlab/](matlab/) | İlk alıştırma: sentetik akımda kırık çubuk yan bantlarının FFT ile bulunması (MATLAB ve Octave'da çalışır) |

---

## Kısaltma notu: "MSCA" değil, "MCSA"

Literatürde yerleşik terim **MCSA — Motor Current Signature Analysis**'tir (Türkçesi: Motor Akım İmza Analizi).
"MSCA" arandığında sonuçların çoğu *Marie Skłodowska-Curie Actions* ile ilgili çıkar; aramalarınızda **MCSA** kullanın.

Yakın terimler:
- **ESA** (Electrical Signature Analysis): akım, gerilim ve gücü birlikte inceler.
- **MSCSA** (Motor *Square* Current Signature Analysis): akımın karesinin spektrumunu kullanır; MCSA'nın niş bir varyantıdır (Pires vd. 2013).
- **EPVA**: genişletilmiş Park vektörü yaklaşımı.

Ayrıntılar: [01 §1.1](01-temeller-ve-okuma-listesi.md#11-kısaltma-notu-msca-değil-mcsa).

---

## 1. MCSA bir sayfada

**Temel fikir.** Motordaki elektriksel ya da mekanik bir asimetri hava aralığındaki manyetik akıyı, rotor hızını ya da torku periyodik olarak **modüle eder**. Örnekler: kırık rotor çubuğu, eksantriklik, rulman hasarı, sarım kısa devresi, yük salınımı.
Bu modülasyon stator akımında, şebeke frekansının etrafında **yan bantlar** ya da ek harmonikler olarak görünür.
Böylece motorun kendisi bir sensör gibi davranır. Tek bir akım trafosu ya da akım probu yeterlidir:
- motora dokunmadan (non-invaziv),
- motor çalışırken,
- çoğu zaman uzaktaki motor kontrol panosundan ölçüm yapılabilir.

**Tipik MCSA zinciri**
1. **Ölçüm:** Genellikle tek faz stator akımı.
   - Örnekleme frekansı birkaç kHz ile onlarca kHz arasında seçilir; ADC'den önce örtüşme önleme (anti-aliasing) süzgeci kullanılır.
   - Kayıt süresi T, gereken frekans çözünürlüğünü belirler: **Δf = 1/T**.
2. **Ön işleme:** DC bileşenin çıkarılması. Gerekirse temel bileşenin bastırılması ya da alt örnekleme.
3. **Spektrum:** Pencereli FFT ya da Welch yöntemi. Genlikler **temel bileşene göre dB** cinsinden ifade edilir.
4. **Kayma/hız:** Takometreden ölçülür ya da akımdan (rotor oluk harmoniklerinden) kestirilir. Arıza frekansları kaymaya bağlıdır.
5. **Arıza frekanslarının hesaplanması:** Formüllerle (§2) hesaplanır, spektrumda bu frekanslardaki genlikler okunur.
6. **Karar:**
   - Eşik değer; örneğin yan bant temel bileşenin 45 dB ya da daha az altındaysa kafes arızası şüphesi (Culbert & Letal 2015). Kademeli şiddet tablosu için bkz. [02 (a)](02-ariza-turleri-ve-imzalari.md).
   - Aynı yük seviyesinde trend izleme.
   - İstatistiksel yöntemler ya da makine öğrenmesi.

**Neden MCSA?**
- Ucuz ve non-invaziv.
- Hem elektriksel hem mekanik arızaları görebilir; motorun sürdüğü yükteki (pompa, dişli kutusu) arızaları bile yakalayabilir.
- Endüstride yerleşik bir yöntemdir; ISO 20958:2013 bu yöntemi tanımlar.

**Sınırlamalar.** Bunların her biri aynı zamanda bir araştırma konusudur.
- **Hafif yükte kayma küçüktür.** Yan bantlar temel bileşene çok yaklaşır ve pencere sızıntısında kaybolur.
- **Kayma doğru bilinmelidir.** Birkaç d/d'lik hız hatası sağlam motorda yanlış alarma yol açabilir (Bonet-Jara vd. 2021).
- **Düşük frekanslı yük salınımları** kırık çubuk yan bantlarını taklit edebilir.
- **İnverter beslemesi ve kapalı çevrim kontrol** imzaları değiştirir ya da maskeler.
- **Rulman arızaları** akımda çok zayıf iz bırakır; tespit edilebilirlikleri tartışmalıdır.
- **Eşikler** motora ve yüke bağlıdır; mutlak eşik yerine trend izlemek esastır.

**Motivasyon.** Büyük motor anketlerinde arızaların yaklaşık dağılımı şöyledir (IEEE 1985, EPRI 1986; ayrıntı [01 §1.2](01-temeller-ve-okuma-listesi.md)):

| Rulman | Stator | Rotor | Diğer |
|---|---|---|---|
| %41–44 | %26–36 | %8–9 | %14–22 |

MCSA en güçlü sonuçları rotor kafesi ve eksantriklik arızalarında verir.

---

## 2. Cep kartı: temel bağıntılar

**Temel büyüklükler**
- **Senkron hız:** n_s = 60·f_s / p [d/d]
- **Kayma:** s = (n_s − n) / n_s
- **Rotor dönme frekansı:** f_r = n/60 = (1 − s)·f_s / p

Burada f_s şebeke frekansı, p kutup **çifti** sayısı, n rotor hızıdır.

| Arıza | Akım spektrumundaki karakteristik frekans | Not |
|---|---|---|
| Kırık rotor çubuğu / uç halka | **f = (1 ± 2ks)·f_s**, k = 1, 2, 3… | (1−2s)f_s asimetrinin doğrudan izidir. (1+2s)f_s hız dalgalanmasından doğar, dolayısıyla eylemsizliğe bağlıdır |
| Karma eksantriklik, mekanik dengesizlik, hizasızlık | **f = f_s ± m·f_r**, m = 1, 2, 3… | Düşük frekanslı bileşenler |
| Statik ve dinamik eksantriklik (rotor oluk harmonikleri) | **f = f_s·[(kR ± n_d)(1 − s)/p ± ν]** | R rotor oluk sayısı; n_d = 0 statik, 1, 2… dinamik; ν = 1, 3, 5… Görünüp görünmemesi R–p kombinasyonuna bağlıdır |
| Rulman hasarı | **f = \|f_s ± m·f_v\|**, f_v ∈ {BPFO, BPFI, BSF, FTF} | f_v rulman geometrisinden hesaplanır ([02](02-ariza-turleri-ve-imzalari.md)). İz zayıftır |
| Stator sarımlar arası kısa devre | **f = f_s·[k ± n(1 − s)/p]**, k = 1, 3; n = 1, 2, …, 2p−1 (formül kısmen doğrulandı) | Kafesli motorda yeni frekans oluşmaz, mevcut bileşenler büyür. Pratikte **negatif bileşen akımı** ve Park vektörü (EPVA) daha güvenilir göstergelerdir |
| Yük tork salınımı | **f = f_s ± m·f_yük** | 2s·f_s yakınındaki salınımlar kırık çubukla karışabilir |
| PMSM kısmi demanyetizasyon / kırık mıknatıs / dinamik eksantriklik | **f = f_s·(1 ± k/p)** | Senkron makinede s = 0. **Düzgün** demanyetizasyon yeni çizgi üretmez |

> Formüllerin kaynakları, değişken tanımları ve uyarılar için bkz. [02-ariza-turleri-ve-imzalari.md](02-ariza-turleri-ve-imzalari.md).

**Çözümlü örnek (Aşama 2 alıştırması).** IEEE DataPort kırık çubuk veri setindeki motoru ele alalım ([05 §5.1](05-veri-setleri-turkce-kaynaklar-egitimler.md)): 4 kutup (p = 2), 60 Hz, tam yükte 1715 d/d, R = 34 çubuk.

| Adım | Hesap | Sonuç |
|---|---|---|
| Senkron hız | n_s = 60·60/2 | 1800 d/d |
| Kayma | s = (1800 − 1715)/1800 | 0,0472 |
| Kırık çubuk yan bantları | (1 ± 2s)·60 | **54,33 Hz** ve **65,67 Hz** (temel bileşenden ±5,67 Hz) |
| Rotor dönme frekansı | f_r = 1715/60 | 28,58 Hz |
| Eksantriklik ve dengesizlik bileşenleri | 60 ± 28,58 | **31,42 Hz** ve **88,58 Hz** |
| Temel oluk harmonikleri | 60·[34·(1 − 0,0472)/2 ± 1] | yaklaşık **911,8 Hz** ve **1031,8 Hz** |

Bu değerler **tam yük** içindir. Kısmi yüklerde kayma küçülür ve yan bantlar 60 Hz'e yaklaşır. Kaymayı her kayıt için ayrıca ölçün ya da kestirin.

---

## 3. Yol haritası: aşamalar

| Aşama | Önerilen süre | Hedef | Ayrıntı |
|---|---|---|---|
| **0. Ön koşullar** | 1–2 hafta | Asenkron makine temelleri, FFT ve örnekleme, MATLAB/Simulink'e giriş | aşağıda |
| **1. MCSA'yı anlamak** | 2–3 hafta | Temel eğitici makaleler ve derlemeler | [01](01-temeller-ve-okuma-listesi.md) |
| **2. Arıza fiziği ve imzaları** | 2 hafta | Her arızanın mekanizması ve formülü | [02](02-ariza-turleri-ve-imzalari.md) |
| **3. Sinyal işleme** | 2–4 hafta (Aşama 4 ile paralel yürür) | FFT'den ileri yöntemlere ve makine öğrenmesine | [03](03-sinyal-isleme-ve-makine-ogrenmesi.md) |
| **4. MATLAB/Simulink modelleme** | 6–8 hafta | Sağlam model, ardından arızalı modeller ve simüle akımda MCSA | [04](04-matlab-simulink-modelleme.md) |
| **5. Gerçek veriyle doğrulama** | 2 hafta | Simülasyon sonuçlarını açık veri setleriyle karşılaştırmak | [05](05-veri-setleri-turkce-kaynaklar-egitimler.md) |
| **6. Kendi katkınız** | sürekli | Araştırma sorusunu belirlemek | §5 |

### Aşama 0: Ön koşullar

**Asenkron makine**
- Döner alan, kayma, eşdeğer devre, dq dönüşümü.
- Kaynaklar:
  - Chapman, *Elektrik Makinalarının Temelleri* (Türkçe çeviri)
  - [ODTÜ OCW EE362](https://ocw.metu.edu.tr/course/view.php?id=336) (Ozan Keysan)
  - Başoğlu ve Orhan'ın Türkçe ders videoları
  - [MIT OCW 6.685](https://ocw.mit.edu/courses/6-685-electric-machines-fall-2013/)

**Sinyal işleme**
- Örnekleme, örtüşme, FFT, pencereleme, çözünürlük.
- Kaynaklar:
  - [Signal Processing Onramp](https://matlabacademy.mathworks.com/details/signal-processing-onramp/signalprocessing)
  - MathWorks [Practical Introduction to Frequency-Domain Analysis](https://www.mathworks.com/help/signal/ug/practical-introduction-to-frequency-domain-analysis.html)
  - Heinzel vd. 2002 ([ücretsiz PDF](https://holometer.fnal.gov/GH_FFT.pdf))

**MATLAB/Simulink**
- [MATLAB Onramp](https://matlabacademy.mathworks.com/details/matlab-onramp/gettingstarted), ardından [Simulink Onramp](https://matlabacademy.mathworks.com/details/simulink-onramp/simulink), ardından [Simscape Onramp](https://matlabacademy.mathworks.com/details/simscape-onramp/simscape). Hepsi ücretsiz, her biri yaklaşık 2 saat.
- Emrah Zerdali'nin Türkçe [Simulink asenkron motor videoları](https://www.youtube.com/watch?v=f2XaBVDQH9U).

✔ **Kontrol noktası:** [`matlab/mcsa_ilk_adim.m`](matlab/mcsa_ilk_adim.m) betiğini çalıştırın ve sonundaki deneyleri yapın. Kaymayı, kayıt süresini ve pencereyi değiştirdiğinizde yan bantlara ne olduğunu kendi cümlelerinizle açıklayın.

### Aşama 1: MCSA'yı derinlemesine anlamak (çekirdek okuma listesi)

1. **Thomson & Gilmore (2003):** MCSA fundamentals, data interpretation, and industrial case histories. [Ücretsiz PDF](https://hdl.handle.net/1969.1/163283). **İlk okunacak kaynak.**
2. **Thomson & Fenger (2001):** Current signature analysis to detect induction motor faults. *IEEE IA Magazine*. [doi](https://doi.org/10.1109/2943.930988)
3. **Culbert & Letal (2015):** Signature analysis for on-line motor diagnostics. [Ücretsiz PDF](https://irispower.com/wp-content/uploads/2018/06/2015-PCIC-Signature-Analysis-For-On-Line-Motor-Diagnostics.pdf). Pratik dB eşikleri ve trend izleme.
4. **Benbouzid (2000):** A review of induction motors signature analysis… *IEEE TIE*. [doi](https://doi.org/10.1109/41.873206). Yanında Benbouzid & Kliman (2003), [HAL'da ücretsiz](https://hal.science/hal-01052444).
5. **Nandi, Toliyat & Li (2005):** Condition monitoring and fault diagnosis of electrical motors—a review. *IEEE TEC*. [doi](https://doi.org/10.1109/TEC.2005.847955)
6. **Henao vd. (2014)** ([ücretsiz kopya](http://hdl.handle.net/10251/98423)) ve **Riera-Guasp, Antonino-Daviu & Capolino (2015)** ([ücretsiz kopya](http://hdl.handle.net/10251/97806)): alanın güncel haritası.
7. **Halder vd. (2022),** *Energies* (açık erişim, [doi](https://doi.org/10.3390/en15228569)) ve **Niu, Dong & Chen (2023),** *IEEE TIM* ([doi](https://doi.org/10.1109/TIM.2023.3285999)): MCSA'ya odaklı güncel derlemeler.

**Kitaplar**
- Thomson & Culbert (2017), *Current Signature Analysis for Condition Monitoring of Cage Induction Motors*: MCSA uygulamasının temel kitabı.
- Toliyat vd. (2012), *Electric Machines: Modeling, Condition Monitoring, and Fault Diagnosis*: modelleme için en önemli kitap.

**Türkçe giriş:** Koca & Ünsal (2017), [DergiPark](https://dergipark.org.tr/tr/pub/tbed/article/300598).

✔ **Kontrol noktası:** MCSA'nın 1–2 sayfalık özetini kendi cümlelerinizle yazın. Özette ölçüm zinciri, dört ana arıza ve sınırlamalar yer alsın.

### Aşama 2: Arıza türleri ve imzaları

§2'deki formüllerin **fiziksel kökenini** öğrenin. Kaynaklar ve arıza başına temel makaleler: [02](02-ariza-turleri-ve-imzalari.md).

**Önce okuyun**
- **Bonet-Jara vd. (2021),** *Sensors* ([açık erişim](https://doi.org/10.3390/s21155037)): formüller, dB kriterleri, kayma hatasının neden yanlış alarm ürettiği; 79 endüstriyel motorda ticari cihazların analizi.
- Thomson & Culbert (2017), Bölüm 4.

**Ardından her arıza için bir temel makale**
- Kırık çubuk: Kliman 1988
- Eksantriklik: Nandi 2001
- Rulman: Schoen 1995 ve Blodt 2008 ([ücretsiz](https://hal.science/hal-00270747))
- Stator: Cardoso 1999 ([ücretsiz](https://estudogeral.uc.pt/bitstream/10316/12916/1/Inter-turn%20stator%20winding%20fault%20diagnosis.pdf))
- Sürücü etkisi: Bellini 2000

✔ **Kontrol noktası:** Bir motorun etiket değerlerinden (kutup sayısı, hız, çubuk sayısı, rulman geometrisi) tüm arıza frekanslarını hesaplayan küçük bir MATLAB fonksiyonu yazın. §2'deki çözümlü örnekle karşılaştırın.

### Aşama 3: Sinyal işleme

Önerilen sıra [03 §3.1](03-sinyal-isleme-ve-makine-ogrenmesi.md)'dedir. Kısaca:
1. FFT temelleri
2. `pwelch`, `pspectrum`, `faultBands`
3. Akımdan kayma kestirimi
4. Demodülasyon: Hilbert, Park vektörü, MSCSA
5. Zoom FFT, MUSIC ve ESPRIT
6. Geçici rejim: dalgacıklar
7. Rulman için zarf analizi ve spektral kurtosis
8. Makine öğrenmesi

✔ **Kontrol noktası:** IEEE DataPort veri setinden bir sağlam ve bir 4 kırık çubuklu kaydı alın. Kendi spektrum kodunuzla yan bantları bulun, sonra MathWorks'ün [kırık rotor örneğini](https://www.mathworks.com/help/predmaint/ug/broken-rotor-fault-detection-in-ac-induction-motors-using-vibration-and-electrical-signals.html) çalıştırıp sonuçları karşılaştırın.

### Aşama 4: MATLAB/Simulink'te modelleme (ana uygulama aşaması)

**Başlamadan önce bilinmesi gereken üç gerçek** (ayrıntı: [04 §4.0](04-matlab-simulink-modelleme.md)):
1. Klasik *Asynchronous Machine* bloğunun bulunduğu **Specialized Power Systems kütüphanesi R2026a'da kaldırıldı**. Eski makalelerin modellerini açmak için R2025b ya da dönüştürme gerekir.
2. Hazır asenkron motor ve PMSM bloklarında **iç arıza parametresi yoktur**. Kırık çubuk, eksantriklik ve sarım kısa devresi modellerini **denklemlerden kendiniz kurarsınız**. PMSM için MathWorks'ün *Model Faulted PMSM* örneği iyi bir başlangıçtır.
3. Simülasyonda sağlam motor spektrumu **gerçekte olduğundan çok temiz** çıkar (−160 dB'e karşı −63 dB). Tespit edilebilirliği yargılamadan önce modele doğal asimetri ve gürültü ekleyin.

**Adımlar**
| Adım | Ne yapılacak | Başlangıç kaynağı |
|---|---|---|
| 4.1 | Sağlam dq modelini kurun ve Simscape bloğuyla doğrulayın | Ozpineci & Tolbert 2003 ([ücretsiz PDF](https://scispace.com/pdf/simulink-implementation-of-induction-machine-model-a-modular-zaa86u43fw.pdf)); [FEX 79260](https://www.mathworks.com/matlabcentral/fileexchange/79260-implementation-of-induction-machine-model) |
| 4.2 | abc modelinde rotor fazlarından birinin direncini artırın; (1±2s)f yan bantlarını yük ve eylemsizliğe göre inceleyin | [FEX 42174](https://www.mathworks.com/matlabcentral/fileexchange/42174-modelling-of-induction-motor-in-a-b-c-variables); Filippetti 1998; Bellini 2001; Rahmatullah vd. 2023 (açık erişim) |
| 4.3 | Stator sarım kısa devresi: önce hazır modeli çalıştırın, sonra kendi modelinizi yazın | Sahin, Bayazit & Keysan 2020 ([GitHub'daki Simulink modeli](https://github.com/ilkersahin78/A-Simulink-Model-for-the-Induction-Machine-with-an-Inter-Turn-Short-Circuit-Fault)); Tallam 2002; Arkan 2005 |
| 4.4 | İleri düzey: çok bağlaşımlı devre modeliyle (MCCM) kırık çubuk ya da değiştirilmiş sargı fonksiyonuyla (MWFA) eksantriklik | Luo 1995; Toliyat & Lipo 1995; Pineda-Sanchez 2018 ve Martinez-Roman 2020 (açık erişim, motor verileri ekte) |
| 4.5 | Rulman: karakteristik frekansta yük torku salınımı ekleyin | Blodt 2008 ([HAL'da ücretsiz](https://hal.science/hal-00270747/document)) |
| 4.6 | Arıza şiddeti taraması ve veri seti üretimi | MathWorks [Use Simulink to Generate Fault Data](https://www.mathworks.com/help/predmaint/ug/Use-Simulink-to-Generate-Fault-Data.html) |

**Türkçe tezler (Simulink):** YÖK Tez No 232341, 292511, 668570, 718185 ([05 §5.2](05-veri-setleri-turkce-kaynaklar-egitimler.md)).

✔ **Kontrol noktası:** Simüle ettiğiniz arızalı akımın spektrumunda formülün öngördüğü frekanslarda tepeler görmelisiniz. Yan bant genliğinin arıza şiddeti ve yükle nasıl değiştiğini grafikle gösterin. Çözücü adımını yarıya indirdiğinizde sonucun değişmediğini kontrol edin.

### Aşama 5: Gerçek veriyle doğrulama

| Veri seti | İçerdiği arızalar |
|---|---|
| [IEEE DataPort kırık çubuk](https://ieee-dataport.org/open-access/experimental-database-detecting-and-diagnosing-rotor-broken-bar-three-phase-induction) | Kırık çubuk; 50 kHz akım |
| [Paderborn](https://mb.uni-paderborn.de/kat/forschung/bearing-datacenter/data-sets-and-download) | Rulman; 64 kHz akım |
| [KAIST asenkron motor](https://data.mendeley.com/datasets/ztmf3m7h5x/6) | Rulman, hizasızlık, dengesizlik |
| [KAIST PMSM](https://data.mendeley.com/datasets/rgn5brrgrn/5) | Sarım kısa devresi |
| [NLN-EMP pompa](https://data.4tu.nl/datasets/2b61183e-c14f-4131-829b-cc4822c369d0) | 11 arıza türü; inverterle beslenen motor |

Tam liste için bkz. [05 §5.1](05-veri-setleri-turkce-kaynaklar-egitimler.md).

✔ **Kontrol noktası:** Simülasyondaki ve ölçümdeki yan bant genliklerini aynı yük seviyesinde karşılaştırın. Farkları (gürültü tabanı, doğal asimetri, doyma) tartışın.

---

## 4. Önerilen 16 haftalık takvim

| Hafta | Okuma | Uygulama | Çıktı |
|---|---|---|---|
| 1–2 | Aşama 0; Thomson & Gilmore | Onramp'ler; `mcsa_ilk_adim.m` | Deney notları |
| 3–4 | Thomson & Fenger, Benbouzid, Nandi; [02](02-ariza-turleri-ve-imzalari.md) | Arıza frekansı hesaplayıcı (MATLAB fonksiyonu) | 2 sayfalık MCSA özeti + hesaplayıcı |
| 5–6 | [03](03-sinyal-isleme-ve-makine-ogrenmesi.md) §3.2–3.3 | IEEE DataPort verisi; kendi spektrum kodunuz; MathWorks örneği | Sağlam ve arızalı spektrum karşılaştırması |
| 7–8 | Ozpineci & Tolbert; Krause (ilgili bölümler) | Sağlam dq modeli; Simscape ile doğrulama | Doğrulanmış sağlam model |
| 9–10 | Filippetti 1998; Bellini 2001 | abc modeli + rotor asimetrisi; yük ve eylemsizlik taraması | Yan bant–yük–şiddet grafikleri |
| 11–12 | Tallam 2002; Arkan 2005; Sahin 2020 | Sarım kısa devresi modeli; negatif bileşen akımı ve EPVA | Stator arızası sonuçları |
| 13–14 | Luo 1995 veya Faiz & Ojaghi 2009; Blodt 2008 | MCCM kırık çubuk **ya da** MWFA eksantriklik; rulman için tork salınımı | İleri model (birini seçin) |
| 15–16 | Aşama 6 kaynakları | Gerçek veriyle doğrulama; araştırma sorusunun seçimi | Ara rapor ve tez/makale planı |

---

## 5. Araştırma fikirleri (Aşama 6)

1. **Hafif yükte (düşük kaymada) teşhis.** FFT, Hilbert, MUSIC/ESPRIT ve MSCSA'yı simüle veride ve IEEE DataPort'un %12,5 yük kayıtlarında karşılaştırmak.
   - Kaynaklar: Puche-Panadero 2009, Xu 2013, Kia 2007, Pires 2013.
2. **Kırık çubuk ile düşük frekanslı yük salınımını ayırt etmek.**
   - Kaynaklar: Göktaş (2015) doktora tezi (YÖK 424287); Göktaş, Arkan & Özgüven 2015.
3. **İnverterle beslenen ve kapalı çevrim kontrollü motorlarda MCSA.**
   - Kaynaklar: Akın vd. 2008; Fernández-Cavero 2017; NLN-EMP veri seti.
4. **Kalkış (geçici rejim) MCSA'sı**, dalgacık dönüşümleriyle.
   - Kaynaklar: Antonino-Daviu 2006 ve 2020; Riera-Guasp 2008; Zenodo kalkış akımı veri seti.
5. **Simülasyondan gerçeğe aktarım.** Simulink/FEM ile üretilmiş etiketli akım verisiyle eğitilen sınıflandırıcının gerçek veride başarımı.
   - Kaynaklar: Ji vd. 2025; Ali vd. 2026. Barrera-Llanga 2023 ise yalnızca simüle veriyle test yapmanın tuzağını gösteren uyarıcı bir örnek.
   - MathWorks'te simüle edilmiş asenkron motor arızası için resmî bir örnek bulunamadı. Bu boşluk bir katkı fırsatı olabilir.
6. **PMSM arızaları** (elektrikli araç motorları): demanyetizasyon, eksantriklik ve sarım kısa devresini birbirinden ayırt etmek.
   - Kaynaklar: Göktaş, Zafarani & Akın 2016; MathWorks *Model Faulted PMSM*; KAIST PMSM veri seti.
7. **Birleşik (çoklu) arızalar.**
   - Kaynaklar: García-Pérez 2011; NLN-EMP veri seti.

---

## 6. Bu hafta başlamak için üç adım

1. [Thomson & Gilmore (2003)](https://hdl.handle.net/1969.1/163283) makalesini okuyun. Ücretsizdir ve yaklaşık 12 sayfadır.
2. [MATLAB Onramp](https://matlabacademy.mathworks.com/details/matlab-onramp/gettingstarted) ve [Signal Processing Onramp](https://matlabacademy.mathworks.com/details/signal-processing-onramp/signalprocessing) kurslarını bitirin.
3. [`matlab/mcsa_ilk_adim.m`](matlab/mcsa_ilk_adim.m) betiğini çalıştırın ve deneylerini yapın.
