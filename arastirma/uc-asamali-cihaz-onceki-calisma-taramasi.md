# Üç aşamalı (arıza teşhisi → kestirimci bakım → hata toleranslı kontrol) gömülü cihaz fikri için önceki çalışma, patent ve ticari ürün taraması

Tarih: 13 Ekim 2026
Hazırlayan: Claude (web tabanlı araştırma; hukuki bir patent/FTO görüşü değildir)

---

## 1. Kısa cevap

**Aradığınız biçimde bir ürün veya patent bulunamadı.** Yani: tek bir gömülü gerçek zamanlı kontrolcü (Raspberry Pi sınıfı) üzerinde, makineden bağımsız biçimde, (1) tüm açık veri setleriyle eğitilmiş ML ile olası tüm arızaları teşhis eden, (2) arızayı oluşmadan kestiren ve (3) arıza tipine göre uygun hata toleranslı kontrol stratejisini otomatik seçip uygulayan bir ticari ürün, açık kaynak sistem ya da patent istemi tespit edilemedi.

Ancak üç önemli uyarı var:

1. **Fikir yeni değil; parçaları ve hatta "üçlü entegrasyon" düşüncesi yaklaşık 25 yıldır var.** En yakın örnekler: Rockwell/Reliance Electric'in 1999 öncelikli ve artık süresi dolmuş patent ailesi (motora gömülü teşhis + arıza zamanı tahmini + kontrol yasasını değiştirme), NASA/Impact Technologies/Georgia Tech'in 2007–2011 "prognostics-enhanced automated contingency management" çalışmaları (simülasyon), Xerox/PARC'ın hâlâ yürürlükte olan US11402833B2 patenti (kalan ömre göre otomatik güvenli mod / kontrolcü uyarlama / yeniden yapılandırma) ve 2023–2026 arasında Çin'den gelen dijital ikiz tabanlı başvurular (asansör invertörü, maglev çekiş sistemi, İHA, uçak eyleyicisi).
2. **Her aşama tek başına çok kalabalık.** Aşama 1–2 (titreşim/akım tabanlı teşhis + kalan ömür) onlarca ticari ürün ve yüzlerce patentle dolu; Aşama 3 (hata toleranslı kontrol) havacılık, sürücüler ve İHA'larda sertifikalı ürünlerde zaten var. Fakat ticari dünyada bu iki dünya kasıtlı olarak ayrı tutuluyor: kestirimci bakım ürünleri **uyarı/iş emri** ile biter, kontrolcüye otomatik müdahale etmez.
3. **"Olası tüm arızaları teşhis eder" iddiasının hiçbir emsali yoktur ve mevcut açık veri korpusu bunu desteklemez.** Açık veri setleri ağırlıkla rulman/dişli titreşimi; motor elektrik arızaları, hidrolik, pompa, proses arızaları çok seyrek. 2024–2026'da yayımlanan "temel model" (foundation model) çalışmaları bile yalnızca titreşim ve rulman/dişli odaklı.

Dolayısıyla yeniliğiniz, aşamaların tek tek varlığında değil, **(a) genel amaçlı ve düşük maliyetli tek bir gerçek zamanlı kontrolcüde üçünün entegrasyonunda, (b) teşhis edilen arıza sınıfı + kalan ömür bilgisine göre bir FTC strateji kütüphanesinden otomatik seçim yapan mekanizmada ve (c) çok veri setli (foundation) teşhis modelinin kestirim ve kontrol katmanlarına bağlanmasında** olabilir. Bunların her biri için patentlenebilirlik, somut teknik araçların istemlenmesine bağlıdır; "üç aşamalı yol haritası" tek başına patentlenemez, çünkü literatürde standart PHM olgunluk modelidir.

---

## 2. Yöntem ve sınırlar

- **Tarama:** 10 paralel araştırma açısı (patentler ×2, ticari kestirimci bakım ürünleri, sürücü/robot/havacılık/otomotiv ürünleri, akademik bütünleşik çerçeveler, evrensel teşhis modelleri ve açık veri setleri, Raspberry Pi/kenar uygulamaları, standartlar ve kamu programları, start-up'lar, Türkiye/Finlandiya/AB). 341 aday kayıt toplandı.
- **Doğrulama:** Çok aşamalı görünen en yakın 36 aday, birincil kaynaktan (Google Patents istem metni, USPTO PDF, makale özeti, üretici sayfası) **çürütme amaçlı** ikinci bir inceleme ile doğrulandı. Bu incelemede araştırmacı ajanların abartılı sınıflamaları düzeltildi; aşağıdaki tablolar düzeltilmiş değerlendirmeyi yansıtır.
- **Ek patent sorguları:** Google Patents'in JSON uç noktası üzerinden İngilizce, Çince, Japonca ve Almanca anahtar kelimelerle 21 sorgu çalıştırıldı; bir kısmı Google'ın hız sınırına takıldı.
- **Sınırlar:** Bu bir web taramasıdır; profesyonel yenilik/FTO (freedom-to-operate) araştırmasının yerine geçmez. Espacenet, PATENTSCOPE ve TÜRKPATENT veri tabanları doğrudan sorgulanamadı (JavaScript/erişim kısıtı). Bazı üretici sayfaları (ABB, SKF, Schaeffler, Omron, Rockwell) erişilemediğinden ilgili bilgiler ikincil kaynaklara dayanır ve metinde belirtilmiştir.

---

## 3. En yakın önceki çalışmalar (doğrulanmış)

Puan: 10 = üç aşama tek gömülü gerçek zamanlı kontrolcüde, genel makine, çok veri setli ML; 8–9 = üç aşama tek alanda donanımda; 6–7 = üç aşama istemlenmiş/simüle edilmiş veya iki aşama uygulanmış; 4–5 = sıradan kestirimci bakım veya tespitli FTC; 1–3 = tek aşama.

### 3.1 Patentler

| Puan | Kimlik | Sahip / yıl | Hukuki durum | Kapsadığı aşamalar | Eksik olan |
|---|---|---|---|---|---|
| 6,5 | US6326758B1 (aile: US6646397B1, US7301296B2, US7538512B2) | Reliance Electric / Rockwell, Discenzo; öncelik 1999 | **Süresi doldu** (2019–2020) | Motora gömülü teşhis + sağlık değerlendirme, arıza zamanı ve nedeninin tahmini, kontrol sinyalini değiştirmeye karar verme (bağımsız istem 9 döngüyü otomatik kapatır) | Tek makine sınıfı (servo/asenkron motor); model tabanlı, ML/veri seti yok; prototip yok; FTC "yumuşak kontrol yasasına geçiş / kazanç değiştirme", arıza tipine göre strateji seçimi değil |
| 6,0 | CN120802909A | Xiangmai Intelligent Tech (Shaanxi), 2025 | **Beklemede** (inceleme 11/2025'te başladı) | Dijital ikiz ile asansör invertörü: arıza tipi teşhisi + IGBT kalan ömrü + otomatik hata toleranslı modülasyon/derating; bağımsız istemde üçü de var; kenar-bulut bölünmesi, yerel STM32H743 veya S7-1200 | Tek bileşen (7 önceden tanımlı arıza modu); açık veri seti yok; prototip yok |
| 6,0 | CN122450188A | Huai'an Üniversitesi, 2026 | **Beklemede** | İHA elektromekanik sistemleri: LSTM arıza tahmini/teşhisi + RUL, Pareto tabanlı hata toleranslı karar, sanal "dijital refakatçi" alt sistemle kontrol yasası yeniden yapılandırma | Yalnızca simülasyon; gömülü donanım yok; teşhis/kestirim yalnızca bağımlı istemlerde; endüstriyel makine değil |
| 5,0 | **US11402833B2** (JP7702337B2 de verildi; EP4006676A1 geri çekilmiş sayıldı) | PARC → Xerox, Kai Goebel; 2020/2022 | **Yürürlükte** (bakım ücreti 07/2026'da ödendi; ~2040'a kadar) | Varlıktan bağımsız: sağlık izleme → RUL → RUL görev süresinden kısaysa otomatik "fail-safe / kontrolcü uyarlama / yeniden yapılandırma / görev değiştirme" | Arıza tespiti yalnızca bağımlı istemlerde; arıza tipine göre değil RUL kademesine göre eylem; gömülü donanım yok; ML yok. **Aşama 2→3 mantığı için en kritik yürürlükteki patent** |
| 5,0 | US10146611B2 | Siemens, 2012/2018 | Yürürlükte (~2034) | Alt sistemlere yakın dağıtık kestirim motorları (SOM sağlık göstergesi, RUL) → yükü sağlıklı alt sistemlere kaydıran kontrol stratejisi | Arıza izolasyonu yok; sistem düzeyinde yük dağıtımı, makine düzeyinde FTC değil |
| 5,0 | US11133771B2 | GM, 2019/2021 | Yürürlükte (~2039) | Araç motor kontrolcüsünde SOH tabanlı arıza izolasyonu (resolver/akım sensörü/sargı) + tork düşürme | Kestirim eşik tabanlı; tek makine sınıfı; tek sabit eylem |
| 5,0 | US10591886B2 | Omron, 2016/2020 | Yürürlükte (~2038) | PLC'de ML eşiğiyle anormallik tespiti → yedek cihaza otomatik geçiş | "Kestirim" erken eşik; FTC yalnızca donanım yedeği anahtarlama |
| 5,0 | US8577509B2 | Vestas, 2009/2013 | **Düştü** (bakım ücreti ödenmedi, 11/2025) | Rüzgar türbini: arıza modu → kalan ömür → kontrol şeması (derating) seçimi | Kontrol adımı bağımlı istemde; CBO birimi veri merkezinde; manuel seçim de kapsanıyor |
| 5,0 | US8942882B2 | Boeing, öncelik 2004 | **Düştü** | IVHM "gatekeeper" mimarisi; açıklamada eyleyici arızası tahmini ve uçuş kontrol yeniden yapılandırması | Bağımsız istemler veri doğrulama mimarisini kapsıyor |
| 5,0 | US10423473B2 | UTC/RTX, 2017/2019 | Yürürlükte (~2037) | Gaz türbini: yerleşik eyleyici/sensör bozulma tespiti → MPC kısıt/ağırlık yeniden yapılandırma | RUL yok; ML yok; tek alan |
| 5,0 | US7536277B2 | Toyota/UConn, 2004/2009 | **Düştü** | ECU yerleşik teşhis ajanları + "sistem işleyişini doğrudan etkileyen" iyileştirici eylem | Kestirim ve limp-home yalnızca bağımlı istem/açıklamada |
| 4,0 | US6823675B2 | GE, 2002/2004 | **Süresi doldu** | Teşhis + "master mode selector" + yeniden yapılandırılabilir model tabanlı kontrol (gaz türbini) | Kestirim yok |
| 4,0 | US8612079B2 | GM, 2011/2013 | **Düştü** (12/2025) | SOH/SOF/RUL → en düşük maliyetli ömür uzatıcı stratejiyi seçip uygulama | Arıza teşhisi yok; sağlık-farkında kontrol |
| 4,0 | **US12504725B2** | GE, 2023; verildi 12/2025 | **Yürürlükte** (~2044) | Anormallik (ağırlıkla siber saldırı) tespit edilince çevrimdışı ayarlanmış kontrolcü kütüphanesinden otomatik kontrolcü değiştirme; "self-healing adaptive controller" | Kestirim yok; teşhis yöntemi istemde yok; gömülü değil. Yine de **anormallik → kontrolcü kütüphanesinden seçim** mantığı için FTO açısından dikkate alınmalı |
| 4,0 | US10048670B2 ailesi (Beet Inc.) | 2014/2018 | Yürürlükte | Fabrika düzeyi: çevrim süresi sapması → arıza tahmini → yedek eleman/üretim yönlendirme ("self-healing enterprise") | Makine kontrolü değil, üretim yönetimi |
| 4,0 | US6892317B1 / JP2001216423A | Xerox, 1999 | Süresi doldu | Yazıcı ağı: tahmin + teşhis + sunucu tetiklemeli otomatik yeniden kalibrasyon | Çevrimiçi FTC değil, uzaktan düzeltici bakım |
| 3,5 | US11193387B2 | GE, 2017/2021 | Yürürlükte (~2037) | FADEC'te ömür/hasar modelleri → "sağlık trimleri" ile eyleyici komutları | Arıza teşhisi yok; sağlık-farkında kontrol |
| 3,5 | US9134713B2 | Siemens, 2012/2015 | **Düştü** (2023) | MPC'de artık tabanlı arıza tespiti → ayar/model yeniden yapılandırma | RUL yok; otomatiklik zorunlu değil |
| 3,5 | US9221535B2 | Honeywell, 2013/2015 | **Düştü** (2023) | Çok motorlu sistemde RUL eşitleyen yük paylaşımı | Teşhis yok |
| 3,0 | US10626748B2 | GE, 2014/2020 | Yürürlükte (~2035) | Kalman tabanlı sürünme hasarı/RUL → set noktası | Teşhis yok |
| 3,0 | US10539932B2 | Intel, 2017/2020 | **Düştü** (2024) | Kenar cihazda titreşim enerjisi → sunucuya seçici yükleme; bağımlı istemde motor ayarı | Teşhis sunucuda; tek gösterge |
| 3,0 | US10378515B2 | Equinor, 2013/2019 | Yürürlükte (~2035) | Ana rulman yük profili kontrolü; açıklamada "beliren arızada otomatik derating" | Derating istemlenmemiş |
| 3,0 | US11808248B2 | Fischer Block, 2020/2023 | Yürürlükte (~2041) | Filo düzeyi sağlık indeksi → uyarı; bağımlı istemde isteğe bağlı çalışma noktası ayarı | Kestirim yok |

Ayrıca ilk taramada ve doğrudan sorgularda görülen, ikinci doğrulamadan geçmemiş fakat tema açısından anlamlı patentler:

- **Çin başvuruları/patentleri (2020–2026):** CN116594314A (Çin Bilimler Akademisi Elektrik Müh. Enst., 2023: dijital ikiz ile yüksek hızlı maglev çekiş sisteminde "sağlık izleme + arıza tahmini + uyarlamalı optimizasyon ve hata toleranslı kontrol" tek istem dizisinde), CN118732480A (Roket Kuvvetleri Müh. Üniv., 2024: dijital ikiz ile uçak eyleyicisi teşhis + durum tahmini + FTC), CN121484876A (Guizhou Power Grid, 2025: derin öğrenme teşhisi + şiddet değerlendirme + "öz-iyileşme" kontrolü, dağıtım şebekesi), CN113485304B (Beihang, verildi: derin öğrenme teşhisi + katmanlı FTC, uçak), CN118630268A (Dalian Teknoloji Üniv., 2024: PEMFC ömür tahmini → bozunma hızını izleyen kontrol), CN113075878A (Pekin Havacılık Otomatik Kontrol Enst., 2021: "arıza tahminine dayalı yedeklilik kontrolü"), CN112684345B (Zhejiang, 2020: PEMFC aktif FTC tabanlı sağlık kontrolü), CN102854874B (NUAA, 2012: çoklu gözlemci tabanlı teşhis + FTC cihazı). Ortak özellikleri: hepsi **belirli bir sisteme özel**, çoğu simülasyon, çoğu beklemede.
- **Yalnızca teşhis + FTC (kestirimsiz):** US7454255B1 (Scientific Systems), US8763950B2 (Bell Helicopter), WO2012118564A2 (Eaton), CN101995821B (Harbin), US7002318B1 (GM konum sensörü), CN108828944B (Shandong Üniv., PSO-SVM enkoder), US6140789A (Mitsubishi servo oto-düzeltme), US11203950B2 (RTX FADEC sensör telafisi), US6085127A (Aurora Flight Sciences).
- **Yalnızca kestirim → kontrol (teşhissiz, "ömür uzatıcı kontrol"):** US7203554B2 (UTC, MPC), US9569901B2 (Denso), US7581434B1 (Rockwell akıllı sıvı sensörü), US12282324B2 (JCI), CN104389685A/CN104564354A (NWPU uçak motoru), US8734105B2 (Vestas rulman tabanlı yük azaltma).
- **Yalnızca teşhis + kestirim (klasik PdM):** US11188065B2 (Nanoprecise), US7882394B2 (Brooks Automation, bir makinenin tüm arıza modlarını kendi kontrolcü hiyerarşisinde teşhis), EP2836881B1 (Siemens, PLC'ye gömülü kestirim), US11853047B2 (Augury, sınıflandırıcının sensör tipleri/filolar arası transferi), US8868985B2 (Siemens, kural üretimli sentetik arıza örnekleri), US7308385B2 (SmartSignal), US10580232B2 (GM), US5566092A (Caterpillar, 1993).

### 3.2 Akademik çalışmalar ve programlar

| Puan | Çalışma | Ne yapıyor | Eksik olan |
|---|---|---|---|
| 5,5 | Prognostics-enhanced Automated Contingency Management (ACM+P): Tang, Kacprzynski, Goebel, Saxena, Saha, Vachtsevanos, PHM 2008 (DOI 10.1109/PHM.2008.4711448); "Prognostics in the Control Loop" AAAI 2007; IEEE Aerospace 2010 | Teşhis + kestirim bilgisinin bileşen/sistem düzeyinde kontrol yeniden yapılandırma ve görev yeniden planlamayı sürdüğü hiyerarşik "proaktif FTC" mimarisi (NASA STTR) | 2008 makalesinde teşhis/kestirim **simüle edilmiş**; yalnızca masaüstü simülasyon (GTMax helikopter, EMA); patent bulunamadı |
| 5,5 | D. W. Brown, "A prognostic health management based framework for fault-tolerant control", Georgia Tech doktora tezi, 2011 (+ PHM Society 2009 EMA makalesi) | RUL/TTF tahminine göre kontrol otoritesini yeniden yapılandıran üç katmanlı mimari, kararlılık kanıtları | MATLAB/Simulink; tek arıza modu (sargı yalıtımı); donanım yok |
| 5,5 | GitHub "Fault-Finding-in-Inverters" (Amrita Müh. Fak. öğrencileri, 2026) | Tek MOSFET için kNN teşhis + erken uyarı + üstel RUL + uyarlamalı derating FTC zinciri | Simülasyon; 3 sınıf; eğitim modeli depoda yok |
| 5,0 | Vachtsevanos, Georgoulas, Nikolakopoulos, MED 2016 (DOI 10.1109/MED.2016.7536041) | "Condition monitoring → fault detected? → RUL + performans değerlendirici → reconfigurable control" akış şeması; üç katmanlı FTC hiyerarşisi | Yalnızca alt katman MPC derating simüle edildi; teşhis gösterilmedi |
| 4,0 | Sağlık-farkında kontrol hattı: Escobet/Puig/Nejjari (MED 2012), Salazar tezi (UPC/CRAN 2018), Karimi Pour & Puig (MED 2021); Cieslak, Gucik-Derigny, Chang (Bordeaux, 2020/21: FDI + anahtarlamalı FTC + kestirimsel karar) | Bileşen güvenilirliği/RUL'u MPC maliyetine koyarak bozunmayı yavaşlatma; bazı çalışmalar eyleyici arızasından sonra FTC ekler | Simülasyon; teşhis çoğunlukla "bilindiği varsayılır"; gerçek zamanlı donanım yok |
| 4,0 | fortiss RISE projesi (MST Kongress 2021; Infineon, BMW, Continental) | Çip üstü yorulma izleme → bulutta ML RUL → yazılımı sağlıklı işlemcilere taşıma (fail-operational EPS) | Makine FTC'si değil, işlemci düzeyi yeniden yapılandırma |
| 4,0 | Lipiec, Mrugalski, Witczak, Stetter, AMCS 2022 | Rulman bozunumu (PRONOSTIA verisi) → TTF → filo görev dengeleme | Makine düzeyinde kontrol yok; simülasyon |
| 3,0 | Troyes hattı (Langeron, Grall, Barros 2013–2017; Gong 2024), Calabria hattı (Tedesco, Casavola 2022–2025), Mrugalska & Stetter 2019 | RUL'a göre LQR ağırlığı yeniden ayarlama; bozunmaya göre kontrol tahsisi; SOH'a göre AGV görev dağıtımı | Teşhis yok; RUL çoğunlukla bilindiği varsayılıyor; simülasyon |
| — | NASA PCoE "Prognostics-enabled Decision Making" K11 gezgin testi (2011–2014) | Bulunan **tek donanım gösterimi**: teşhis + kestirim → otomatik rota yeniden planlama | Kontrol yasası yeniden yapılandırması değil, görev düzeyi karar |
| — | NASA IFCS (F-15, 2003–2005), NASA IRAC, ESA/ECSS FDIR, EU RECONFIGURE (FP7) | Gerçek uçuşta/uzayda teşhis → otomatik kontrol yeniden yapılandırma | Kestirim yok |
| — | EU projeleri SelSus (FP7, "self-healing production resources"), MANTIS, SERENA, PROPHESY, Z-BRE4K, UPTIME, AI-PROFICIENT, IMPROVE; Paderborn SFB 614 | Aşama 1–2 platformları; PROPHESY "bakım güdümlü gerçek zamanlı kontrol"ü gelecek zaman kipinde vaat etti; SFB 614 öz-iyileşen mekatronik yazılım | Hiçbiri doğrulanabilir biçimde döngüyü kontrolcüde kapatmadı |

**Akademik özet:** Aldrini vd. (J. Intell. Manuf. 2023) derlemesi "FDD ile öz-iyileşme/FTC'yi bir araya getiren modellerin eksikliğini" açıkça belirtiyor; Bougacha vd. (IJPHM 2020) kestirim güdümlü kontrol yeniden yapılandırmayı "kestirim sonrası karar verme"nin küçük bir alt kategorisi olarak listeliyor. NASA PCoE'nin kendi sayfası "yerel kestirim bilgisinin kontrolcü düzeyinde değişikliklere nasıl çevrileceğini" **açık araştırma sorusu** olarak listeliyor. Terminoloji tuzağı: literatürde "PFTC" çoğunlukla *pasif* FTC demektir; aradığınız kavram "health-aware control", "proactive FTC", "prognostics-enhanced reconfigurable control", "degradation-tolerant control", "RUL control" adlarıyla geçer.

---

## 4. Aşama aşama manzara

### 4.1 Aşama 1: Durum izleme ile arıza teşhisi

**Ticari ürünler (hepsi uyarı ile biter, hiçbiri kontrolcüye müdahale etmez):** SKF Enlight AI / IMx, Schaeffler OPTIME, Siemens Senseye ve SITRANS SCM IQ / SIPLUS CMS, ABB Ability Smart Sensor, Emerson AMS / PeakVue, Bently Nevada System 1, Honeywell Forge APM, AVEVA Predictive Analytics, Augury, Samotics SAM4, Nanoprecise, Fluke/Azima WATCHMAN, Tractian, Petasense, KCF, Artesis e-MCM, Ronds (Çin), Onepredict (Kore), Sensemore (Türkiye), Condence/Distence (Finlandiya), Amazon Monitron (bakım modunda) ve Lookout for Equipment (destek 10/2026'da bitiyor). En geniş arıza listesi iddiaları: Tractian (70–75+ arıza modu), Samotics (elektrik + mekanik + yük tarafı; sınıf başına "kanıtlı/gelişen/erken" olgunluk notu), Mitsubishi SCM (rulman, dengesizlik, hizasızlık, yağlama, kavitasyon, faz kaybı, rezonans). **Hiçbir satıcı "tüm arızaları" iddia etmiyor**; dürüst olanlar arıza başına olgunluk notu yayımlıyor ve CAT III/IV analistleri döngüde tutuyor.

**Gerçek zamanlı kontrolcü içinde ML:** Omron Sysmac AI Controller (NX7/NY5; PLC çevriminde Isolation Forest), Beckhoff TwinCAT TF3600 Condition Monitoring + TF3800 ML (gerçek zamanlı PLC'de ONNX çıkarımı), Weidmüller edgeML, Rockwell LogixAI/GuardianAI, Mitsubishi SCM, Danfoss VLT CBM (sürücü firmware'inde). Bunlar **platform**; tepkiyi entegratör programlar, kestirim motoru ve FTC kütüphanesi gelmez. Hedefinize en yakın "ticari zemin" bu gruptur.

**Evrensel / temel (foundation) teşhis modelleri (2024–2026):** Soru "birisi tüm açık veri setleriyle tek model eğitti mi?" ise cevap **evet, kısmen**:

| Model | Kurum | Eğitim verisi | Teşhis | RUL | Gömülü |
|---|---|---|---|---|---|
| UniFault (arXiv 2504.01373) | A*STAR / Maryland | ~11 açık rulman seti, 6,9 M örnek (IMS, Ottawa, CWRU, Paderborn, DIRG, XJTU-SY, MFPT, FEMTO, KAIST, HIT, Bosch CNC) | Evet | Hayır | "Lite" sürüm 823 K parametre (Pi'ye sığar, test edilmemiş) |
| VibFM (PHME 2026) | Stuttgart Üniv. | 16 açık set, ~400 saat | Evet | Hayır | Hayır |
| TSFM | Seoul Nat. Univ. / OnePredict | 17 titreşim seti | Evet (öznitelik çıkarıcı) | Hayır | TorchScript, SBC'de çalışabilir, test yok |
| BearLLM (AAAI 2025) | CAS Shenyang | 9 açık benchmark, tek ağırlık seti | Evet (+ metin raporu) | Hayır | Hayır (Qwen2-1.5B) |
| RmGPT (arXiv 2409.17604) | SJTU / PoliMi | ~5–7 set | Evet | **Evet** (XJTU-SY) | "Orin" gecikme sütunu var, ayrıntı yok |
| PHM-Vibench (PHMAP 2025) | Tsinghua | 20+ set, benchmark çerçevesi | Evet | Evet | Hayır |

Ortak sınırlar: yalnızca titreşim; rulman/dişli odaklı; motor akımı (MCSA), hidrolik, pompa, proses arızaları korpusta yok; makineler/çalışma koşulları arası dağılım kayması; veri setleri arası etiket uzayı uyumsuzluğu (her çalışma kendi etiketlerini yeniden tanımlıyor); ön eğitim/test sızıntısı riski (RmGPT CWRU'nun ön eğitim korpusunda olabileceğini kabul ediyor). Hiçbiri kontrol yapmıyor, hiçbiri gömülü kontrolcüde çalıştırılmadı.

**Türkiye ve Finlandiya'daki teşhis çalışmaları:** LUT'un 2005–2021 "sürücü tabanlı sensörsüz izleme" hattı (Ahola, Ahonen, Tamminen, Niemelä, Pöyhönen: kavitasyon, surge, çek valf, filtre kirlenmesi, hava kaçağı, başlangıç rulman hasarı; LUT profillerinde üç patent başlığı), LUT'un güncel ML/dijital ikiz teşhis çalışmaları (Sopanen, Lindh, Nevaranta; 2025–2026, açık erişimli AMB veri seti dahil), Aalto Elektromekanik grubu (sentetik + ölçülmüş veriyle motor arızası teşhisi; "eksik veriyi düzenekle tamamlama" fikrinize doğrudan ilgili), Sabancı (Ünel; Ford Otosan filo verisiyle anomali tespiti), İTÜ/ODTÜ (bu taramada doğrulanamadı).

### 4.2 Aşama 2: Kestirimci bakım / kalan ömür

- RUL iddiası olan ürünler: Senseye ("patent-pending" RUL), Azima WATCHMAN, AVEVA PA, Honeywell APM, Nanoprecise RotationLF, Sensemore (aylar öncesinden), Schaeffler OPTIME (haftalar), Samotics (5 aya kadar), ABB CBM for drives (1–2 yıl), Konecranes TRUCONNECT (kalan tasarım ömrü), Renesas Reality AI (bileşen RUL'u, MCU üzerinde). **Hepsi danışman niteliğinde**, çoğu bulut tarafında; hiçbirinin doğruluğu için bağımsız benchmark yayımlanmış değil.
- Sürücüye gömülü kestirim: Danfoss VLT CBM, Schneider Altivar Predict, Mitsubishi MR-J5 makine teşhisi, Rockwell PowerFlex 755T bileşen ömrü, Yaskawa GA700, Siemens Drivetrain Analyzer Edge, FANUC ZDT, KUKA iiQoT. Hiçbiri kestirim çıktısını kontrol yasasına bağlamıyor; Danfoss kırmızı alarm seviyesinde makineyi **durduruyor**.
- Açık kaynak: NASA ProgPy (model ve veri tabanlı kestirim çerçevesi; teşhis ve kontrol yok).
- Standartlar: ISO 13374 / MIMOSA OSA-CBM altı katmanı "advisory generation" ile biter; ISO 13381-1 (2025 revizyonu) yalnızca kestirim sürecini tanımlar; IEEE 1856, SAE JA6268, DoD CBM+ ve F-35 ALIS/ODIN da danışman/lojistik düzeyinde kalır.

### 4.3 Aşama 3: Hata toleranslı kontrol

**Ticari olarak var olan otomatik tepkiler (sabit kodlu, arıza başına, kestirimsiz):**

- Sürücüler: Siemens SINAMICS S120 p0491 (enkoder arızasında enkodersiz vektör kontrole otomatik geçiş), ABB ACS880 90.45/90.46 (geri besleme kaybında tahmini hızla sürmeye devam), 30.31 (düşük gerilimde tork azaltarak "ride-through"), Nidec Unidrive M (termal sınırda anahtarlama frekansını otomatik düşürme), ABB/Siemens termal modellerle derating.
- Otomotiv: Bosch iBooster + ESC fail-degraded fren, fail-operational EPS; FADEC sensör telafisi (RTX US11203950B2).
- İHA: PX4 Failure Detector + CA_FAILURE_MODE (motor arızasında kontrol tahsisinden çıkarma), ArduPilot EKF3 şerit değiştirme; TU Delft / TU Braunschweig / ETH rotor kaybı FTC'leri gerçek uçuşta.
- Takım tezgahı: Sandvik Coromant CoroPlus Process Control (takım kırılması/çarpışmada otomatik durdurma/ilerleme ayarı).
- Koruma sistemleri (API 670: Bently Orbit 60, B&K Compass 6000, SKF IMx röle çıkışları): fail-safe **trip**, hata toleranslı kontrol değil.

**Patentlerde FTC:** Çoğu tek arıza tipi ve model/gözlemci tabanlı; ML teşhisine göre bir **strateji kütüphanesinden seçim** yapan istem bulunamadı (en yakın: GE US12504725B2'nin anormallik bölgesine göre kontrolcü kütüphanesinden seçim; Çin İHA başvurusunun Pareto optimizasyonu; Rockwell 1999'un kontrol parametresi uyarlaması).

**Neden ticari dünyada birleşmiyor?** Üretici sayfalarında bu açıkça görülüyor: Samotics "bakım tepkisine sizin ekibiniz karar verir", AVEVA kullanıcının "acil durdurmayı başlatıp başlatmayacağına" karar vermesini bekliyor, Augury/Infinite Uptime "kararları fabrika ekibinden almayız" diyor. Sebep teknoloji eksikliği değil, **işlevsel güvenlik ve sorumluluk**: otomatik kontrol yeniden yapılandırması deterministik, doğrulanabilir ve sertifikalanabilir olmalı (IEC 61508 / ISO 13849; IEC 61800-5-1 otomatik yeniden başlatmada "BU MAKİNE OTOMATİK BAŞLAR" etiketi istiyor), ML teşhisi ise olasılıksal. Bu boşluk hem fırsatınız hem de en büyük engelinizdir.

### 4.4 Gömülü platform ve Raspberry Pi

- **Raspberry Pi tabanlı ticari bir durum izleme/kestirim/FTC ürünü bulunamadı.** Pi tabanlı endüstriyel platformlar var (KUNBUS Revolution Pi: Compute Module, EN 61131-2 soft PLC; Brainboxes BB-400: CM3+ + Arduino; Monarco HAT + REXYGEN; CODESYS Control for Raspberry Pi — lisansı "özel kullanım, test ve eğitim" ile sınırlı; LinuxCNC Pi 4/5 imajı), fakat hiçbiri teşhis/kestirim/FTC taşımıyor.
- Açık kaynak Pi projeleri (CWRU TFLite sınıflandırıcı Pi 4'te <50 ms; MCSA LSTM-AE Pi 5'te; ESP32 + Pi dijital ikiz) yalnızca sınıflandırma/anomali puanı; en fazla röle ile koruyucu durdurma.
- **Gerçek zamanlılık:** Resmî Raspberry Pi çekirdeği PREEMPT_RT paketi sunmuyor (topluluk derlemeleri var; PREEMPT_RT Linux 6.12 ile ana hatta girdi). LinuxCNC makine kontrolü için RT çekirdek şart diyor ve Pi 3 ve öncesini önermiyor. Ciddi her gömülü örnek **hibrit mimari** kullanıyor: Linux SBC analitik için + mikrodenetleyici sert gerçek zamanlı G/Ç ve kontrol için (Pixhawk: STM32H7 + STM32F100; BB-400: CM3+ + Arduino; RP2350/Pico 2 doğal eş işlemci). Öneri: Aşama 1–2 Pi 4/5/CM5'te, Aşama 3 kontrol döngüsü RT çekirdekli Pi'de (ms sınıfı döngüler) veya güvenlik için RP2350/STM32 eş işlemcisinde ya da sertifikalı PLC/sürücüde.
- TinyML araç zincirleri (ST NanoEdge AI Studio, Edge Impulse — Pi 4/5 tam destekli, Renesas Reality AI — RUL iddiası, SensiML, Infineon DEEPCRAFT, NXP eIQ, TDK SensEI) Aşama 1'i ucuza prototiplemeyi sağlar, Aşama 2–3 için bir şey sunmaz.

### 4.5 Bölgesel durum (Türkiye, Finlandiya, AB)

- **Türkiye:** Doğrulanabilen tek ticari oyuncu Sensemore (bulut tabanlı titreşim izleme, RUL iddiası; kontrol müdahalesi yok); Artesis e-MCM (model tabanlı motor izleme). Akademide Sabancı (Ünel: simülasyonda quadrotor FTC; Ford Otosan ile filo anomali tespiti; birbirinden ayrı çalışmalar, entegrasyon yok). TÜRKPATENT ve TÜBİTAK kayıtları bu taramada doğrudan sorgulanamadı; ek tarama sonuçları Bölüm 9'da güncellenecektir.
- **Finlandiya / LUT:** LUT'un kendi önceki çalışmaları Aşama 1'i (sürücü tabanlı sensörsüz izleme, dijital ikiz/ML teşhis) yoğun biçimde, Aşama 2'yi kısmen (başlangıç rulman hasarı izleme 2014/2016, filtre değişim zamanı optimizasyonu 2021, güç yarı iletkeni ömür kestirimi 2014) kapsıyor; Aşama 3 yalnızca tekil çalışmalarda var ("Optimal control of powertrain and energy balance to recover an equipment fault on a marine vessel", 2021, O. Pyrhönen, Lindh, Peltoniemi vd.; J. Pyrhönen/Niemelä'nın hata toleranslı modüler statorlu PM makine tasarımları; AMB/yataksız kontrol). LUT laboratuvar sayfaları "hata toleranslı kontrol" veya "bütünleşik teşhis-kestirim-FTC"yi tema olarak listelemiyor: fikir LUT içinde yeni görünüyor ama mevcut LUT teşhis IP'siyle örtüşüyor (ortak buluş/IP sahipliği konusunu erken netleştirin). Finlandiya sanayii (ABB Drives Helsinki, Danfoss Vaasa, Wärtsilä Expert Insight, Konecranes TRUCONNECT, KONE 24/7, Valmet, Metso, Nome, Condence, VTT Smart Predictive Maintenance) tamamen Aşama 1–2 ve danışman niteliğinde.
- **AB:** Yukarıdaki EU projeleri; Nordik FTC teorisi (DTU Blanke, Aalborg Odgaard/Stoustrup rüzgar türbini FDI/FTC benchmark'ı, Linköping Fault Diagnosis Toolbox — Pi sınıfı hedefe C kodu üretebilen model tabanlı teşhis aracı) güçlü ama kestirimsiz.

---

## 5. Yenilik boşlukları (fikrinizin nerede "yeni" görünebileceği)

1. **Genel amaçlı entegrasyon:** Üç aşamayı makineden bağımsız biçimde tek bir düşük maliyetli gerçek zamanlı kontrolcüde birleştiren ürün yok; patentler alana özel (motor 1999, asansör invertörü, İHA, maglev, rüzgar, gaz türbini) veya yalnızca karar mantığı (Xerox).
2. **Arıza sınıfı + RUL → FTC strateji seçimi:** "Teşhis edilen arıza tipine ve kalan ömre göre bir FTC strateji kütüphanesinden (sensörsüz geçiş, derating, eyleyici yeniden tahsisi, güvenli durdurma vb.) otomatik seçim ve geçiş" istemine rastlanmadı. Xerox patenti RUL kademesine göre, GE 2025 patenti anormallik bölgesine göre seçim yapıyor; ikisi de arıza tipine göre değil.
3. **Çok veri setli teşhis modelinin kestirim ve kontrole bağlanması:** Foundation modeller (UniFault, VibFM, BearLLM, RmGPT) teşhiste kalıyor; hiçbiri gömülü kontrolcüde çalıştırılmadı ve kontrol katmanına bağlanmadı.
4. **Kendi düzeneklerinizle "veri boşluğu doldurma":** Aalto (sentetik + ölçüm) ve Siemens US8868985B2 (sentetik arıza örnekleri) benzer fikirleri var; ancak "açık korpusta olmayan arıza modları için amaca özel düzenekle veri üretip aynı modele ekleme" sistematik bir yöntem olarak patentlerde görülmedi (bu tek başına patentlenebilir olmayabilir; eğitim verisinin genişliği inceleme uzmanlarınca istem sınırlaması sayılmaz).

---

## 6. Riskler ve uyarılar

**Teknik**

- "Olası tüm arızaları teşhis" iddiası savunulamaz; hiçbir ürün, program veya standart bunu iddia etmiyor. Bunun yerine ISO 17359 / FMECA ile makine sınıfı başına **sınırlı bir arıza taksonomisi** tanımlayıp, açık veri + kendi düzeneğinizle kapsanan modları ve "bilinmeyen/anomali" sınıfını açıkça belirtmek hem teknik hem IP açısından daha sağlam.
- Alan kayması: açık veri setleri küçük laboratuvar düzeneklerinden, tohumlanmış (EDM) arızalardan ve çoğunlukla rulman titreşiminden oluşuyor; çapraz makine genelleme literatürde hâlâ zayıf (HUST DG benchmark'ı bunu ölçüyor).
- Raspberry Pi'de sert gerçek zamanlı FTC: PREEMPT_RT veya eş işlemci şart; işlevsel güvenlik sertifikasyonu Pi üzerinde pratikte imkânsıza yakın; koruyucu trip katmanını (API 670 / ISO 20816 mantığı) ML'den bağımsız deterministik bir yolda tutun.
- Sağlık-farkında kontrolün literatürde raporlanan kazanımları mütevazı (EHA örneğinde %2,75–3,22 RUL); ürün vaadini buna göre kurun.

**Fikri mülkiyet (hukuki görüş değildir)**

- Yürürlükte ve en yakın: **Xerox US11402833B2** (RUL görev süresinden kısaysa otomatik iyileştirici eylem; varlıktan bağımsız; ~2040), **GE US12504725B2** (anormallik → kontrolcü kütüphanesinden otomatik geçiş; ~2044), Siemens US10146611B2 (kestirim → yük yeniden dağıtımı; ~2034), GM US11133771B2 (motor kontrolcüsünde arıza izolasyonu + tork düşürme; ~2039), Omron US10591886B2 (ML anormallik → yedek anahtarlama; ~2038), RTX US10423473B2, GE US11193387B2, Augury US11853047B2 (sınıflandırıcı transferi), Equinor US10378515B2, Fischer Block US11808248B2 ve beklemedeki Çin başvuruları (CN120802909A, CN122450188A, CN116594314A vb.). Bunlar için profesyonel FTO incelemesi gerekir.
- Süresi dolmuş/düşmüş ve dolayısıyla **serbestçe kullanılabilir fakat yeniliğinizi sınırlayan** önceki teknik: Rockwell US6326758B1 ailesi, GE US6823675B2, GM US8612079B2, Vestas US8577509B2, Boeing US8942882B2, Toyota/UConn US7536277B2, Siemens US9134713B2, Honeywell US9221535B2, Intel US10539932B2, Xerox US6892317B1.
- "Teşhis → kestirim → kestirimin kontrol döngüsüne alınması" yol haritası 2007'den beri (NASA/Impact "Prognostics in the Control Loop") standart PHM olgunluk modelidir; patent başvurusu yol haritasına değil **yönteme** (strateji seçim politikası, belirsizlik kapılama, hibrit RT mimari, taksonomi eşleme vb.) dayanmalıdır.

---

## 7. Aşama 1 için açık erişimli veri seti kataloğu

Hazır kataloglar (en güncelden eskiye): VictorBauler/awesome-bearing-dataset (94 set, DOI'lerle), CHAOZHAO-1/Machine-Fault-Dataset (30+ kategori: rulman, dişli, pompa, motor, batarya, İHA), hustcxl/Rotating-machine-fault-data-set (20 set), PHM-Vibench (20+ set, birleşik protokoller), UniFault Tablo 1, VibFM README, Zhao vd. DL-based-Intelligent-Diagnosis-Benchmark / UDTL (7 setin birleşik yükleyicileri), PyPHM, NASA PCoE listesi.

| Veri seti | Makine / bileşen | Arıza tipleri | Not |
|---|---|---|---|
| CWRU | 2 hp motor rulmanı | İç/dış bilezik, bilye (EDM) | Kanonik benchmark; çoğu foundation modelde holdout |
| Paderborn (KAt) | 425 W PMSM rulmanı | Yapay + gerçek hızlandırılmış hasar; titreşim + motor akımı 64 kHz | Ticari kullanım izne tabi |
| MFPT | Rulman | İç/dış bilezik, yük değişimli + 3 gerçek makine | ASNT'ye taşındı; GitHub (MathWorks) aynası |
| IMS (NASA PCoE) | Rulman, run-to-failure | İç bilezik, makara, dış bilezik | Kestirim benchmark'ı |
| XJTU-SY | Rulman, hızlandırılmış ömür | İç/dış bilezik aşınma, kafes kırılması | RUL benchmark'ı |
| FEMTO / PRONOSTIA (PHM 2012) | Rulman, run-to-failure | 17 rulman, 3 koşul | NASA PCoE aynası |
| JNU | Rulman | İç/dış/makara çentik | Lisans belirsiz |
| SEU | Dişli kutusu + rulman | Kırık/eksik diş, çatlak, aşınma; bilye/iç/dış | 8 kanal |
| HUST (Huazhong) | Rulman, dişli, motor (titreşim+ses), aktarma | 9 sağlık durumu × 11 koşul | RESS 2024 |
| HUST (Hanoi) | 5 rulman tipi | 6 arıza sınıfı, bileşik dahil | CC BY 4.0 |
| Ottawa 2018 / UORED-VAFCLS 2023 | Rulman | Değişken hız; iç/dış/bilye/kafes, mikrofon | CC BY 4.0 |
| MaFaulDa | SpectraQuest MFS | **Dengesizlik, hizasızlık**, rulman | Mil düzeyi arızalar için değerli |
| KAIST | Döner makine, çok modlu | İç/dış bilezik, hizasızlık, dengesizlik; titreşim + ses + sıcaklık + **3 faz akım** | + run-to-failure seti |
| USP/UNIOESTE broken rotor bar | 1 hp asenkron motor | 1–4 kırık çubuk; akım + gerilim + titreşim | IEEE DataPort (giriş gerekir) |
| ZeMA hidrolik (UCI #447) | Hidrolik test düzeneği | Soğutucu, valf, pompa iç kaçak, akümülatör | Hidrolik arızalar için tek yaygın set |
| MIMII / DCASE Task 2 | Valf, pompa, fan, ray (ses) | Kontaminasyon, kaçak, dengesizlik | 100 GB, CC BY-SA |
| MCC5-THU | Dişli kutusu, 12 değişken koşul | Pitting, aşınma, diş kırılması, çatlak | Data in Brief 2024 |
| DIRG (PoliTo) | Yüksek hızlı havacılık rulmanı | Çentik, değişken hız/yük + 230 saat dayanım | Zenodo 3559553 |
| UoC | İki kademeli dişli kutusu | 9 pinyon durumu | Figshare |
| NASA PCoE deposu | C-MAPSS/N-CMAPSS turbofan, freze, CNC, batarya, güç elektroniği | Run-to-failure | 21 set; bazıları geçici olarak indirilemiyor |
| PHM Society Data Challenges 2008–2026 | Dişli, helikopter, bilyalı vida vb. | Yıl bazında değişir | data.phmsociety.org |
| CARE / Kelmarsh / Penmanshiel / NREL | Rüzgar türbini SCADA, saha verisi | Jeneratör, dişli kutusu, ana rulman öncesi anomaliler | CC BY-SA |
| Bosch CNC Machining | 3 CNC, 15 operasyon | İyi/kötü etiketli titreşim | Gerçek saha, makineler arası kayma |
| Tennessee Eastman | Kimyasal proses (simülasyon) | 20 arıza | Döner makine dışı |

Gözlem: korpus büyük ölçüde rulman titreşimi; doğal bozunumlu run-to-failure setleri az; motor akımlı çok sensörlü setler nadir (Paderborn, KAIST, USP); gerçek saha verisi ağırlıkla rüzgar türbini ve CNC. Pompa, kompresör, hidrolik, elektriksel (stator/rotor) ve proses arızaları için kendi düzenekleriniz zorunlu görünüyor; bu, önerinizdeki "eksik eğitimler için düzenek kurma" adımını haklı çıkarıyor.

---

## 8. Önerilen sonraki adımlar

1. **Profesyonel yenilik ve FTO araştırması** (patent vekili): Espacenet, PATENTSCOPE, TÜRKPATENT; CPC sınıfları G05B23/0283 (kestirimci bakım/RUL), G05B23/0275 (arıza izolasyonu), G05B23/0289 (başlangıç arızaları), G05B9/02, G05B13/02–13/04 (uyarlamalı kontrol), G01M13/04–13/045 (rulman testi), G06N3/08; anahtar kelimeler: "reconfigurable control", "controller adaptation", "health trims", "countermeasure", "standby device", "degraded mode", "life extending control", "health-aware", 容错控制, 故障预测, 自愈控制, Rekonfiguration, Restlebensdauer, "hata toleranslı kontrol", "kestirimci bakım".
2. **İstemleri yönteme odaklayın:** arıza sınıfı × şiddet × RUL → strateji kütüphanesi eşlemesi; teşhis belirsizliğine göre kapılama (yanlış pozitifte güvenli davranış); Linux SBC + RT mikrodenetleyici + bağımsız koruma rölesi hibrit mimarisi; çapraz veri seti taksonomi eşleme ve düzenek verisiyle ince ayar yöntemi.
3. **Kapsamı dürüstçe sınırlayın:** "tüm arızalar" yerine makine sınıfı başına FMECA tabanlı arıza listesi + açık "bilinmeyen" sınıfı; PHM-Vibench ve HUST DG benchmark'ı ile çapraz makine performansını raporlayın.
4. **LUT IP durumu:** LUT'un sürücü tabanlı izleme patentleri ve güncel dijital ikiz çalışmalarıyla örtüşmeyi ve buluş sahipliğini LUT teknoloji transfer birimiyle erken netleştirin.
5. **Tasarımda güvenlik ayrımı:** ML teşhisi yalnızca "yumuşak" FTC (derating, sensörsüz geçiş, yük yeniden tahsisi) tetiklesin; sert koruma deterministik eşiklerle ayrı kanalda kalsın (ticari ürünlerin bugün yaptığı ayrımı kasten koruyun).
6. **Savunma amaçlı yayın** alternatifini değerlendirin: entegrasyon mimarisi patentlenemezse, hakemli yayın + açık kaynak sürümü başkalarının aynı entegrasyonu patentlemesini engeller.

---

## 9. Ek tarama sonuçları (Türkiye/Finlandiya patent ofisleri, start-up'lar, Raspberry Pi ürünleri, Çin/Japon/Kore patentleri)

Bu bölüm, oturum limitine takılan dört ek tarama ajanının sonuçları geldikçe güncellenecektir.

---

## Ek A. Taramada kullanılan başlıca birincil kaynaklar

- Google Patents sayfaları (patents.google.com/patent/<numara>/en), USPTO ppubs PDF'leri, patentimages PDF'leri (istem metinleri doğrudan okundu).
- NASA DASHlink: "Prognostics in the Control Loop" (AAAI 2007), "Prognostics-enhanced ACM for Advanced Autonomous Systems" (PHM 2008); NASA PCoE sayfası ve veri deposu; NASA ProgPy GitHub.
- PHM Society makaleleri 1635 (Brown vd. 2009), 1870 (Bole vd. 2010), 4303 (PHM-Vibench), 4912 (VibFM); arXiv 2504.01373 (UniFault), 2409.17604 (RmGPT), 2408.11281 (BearLLM), 2412.01218 (FD-LLM), 2502.15481 (FaultGPT).
- Üretici belgeleri: ABB ACS880 firmware kılavuzu, Siemens SINAMICS p0491 parametre listesi/forum, Danfoss VLT CBM uygulama notu, Nidec Unidrive M broşürü, Beckhoff TF3600/TF3800, Edge Impulse Pi 4/5 dokümanı, Revolution Pi, Monarco, CODESYS mağazası, LinuxCNC indirme sayfası, PX4 ve ArduPilot dokümanları.
- CORDIS proje raporları: SelSus 609382, MANTIS 662189, SERENA 767561, PROPHESY 766994, Z-BRE4K 768869, UPTIME 768634, AI-PROFICIENT 957391, IMPROVE 678867, RECONFIGURE 314544, ADDSAFE 233815.
- Standart kayıtları (EVS aynası): ISO 13374-1/-2, ISO 13381-1:2025, ISO 17359:2018, ISO 13379-1, ISO 20816-1; MIMOSA OSA-CBM; ECSS-E-ST-70-11C Rev.1.
- LUT profil ve laboratuvar sayfaları (Ahola, Lindh, Nevaranta, Sopanen, J. Pyrhönen, O. Pyrhönen, Peltoniemi, Pöyhönen, Niemelä); Sabancı Ünel grubu sayfası; Sensemore, Condence, Konecranes, KONE, Wärtsilä, VTT sayfaları.
