# Üç aşamalı (arıza teşhisi → kestirimci bakım → hata toleranslı kontrol) gömülü cihaz fikri için önceki çalışma, patent ve ticari ürün taraması

Tarih: 14 Ekim 2026
Hazırlayan: Claude (web tabanlı araştırma; hukuki bir patent/FTO görüşü değildir)

---

## 1. Kısa cevap

**Aradığınız biçimde bir ürün veya patent bulunamadı.** Yani: tek bir gömülü gerçek zamanlı kontrolcü (Raspberry Pi sınıfı) üzerinde, makineden bağımsız biçimde, (1) tüm açık veri setleriyle eğitilmiş ML ile olası tüm arızaları teşhis eden, (2) arızayı oluşmadan kestiren ve (3) arıza tipine göre uygun hata toleranslı kontrol stratejisini otomatik seçip uygulayan bir ticari ürün, açık kaynak sistem ya da patent istemi tespit edilemedi.

Ancak dört önemli uyarı var:

1. **Fikir yeni değil; parçaları ve "üçlü entegrasyon" düşüncesi yaklaşık 25 yıldır var.** En yakın örnekler: Rockwell/Reliance Electric'in 1999 öncelikli ve artık süresi dolmuş patent ailesi (motora gömülü teşhis + arıza zamanı tahmini + kontrol yasasını değiştirme), NASA/Impact Technologies/Georgia Tech'in 2007–2011 "prognostics-enhanced automated contingency management" çalışmaları (simülasyon), Xerox/PARC'ın hâlâ yürürlükte olan US11402833B2 patenti (kalan ömre göre otomatik güvenli mod / kontrolcü uyarlama / yeniden yapılandırma).
2. **2024–2026'da Çin'den gelen bir başvuru kümesi üç aşamayı belirli makineler için tek sistemde istemliyor** ve bazıları kenar cihazda çalışıyor: asansör invertörü (CN120802909A; STM32/S7-1200 yerel kontrolcü), hidroelektrik regülatör yağ pompası (CN122386948A; kenar birimi + PLC, arıza derecesine göre kesintisiz pompa anahtarlama), elektromekanik eyleyici (CN120143610A; FPGA/nöromorfik çip, açık bir rulman veri setinden transfer öğrenme), İHA (CN122450188A), maglev çekiş sistemi (CN116594314A). Ayrıca "arıza tipine/derecesine göre hazır strateji kütüphanesinden FTC seçimi"ni açıkça istemleyen Çin başvuruları var (CN121680485A istem 6, CN120278009A, CN120630935A, CN116317827A, CN118732480A). Hepsi **tek bir varlığa özel**, çoğu beklemede, bir kısmı geri çekilmiş; hiçbiri makineden bağımsız değil ve hiçbiri "tüm açık veri setleri" ile eğitim iddia etmiyor. FTO açısından bu küme, verilmiş Batı patentlerinden daha önemli.
3. **Her aşama tek başına çok kalabalık; ticari dünyada ise kasıtlı olarak ayrı tutuluyor.** Kestirimci bakım ürünleri (SKF, Schaeffler, Siemens Senseye, Augury, Samotics, Tractian, Sensemore vb.) **uyarı/iş emri** ile biter; otomatik kontrol tepkileri yalnızca sürücü/ECU/FADEC/uçuş kontrolcüsü içinde sabit kodlu, arıza başına ve kestirimsiz olarak var. 2026'daki "self-healing", "closed-loop", "AI agent" söylemleri de incelendiğinde iş emri otomasyonu veya proses optimizasyonu çıkıyor.
4. **"Olası tüm arızaları teşhis eder" iddiasının hiçbir emsali yoktur ve mevcut açık veri korpusu bunu desteklemez.** Açık veri setleri ağırlıkla rulman/dişli titreşimi; motor elektrik arızaları, hidrolik, pompa ve proses arızaları çok seyrek. 2024–2026'daki "temel model" (foundation model) çalışmaları bile titreşim ve rulman/dişli odaklı.

Dolayısıyla yeniliğiniz, aşamaların tek tek varlığında değil; **(a) makineden bağımsız, düşük maliyetli tek bir gerçek zamanlı kontrolcüde üçünün entegrasyonunda, (b) ML teşhis sınıfı + şiddet + kalan ömür + belirsizlik bilgisine göre genel bir FTC strateji kütüphanesinden seçim yapan ve bunu güvenlik kapılamasıyla uygulayan mekanizmada, (c) çok veri setli (foundation) teşhis modelinin kestirim ve kontrol katmanlarına gömülü ortamda bağlanmasında** olabilir. Patentlenebilirlik, somut teknik araçların istemlenmesine bağlıdır; "üç aşamalı yol haritası" tek başına patentlenemez, çünkü 2007'den beri standart PHM olgunluk modelidir.

---

## 2. Yöntem ve sınırlar

- **Tarama:** 14 araştırma açısı (patentler ×3, ticari kestirimci bakım ürünleri, sürücü/robot/havacılık/otomotiv ürünleri, akademik bütünleşik çerçeveler, evrensel teşhis modelleri ve açık veri setleri, Raspberry Pi/kenar uygulamaları ×2, standartlar ve kamu programları, start-up'lar ×2, Türkiye/Finlandiya/AB ×2, Çin/Japon/Kore patentleri). Yaklaşık 440 aday kayıt toplandı.
- **Doğrulama:** Çok aşamalı görünen en yakın 39 aday, birincil kaynaktan (Google Patents istem metni, USPTO PDF, makale tam metni/özeti, üretici kılavuzu) **çürütme amaçlı** ikinci bir inceleme ile doğrulandı; araştırmacı ajanların abartılı sınıflamaları düzeltildi. Aşağıdaki tablolar düzeltilmiş değerlendirmeyi yansıtır. Ek taramadan gelen 9 aday ise model limiti nedeniyle doğrulanamadı; bunlar "doğrulanmamış" olarak işaretlidir.
- **Ek patent sorguları:** Google Patents'in JSON uç noktası üzerinden İngilizce, Çince, Japonca, Korece ve Almanca anahtar kelimeler ve CPC sınıflarıyla yaklaşık 50 sorgu denendi; yarıdan fazlası Google'ın bot engeline (503) takıldı.
- **Sınırlar:** Bu bir web taramasıdır; profesyonel yenilik/FTO (freedom-to-operate) araştırmasının yerine geçmez. Espacenet, PATENTSCOPE, TÜRKPATENT, PRH (Finlandiya), Lens ve LUTPub bu ortamdan doğrudan sorgulanamadı. Japonca sorguların çoğu engellendi; Japon patent kapsamı eksiktir. Bazı üretici sayfaları (ABB, SKF, Schaeffler, Omron, Rockwell, Nanoprecise, OnePredict) erişilemediğinden ilgili bilgiler ikincil kaynaklara dayanır ve metinde belirtilmiştir.

---

## 3. En yakın önceki çalışmalar (doğrulanmış)

Puan: 10 = üç aşama tek gömülü gerçek zamanlı kontrolcüde, genel makine, çok veri setli ML; 8–9 = üç aşama tek alanda donanımda; 6–7 = üç aşama istemlenmiş/simüle edilmiş veya iki aşama uygulanmış; 4–5 = sıradan kestirimci bakım veya tespitli FTC; 1–3 = tek aşama.

### 3.1 Patentler (ikinci incelemeden geçenler)

| Puan | Kimlik | Sahip / yıl | Hukuki durum | Kapsadığı aşamalar | Eksik olan |
|---|---|---|---|---|---|
| 6,5 | US6326758B1 (aile: US6646397B1, US7301296B2, US7538512B2) | Reliance Electric / Rockwell, Discenzo; öncelik 1999 | **Süresi doldu** (2019–2020) | Motora gömülü teşhis + sağlık değerlendirme, arıza zamanı ve nedeninin tahmini, kontrol sinyalini değiştirmeye karar verme (bağımsız istem 9 döngüyü otomatik kapatır) | Tek makine sınıfı; model tabanlı, ML/veri seti yok; prototip yok; FTC "yumuşak kontrol yasasına geçiş / kazanç değiştirme", arıza tipine göre strateji seçimi değil |
| 6,0 | CN120802909A | Xiangmai Intelligent Tech (Shaanxi), 2025 | **Beklemede** (inceleme 11/2025) | Dijital ikiz ile asansör invertörü: arıza tipi teşhisi + IGBT kalan ömrü + otomatik hata toleranslı modülasyon/derating; bağımsız istemde üçü de var; kenar-bulut bölünmesi, yerel STM32H743 veya S7-1200 | Tek bileşen (7 önceden tanımlı arıza modu); açık veri seti yok; prototip yok |
| 6,0 | CN122450188A | Huai'an Üniversitesi, 2026 | **Beklemede** | İHA elektromekanik sistemleri: LSTM arıza tahmini/teşhisi + RUL, Pareto tabanlı hata toleranslı karar, kontrol yasası yeniden yapılandırma | Yalnızca simülasyon; gömülü donanım yok; teşhis/kestirim yalnızca bağımlı istemlerde |
| 5,0 | **US11402833B2** (JP7702337B2 de verildi; EP4006676A1 geri çekilmiş sayıldı) | PARC → Xerox, Kai Goebel; 2020/2022 | **Yürürlükte** (bakım ücreti 07/2026'da ödendi; ~2040'a kadar) | Varlıktan bağımsız: sağlık izleme → RUL → RUL görev süresinden kısaysa otomatik "fail-safe / kontrolcü uyarlama / yeniden yapılandırma / görev değiştirme" (Markush seçimi: yalnızca görev değiştirmeyle de karşılanır) | Arıza tespiti yalnızca bağımlı istemlerde; eylem arıza tipine göre değil RUL kademesine göre; gömülü donanım yok; ML yok. **Aşama 2→3 mantığı için en kritik yürürlükteki Batı patenti** |
| 5,0 | US10146611B2 | Siemens, 2012/2018 | Yürürlükte (~2034) | Alt sistemlere yakın dağıtık kestirim motorları (SOM sağlık göstergesi, RUL) → yükü sağlıklı alt sistemlere kaydıran kontrol stratejisi | Arıza izolasyonu yok; sistem düzeyinde yük dağıtımı |
| 5,0 | US11133771B2 | GM, 2019/2021 | Yürürlükte (~2039) | Araç motor kontrolcüsünde SOH tabanlı arıza izolasyonu (resolver/akım sensörü/sargı) + tork düşürme | Kestirim eşik tabanlı; tek makine sınıfı; tek sabit eylem |
| 5,0 | US10591886B2 | Omron, 2016/2020 | Yürürlükte (~2038) | PLC'de ML eşiğiyle anormallik tespiti → yedek cihaza otomatik geçiş | "Kestirim" erken eşik; FTC yalnızca donanım yedeği anahtarlama |
| 5,0 | US8577509B2 | Vestas, 2009/2013 | **Düştü** (11/2025) | Rüzgar türbini: arıza modu → kalan ömür → kontrol şeması (derating) seçimi | Kontrol adımı bağımlı istemde; CBO birimi veri merkezinde; manuel seçim de kapsanıyor |
| 5,0 | US8942882B2 | Boeing, öncelik 2004 | **Düştü** | IVHM "gatekeeper" mimarisi; açıklamada eyleyici arızası tahmini ve uçuş kontrol yeniden yapılandırması | Bağımsız istemler veri doğrulama mimarisini kapsıyor |
| 5,0 | US10423473B2 | UTC/RTX, 2017/2019 | Yürürlükte (~2037) | Gaz türbini: yerleşik eyleyici/sensör bozulma tespiti → MPC kısıt/ağırlık yeniden yapılandırma | RUL yok; ML yok |
| 5,0 | US7536277B2 | Toyota/UConn, 2004/2009 | **Düştü** | ECU yerleşik teşhis ajanları + "sistem işleyişini doğrudan etkileyen" iyileştirici eylem | Kestirim ve limp-home yalnızca bağımlı istem/açıklamada |
| 4,0 | US6823675B2 | GE, 2002/2004 | **Süresi doldu** | Teşhis + "master mode selector" + yeniden yapılandırılabilir model tabanlı kontrol (gaz türbini) | Kestirim yok |
| 4,0 | US8612079B2 | GM, 2011/2013 | **Düştü** (12/2025) | SOH/SOF/RUL → en düşük maliyetli ömür uzatıcı stratejiyi seçip uygulama | Arıza teşhisi yok |
| 4,0 | **US12504725B2** | GE, 2023; verildi 12/2025 | **Yürürlükte** (~2044) | Anormallik (ağırlıkla siber saldırı) tespit edilince çevrimdışı ayarlanmış kontrolcü kütüphanesinden otomatik kontrolcü değiştirme | Kestirim yok; teşhis yöntemi istemde yok; gömülü değil. **Anormallik → kontrolcü kütüphanesinden seçim** mantığı için FTO açısından dikkate alınmalı |
| 4,0 | US10048670B2 ailesi (Beet Inc.) | 2014/2018 | Yürürlükte | Fabrika düzeyi: çevrim süresi sapması → arıza tahmini → yedek eleman/üretim yönlendirme | Makine kontrolü değil |
| 4,0 | Valmet/Neles ND9000 (ürün; kılavuz 7ND9071EN) | Valmet, Finlandiya | Ürün | Gömülü 32-bit MCU vana konumlandırıcı: öz-teşhis + iç sensör arızasında "düşük performans modu"nda kontrole devam veya fail-safe konum; bakım için trend/sayaç | Kestirim yok; FTC yalnızca kendi iç sensör arızaları için; vana/eyleyici arızaları uyarı |
| 4,0 | US6892317B1 / JP2001216423A | Xerox, 1999 | Süresi doldu | Yazıcı ağı: tahmin + teşhis + sunucu tetiklemeli otomatik yeniden kalibrasyon | Çevrimiçi FTC değil |
| 3,5 | US11193387B2 | GE, 2017/2021 | Yürürlükte (~2037) | FADEC'te ömür/hasar modelleri → "sağlık trimleri" | Arıza teşhisi yok |
| 3,5 | US9134713B2 | Siemens, 2012/2015 | **Düştü** (2023) | MPC'de artık tabanlı arıza tespiti → ayar/model yeniden yapılandırma | RUL yok; otomatiklik zorunlu değil |
| 3,5 | US9221535B2 | Honeywell, 2013/2015 | **Düştü** (2023) | Çok motorlu sistemde RUL eşitleyen yük paylaşımı | Teşhis yok |
| 3,0 | US10626748B2 | GE, 2014/2020 | Yürürlükte (~2035) | Sürünme hasarı/RUL → set noktası | Teşhis yok |
| 3,0 | US10539932B2 | Intel, 2017/2020 | **Düştü** (2024) | Kenar cihazda titreşim enerjisi → seçici yükleme; bağımlı istemde motor ayarı | Teşhis sunucuda |
| 3,0 | US10378515B2 | Equinor, 2013/2019 | Yürürlükte (~2035) | Ana rulman yük profili kontrolü; açıklamada "beliren arızada otomatik derating" | Derating istemlenmemiş |
| 3,0 | US11808248B2 | Fischer Block, 2020/2023 | Yürürlükte (~2041) | Filo düzeyi sağlık indeksi → uyarı; bağımlı istemde çalışma noktası ayarı | Kestirim yok |

### 3.2 Çin/Kore patent kümesi (istem 1 veya özet okundu; ikinci incelemeden geçmedi)

| Kimlik | Sahip / yıl | Durum | Ne istemliyor | Not |
|---|---|---|---|---|
| CN122386948A | Hubei Energy Lushui Hydropower, 2026 | Beklemede | Hidroelektrik regülatör yağ pompası: dört katmanlı ML teşhis (Isolation Forest, CNN+LSTM, şiddet derecelendirme, LSTM bozunma trendi) + öncü derece + RUL + arıza derecesine göre kesintisiz pompa anahtarlama; **kenar birimi + PLC (≤10 ms)** | Üç aşama, kenar donanımı; tek varlık |
| CN120143610A | Guangdong Polytechnic of Industry and Commerce, 2025 | Beklemede | Elektromekanik eyleyici: titreşim/akım/sıcaklık → SNN füzyonu → DTW ile arıza şablon kütüphanesi (tip + güven) → yedek eyleyiciye geçiş, tork rampası, PID kazanç uyarlaması; bağımlı istemde SNN-LSTM RUL; **FPGA + nöromorfik kenar**; **açık bir rulman veri setinden transfer öğrenme** | Üç aşama; taramada açık veri setine atıf yapan tek patent |
| CN116594314A | Çin Bilimler Akademisi Elektrik Müh. Enst., 2023 | Bilinmiyor | Dijital ikiz ile maglev çekiş sistemi: sağlık izleme + arıza tahmini + uyarlamalı optimizasyon ve FTC (istem 1, dört adım) | İstem ayrıntıları okunamadı |
| CN118732480A | Roket Kuvvetleri Müh. Üniv., 2024 | Beklemede | Dijital ikiz ile uçak eyleyicisi: gözlemci + ikiz tahmini → arıza durumu (sağlıklı / kontrol edilebilir / kontrol edilemez) → duruma göre FTC | Teşhis + durum tahmini + FTC |
| CN121680485A | Shenzhen Huajie Digital Energy, 2026 | Beklemede | PV izleyici saha kontrolcüsü: motor akım/gerilim, titreşim, enkoder tutarlılığı → özellik kütüphanesiyle arıza modu → **istem 6: her arıza tipine bir strateji** (aşırı yük → güvenli eğim; sıkışma → ters sürüş; sensör arızası → veriyi yoksay) | Açık "tip → strateji" istemi |
| CN120278009A | San Dianshui New Energy (Anhui), 2025 | Beklemede | Gemi: dijital ikiz → arıza tipi + seviyesi → **bilgi grafiği kütüphanesinden FTC şeması seçimi** → seyre devam | Açık "tip → strateji" istemi |
| CN120630935A | Tsinghua Shenzhen Araştırma Enst., 2025 | Beklemede | Otomotiv şasi alan kontrolcüsü: FTA ile arıza modu kütüphanesi, ML ile arıza modu **tahmini** ve şiddeti → şiddete göre yeniden ayar / kontrolcü değiştirme / izole + bozulmuş mod | Gömülü; RUL yok |
| CN116317827A | Beihang, 2023 | Bilinmiyor | PM motor: TMS320F28062 MCU; Hall/faz/rulman/sıcaklık teşhisi → **arıza tipine göre mod** (Hall arızası → sensörsüz back-EMF; aşırı sıcaklık → derating) | Teşhis + FTC gömülü; kestirim yok |
| CN118963327A | Bireysel başvuru (Zheng Zhicong), 2024 | **Geri çekildi** | Genel "mekatronik sistem": uyarlamalı teşhis (CNN/RNN/SVM), RUL (random forest), erken uyarı, öz-iyileşme kontrolü (parametre ayarı + yedek anahtarlama), sanal algılama | Hedef kavrama en geniş istem; geri çekilmiş |
| CN121484876A | Guizhou Power Grid, 2025 | Beklemede | Dağıtım şebekesi esnek bağlantı cihazı: derin öğrenme teşhisi + şiddet → öz-iyileşme kontrolü | Güç sistemi |
| CN118630268A | Dalian Teknoloji Üniv., 2024 | Beklemede | PEMFC: ömür tahmini (IGWO-ESN, CNN-BiLSTM) → referans bozunma hızını izleyen PID-ILC giriş basıncı kontrolü | Kestirim → kontrol; teşhis yok |
| CN113485304B | Beihang, 2021 | Verildi | Uçak: derin öğrenme arıza parametresi teşhisi + katmanlı FTC | Teşhis + FTC |
| CN121282805A | Nantong Zhengyao, 2025 | Durduruldu | Güç sistemi: teşhis → GRU+dikkat RUL → kurtarma kararı → kontrol yürütme | Özet düzeyinde |
| KR102383775B1 | Doosan Heavy Industries, 2020 | **Verildi** | Santral: teşhis sistemi "tahmin edilen arıza" için hata toleranslı kontrol değeri üretir, yanma optimizasyonuyla birleşerek otomatik kontrol komutu | Tesis düzeyi; gömülü değil |
| US12500532B1 | Southwest Jiaotong Univ., 2025 (CN önceliği) | **Verildi (ABD)** | Motor sürücü akım sensörü arızaları: Jetson Xavier'de 1D-CNN teşhis (<20 ms) → dSPACE'te FTC; 6 sensör arızası | Teşhis + FTC, kenar AI; kestirim yok |

Ayrıca ilk taramada görülen, tema açısından anlamlı patentler: yalnızca teşhis + FTC (kestirimsiz): US7454255B1 (Scientific Systems), US8763950B2 (Bell), WO2012118564A2 (Eaton), CN101995821B (Harbin), US7002318B1 (GM), CN108828944B (Shandong), US6140789A (Mitsubishi), US11203950B2 (RTX FADEC), US6085127A (Aurora), CN102854874B (NUAA), CN109595687A (Jilin, DCS: arıza tipine göre farklı kontrol stratejisi, 2019). Yalnızca kestirim → kontrol ("ömür uzatıcı kontrol"): US7203554B2 (UTC), US9569901B2 (Denso), US7581434B1 (Rockwell), US12282324B2 (JCI), CN104389685A/CN104564354A (NWPU), US8734105B2 (Vestas). Yalnızca teşhis + kestirim: US11188065B2 (Nanoprecise), US7882394B2 (Brooks), EP2836881B1 (Siemens PLC), US11853047B2 (Augury transfer), US8868985B2 (Siemens sentetik veri), US7308385B2 (SmartSignal), US12066797B2 (FANUC + Preferred Networks: ML anomali derecesi → bildirim), EP2156254B1 (Boeing), US7688603B2 (ABB Oy Helsinki, sürücü öz-izleme).

### 3.3 Akademik çalışmalar ve programlar

| Puan | Çalışma | Ne yapıyor | Eksik olan |
|---|---|---|---|
| 5,5 | Prognostics-enhanced Automated Contingency Management (ACM+P): Tang, Kacprzynski, Goebel, Saxena, Saha, Vachtsevanos, PHM 2008 (DOI 10.1109/PHM.2008.4711448); "Prognostics in the Control Loop" AAAI 2007; IEEE Aerospace 2010 | Teşhis + kestirim bilgisinin bileşen/sistem düzeyinde kontrol yeniden yapılandırma ve görev yeniden planlamayı sürdüğü hiyerarşik "proaktif FTC" mimarisi (NASA STTR) | 2008 makalesinde teşhis/kestirim **simüle edilmiş**; yalnızca masaüstü simülasyon; patent bulunamadı |
| 5,5 | D. W. Brown, Georgia Tech doktora tezi, 2011 (+ PHM Society 2009 EMA makalesi) | RUL/TTF tahminine göre kontrol otoritesini yeniden yapılandıran üç katmanlı mimari, kararlılık kanıtları | MATLAB/Simulink; tek arıza modu; donanım yok |
| 5,5 | GitHub "Fault-Finding-in-Inverters" (Amrita Müh. Fak. öğrencileri, 2026) | Tek MOSFET için kNN teşhis + erken uyarı + üstel RUL + uyarlamalı derating FTC zinciri | Simülasyon; 3 sınıf; eğitim modeli depoda yok |
| 5,0 | Vachtsevanos, Georgoulas, Nikolakopoulos, MED 2016 | "Condition monitoring → fault detected? → RUL + performans değerlendirici → reconfigurable control" akış şeması | Yalnızca alt katman MPC derating simüle edildi |
| 4,0 | Tampere Üniv. (Mattila grubu), IEEE/ASME AIM 2025 (arXiv 2502.03278) | 6,65 t hidrolik mobil robotta **Beckhoff CX2030 IPC üzerinde 1 kHz** model-free uyarlamalı FTC; sensör/valf arızaları yazılımla enjekte edilip telafi edildi | Teşhis yalnızca uyarlamalı parametrede örtük; kestirim yok; ML yok |
| 4,0 | Sağlık-farkında kontrol hattı: Escobet/Puig/Nejjari (2012), Salazar tezi (2018), Karimi Pour & Puig (MED 2021); Cieslak, Gucik-Derigny, Chang (Bordeaux, 2020/21: FDI + anahtarlamalı FTC + kestirimsel karar) | Bileşen güvenilirliği/RUL'u MPC maliyetine koyarak bozunmayı yavaşlatma | Simülasyon; teşhis çoğunlukla "bilindiği varsayılır" |
| 4,0 | fortiss RISE projesi (MST Kongress 2021) | Çip üstü yorulma izleme → bulutta ML RUL → yazılımı sağlıklı işlemcilere taşıma | Makine FTC'si değil |
| 4,0 | Lipiec, Mrugalski, Witczak, Stetter, AMCS 2022 | Rulman bozunumu (PRONOSTIA) → TTF → filo görev dengeleme | Makine düzeyinde kontrol yok |
| 3,5 | Aalto (Jämsä-Jounela grubu): Kettunen 2011 veri tabanlı FT-MPC; Sarkar vd. 2017 veri uzlaştırmalı MPC | Proses FDD + MPC uyarlaması | Simülasyon; 2017'de teşhis yok |
| 3,0 | Troyes hattı (Langeron, Grall, Barros; Gong 2024), Calabria (Tedesco, Casavola), Mrugalska & Stetter 2019, Sabancı (Ünel) | RUL'a göre LQR ağırlığı; bozunmaya göre kontrol tahsisi; SOH'a göre AGV görev dağıtımı; ayrı ayrı quadrotor FTC ve filo anomali tespiti | Teşhis yok veya entegre değil; simülasyon |
| — | NASA PCoE "Prognostics-enabled Decision Making" K11 gezgin testi (2011–2014) | Bulunan **tek donanım gösterimi**: teşhis + kestirim → otomatik rota yeniden planlama | Kontrol yasası yeniden yapılandırması değil |
| — | NASA IFCS (F-15), NASA IRAC, ESA/ECSS FDIR, EU RECONFIGURE (FP7), ITU Hajiyev/Çalışkan FDI + yeniden yapılandırma (kitap 2003) | Teşhis → otomatik kontrol yeniden yapılandırma (uçuşta/uzayda/simülasyonda) | Kestirim yok |
| — | EU projeleri SelSus, MANTIS, SERENA, PROPHESY, Z-BRE4K, UPTIME, AI-PROFICIENT, IMPROVE; Paderborn SFB 614; VTT Research Notes 2343 (2006) | Aşama 1–2 platformları; PROPHESY "bakım güdümlü gerçek zamanlı kontrol"ü gelecek zaman kipinde vaat etti; VTT 2006 raporu OSA-CBM katmanları arasında "karar desteği (limp-home, otomatik yeniden yapılandırma)"yı tasarım seçeneği olarak listeler | Hiçbiri döngüyü kontrolcüde kapatmadı |
| — | Gill, Markaj, Gehlhoff (HSU Hamburg), arXiv 2505.02076 (2025) | LLM ajanları + dijital ikizle proses tesisinde arıza semptomu tespiti → düzeltici kontrol eylemi önerisi → ikizde doğrulama; "bilinmeyen arıza tipleri" hedefli | Simülasyon; bulut LLM; kestirim yok |

**Akademik özet:** Aldrini vd. (J. Intell. Manuf. 2023) derlemesi "FDD ile öz-iyileşme/FTC'yi bir araya getiren modellerin eksikliğini" açıkça belirtiyor; Bougacha vd. (IJPHM 2020) kestirim güdümlü kontrol yeniden yapılandırmayı küçük bir alt kategori olarak listeliyor. NASA PCoE'nin kendi sayfası "yerel kestirim bilgisinin kontrolcü düzeyinde değişikliklere nasıl çevrileceğini" **açık araştırma sorusu** olarak listeliyor. Terminoloji tuzağı: literatürde "PFTC" çoğunlukla *pasif* FTC demektir; aradığınız kavram "health-aware control", "proactive FTC", "prognostics-enhanced reconfigurable control", "degradation-tolerant control", "RUL control", Çince "故障预诊 + 剩余寿命 + 容错/自愈" adlarıyla geçer.

---

## 4. Aşama aşama manzara

### 4.1 Aşama 1: Durum izleme ile arıza teşhisi

**Ticari ürünler (hepsi uyarı ile biter):** SKF Enlight AI / IMx, Schaeffler OPTIME, Siemens Senseye ve SITRANS SCM IQ / SIPLUS CMS, ABB Ability Smart Sensor, Emerson AMS / PeakVue, Bently Nevada System 1, Honeywell Forge APM, AVEVA Predictive Analytics, Augury, Samotics SAM4, Nanoprecise, Fluke/Azima WATCHMAN, Tractian, Petasense, KCF, Novity TruPrognostics (PARC spin-out), Artesis e-MCM, Ronds (Çin), OnePredict (Kore), Witium WitEBox (Çin), Sensemore (Türkiye), Condence/Distence (Finlandiya), Amazon Monitron (bakım modunda) ve Lookout for Equipment (destek 10/2026'da bitiyor). En geniş arıza listesi iddiaları: KCF ("neredeyse her arıza tipi", 50+ tip), Tractian (70–75+ arıza modu, "tüm başlıca arıza modları"), Novity ("doğrulanmış arıza modlarının %90'ından fazlası"), Samotics (sınıf başına "kanıtlı/gelişen/erken" olgunluk notu). **Hiçbir satıcı "tüm arızaları" iddia etmiyor**; dürüst olanlar arıza başına olgunluk notu yayımlıyor ve analistleri döngüde tutuyor.

**Gerçek zamanlı kontrolcü içinde ML:** Omron Sysmac AI Controller, Beckhoff TwinCAT TF3600 + TF3800 (gerçek zamanlı PLC'de ONNX çıkarımı; küçük ağlar için 50 µs çevrimde <100 µs), Weidmüller edgeML, Phoenix Contact PLCnext MLnext, Rockwell LogixAI/GuardianAI, Mitsubishi SCM, Danfoss/VACON sürücü içi CBM, **TI C2000 TMS320F28P550SJ (NPU'lu gerçek zamanlı kontrol MCU'sunda rulman/ark arızası CNN'i)**, AISing AiiR (MCU üzerinde cihaz içi öğrenme). Bunlar **platform**; tepkiyi entegratör programlar. Hedefinize en yakın "ticari zemin" bu gruptur; TI C2000 örneği "teşhisin kontrol döngüsünü çalıştıran aynı MCU'da yapılması" açısından mimari olarak en yakın ticari parçadır.

**Evrensel / temel (foundation) teşhis modelleri (2024–2026):** "Birisi birçok açık veri setiyle tek model eğitti mi?" sorusunun cevabı **evet, kısmen**:

| Model | Kurum | Eğitim verisi | Teşhis | RUL | Gömülü |
|---|---|---|---|---|---|
| UniFault (arXiv 2504.01373) | A*STAR / Maryland | ~11 açık rulman seti, 6,9 M örnek | Evet | Hayır | "Lite" 823 K parametre (Pi'ye sığar, test edilmemiş) |
| VibFM (PHME 2026) | Stuttgart Üniv. | 16 açık set, ~400 saat | Evet | Hayır | Hayır |
| TSFM | Seoul Nat. Univ. / OnePredict | 17 titreşim seti | Evet (öznitelik çıkarıcı) | Hayır | TorchScript, test yok |
| BearLLM (AAAI 2025) | CAS Shenyang | 9 açık benchmark, tek ağırlık seti | Evet (+ metin raporu) | Hayır | Hayır (Qwen2-1.5B) |
| RmGPT (arXiv 2409.17604) | SJTU / PoliMi | ~5–7 set | Evet | **Evet** (XJTU-SY) | "Orin" gecikme sütunu var, ayrıntı yok |
| PHM-Vibench (PHMAP 2025) | Tsinghua | 20+ set, benchmark çerçevesi | Evet | Evet | Hayır |

Ortak sınırlar: yalnızca titreşim; rulman/dişli odaklı; MCSA, hidrolik, pompa, proses arızaları korpusta yok; makineler/çalışma koşulları arası dağılım kayması (HUST DG benchmark'ı bunu ölçüyor); etiket uzayı uyumsuzluğu; ön eğitim/test sızıntısı riski. Hiçbiri kontrol yapmıyor, hiçbiri gömülü kontrolcüde çalıştırılmadı. Patentlerde açık veri setine atıf yapan tek belge CN120143610A (açık bir rulman setinden transfer öğrenme).

### 4.2 Aşama 2: Kestirimci bakım / kalan ömür

- RUL iddiası olan ürünler: Senseye ("patent-pending"), Azima WATCHMAN, AVEVA PA, Honeywell APM, Nanoprecise RotationLF, Novity (olasılıksal arıza zaman penceresi), Sensemore (aylar öncesinden), Schaeffler OPTIME (haftalar), Samotics (5 aya kadar), ABB CBM for drives (1–2 yıl), Konecranes TRUCONNECT, Renesas Reality AI (MCU'da bileşen RUL'u). **Hepsi danışman niteliğinde**; hiçbirinin doğruluğu için bağımsız benchmark yok.
- Sürücü/kontrolcüye gömülü kestirim: Danfoss VLT / VACON CBM, Schneider Altivar Predict, Mitsubishi MR-J5, Rockwell PowerFlex 755T, Yaskawa GA700, Siemens Drivetrain Analyzer Edge, FANUC ZDT (ve FANUC/Preferred Networks US12066797B2: ML anomali derecesi → bildirim), KUKA iiQoT. Hiçbiri kestirim çıktısını kontrol yasasına bağlamıyor; Danfoss kırmızı alarmda makineyi **durduruyor**.
- Kenar cihazda teşhis + RUL (kontrolsüz) artık rutin: Pi 4B dijital ikiz ön baskısı (Patil vd. 2026: 12–18 ms çıkarım, RUL), ESP32-S3 (Kumar vd. 2026: sınıflandırma + TTF, <50 ms), RP2040 batarya RUL (2025).
- Açık kaynak: NASA ProgPy. Standartlar: ISO 13374 / OSA-CBM "advisory generation" ile biter; ISO 13381-1 (2025) yalnızca kestirim süreci; IEEE 1856, SAE JA6268, DoD CBM+, F-35 ALIS/ODIN danışman/lojistik düzeyinde.

### 4.3 Aşama 3: Hata toleranslı kontrol

**Ticari olarak var olan otomatik tepkiler (sabit kodlu, arıza başına, kestirimsiz):**

- Sürücüler: Siemens SINAMICS S120 p0491 (enkoder arızasında enkodersiz kontrole otomatik geçiş), ABB ACS880 90.45/90.46 (geri besleme kaybında tahmini hızla devam), 30.31 (düşük gerilim ride-through), Nidec Unidrive M (termal sınırda anahtarlama frekansını düşürme).
- Otomotiv/havacılık/denizcilik: Bosch iBooster + ESC fail-degraded fren, fail-operational EPS; FADEC sensör telafisi (RTX); Wärtsilä UNIC motor kontrolü (koruyucu yük azaltma; kestirim verisi gemi dışı; broşür düzeyi kanıt); Valmet/Neles ND9000 konumlandırıcı (iç sensör arızasında düşük performans modu).
- İHA: PX4 Failure Detector + CA_FAILURE_MODE, ArduPilot EKF3 şerit değiştirme; TU Delft / TU Braunschweig / ETH rotor kaybı FTC'leri gerçek uçuşta.
- Takım tezgahı: Sandvik Coromant CoroPlus Process Control, MachineMetrics "feed hold" (otomatik mi belirsiz).
- Koruma sistemleri (API 670): fail-safe **trip**, FTC değil.

**Otomatik kontrol yazan AI ürünleri arıza güdümlü değil:** Imubit (RL ile DCS/PLC set noktası yazma, proses optimizasyonu), Phaidra (veri merkezi soğutma ajanları). Kestirimci bakım satıcılarının "closed-loop"u (Augury–MaintainX, Tractian, Oxmaint) sensör → teşhis → otomatik iş emri anlamına geliyor; "prescriptive" ise planlayıcı onaylı öneri. Augury'nin 2026 rol tabanlı ajanları, OnePredict'in "AI-native factory" vizyonu (Eylül 2026) ve Avathon'un "autonomous operations"ı danışman veya yol haritası düzeyinde. Tek açık "otomatik set noktası değişikliği" iddiası iFactory'nin "Self-Healing Manufacturing Systems" sayfası (mühendis tanımlı zarf içinde hız/basınç/ilerleme ayarı); donanım, RUL veya vaka verisi yok, CMMS satıcısı pazarlaması olarak değerlendirildi. Nisan 2026 tarihli bir Substack yazısı ("Self-Healing Motor Controller": FOC + TinyML teşhis + limp mode + açık faz yeniden yapılandırma, NVIDIA Orin) kavramsal, yapılmamış. Dikkat: 2025–2026'daki bazı SEO bloglarında (ör. "AD7403-2 düğümleriyle otomatik tork derating", Schneider "Auto-Fix Templates") doğrulanamayan, muhtemelen uydurma iddialar var.

**Patentlerde FTC:** Batı patentlerinde ML teşhisine göre bir **strateji kütüphanesinden seçim** istemi yok (en yakın GE US12504725B2'nin anormallik bölgesine göre kontrolcü kütüphanesi); **Çin başvurularında ise var** (CN121680485A istem 6, CN120278009A bilgi grafiği, CN120630935A şiddete göre, CN116317827A arıza tipine göre mod, CN118732480A duruma göre, CN109595687A 2019). Bunlar el ile kodlanmış, varlığa özel eşlemeler.

**Neden ticari dünyada birleşmiyor?** Samotics "bakım tepkisine sizin ekibiniz karar verir", AVEVA kullanıcının "acil durdurmayı başlatıp başlatmayacağına" karar vermesini bekliyor, Augury/Infinite Uptime "kararları fabrika ekibinden almayız" diyor. Sebep teknoloji eksikliği değil, **işlevsel güvenlik ve sorumluluk**: otomatik kontrol yeniden yapılandırması deterministik, doğrulanabilir ve sertifikalanabilir olmalı (IEC 61508 / ISO 13849; IEC 61800-5-1 otomatik yeniden başlatmada uyarı etiketi istiyor), ML teşhisi ise olasılıksal. Bu boşluk hem fırsatınız hem de en büyük engelinizdir.

### 4.4 Gömülü platform ve Raspberry Pi

- **Raspberry Pi tabanlı ticari bir kestirim/FTC ürünü yok.** Pi tabanlı ticari durum izleme cihazları var ama yalnızca tespit/uyarı: Mechmine mmBox-mini (İsviçre; analiz bulutta), PiLink PL-R4 (Japonya; Pi üzerinde FFT/zarf analizi, STM32 ile 20 kHz örnekleme), Industrial Shields Raspberry PLC / GateBerry (CM4; "cihazda anomali tespiti" iddiası). Pi tabanlı endüstriyel platformlar: KUNBUS Revolution Pi (KUNBUS forumu: RevPi Connect + CODESYS ile 100 µs çevrim / 1 µs jitter **mümkün değil**), Brainboxes BB-400 (CM3+ + Arduino), Monarco HAT + REXYGEN, CODESYS Control for Raspberry Pi (lisans: özel kullanım/test/eğitim), LinuxCNC Pi 4/5 imajı (RT çekirdek şart). GitHub'da "fault diagnosis" + "remaining useful life" + "fault-tolerant control" üçlüsünü içeren **hiçbir depo yok**.
- **Doğrulanmış gerçek zamanlılık ölçümleri:** Pi 5 + PREEMPT_RT (6.6.21), 1 saat stres altında cyclictest ortalama 5,91 µs, en kötü 124–125 µs (standart çekirdekte en kötü 36,8 ms) [Dewit vd., OSPERT 2024]; Pi 5, 250 Hz döngü, isolcpus + SCHED_FIFO 99: ortalama 31 µs, P99 130 µs, en kötü 224 µs; SCHED_OTHER ile 4–9 ms [Giacomossi vd., arXiv 2604.19275, 2026]; Pi 3 + PREEMPT_RT: GPIO IRQ tepki ~118 µs, nadiren >1 ms, 150 µs tasarım sınırı önerisi [Adam vd., Electronics 2021]; Pi 5'te SPI işlemlerinde yük altında 1,5–2 ms sapmalar (RP1 DMA), CM4'te sabit [Pi forumları]; hibrit Pi 3B+ (SCHED_FIFO) + TM4C123 test düzeneği: kontrol görevi jitter ort. 10 µs / en kötü 61 µs, 300 ms MCU watchdog fail-safe [YigitalpDellal, kendi raporu]. Bir 2025 rotor arızası farkında quadrotor makalesi Pi sınıfı kartların kendi kontrol hızı için yavaş olduğunu açıkça belirtiyor. Pi'de ML çıkarımı bellek yolunu yüklediğinden jitter kaynağıdır.
- **Sonuç:** Aşama 1–2 Pi 4/5/CM5'te (12–50 ms çıkarım yeterli); Aşama 3 kontrol döngüsü ya RT çekirdekli, CPU izole edilmiş Pi'de (yüzlerce µs sınıfı) ya da güvenlik için RP2350/STM32 eş işlemcisinde veya sertifikalı PLC/sürücüde. Bu hibrit mimari, bulunan tek Pi tabanlı FTC test düzeneğinin ve US12500532B1'in (Jetson'da teşhis, dSPACE'te FTC) de tercih ettiği yapıdır.
- TinyML araç zincirleri (ST NanoEdge AI, Edge Impulse — Pi 4/5 tam destekli, Renesas Reality AI — RUL iddiası, SensiML, Infineon DEEPCRAFT, NXP eIQ, TDK SensEI) Aşama 1'i ucuza prototiplemeyi sağlar; hiçbirinin endüstriyel makinede nicel doğrulukla yayımlanmış RUL vakası bulunamadı.

### 4.5 Bölgesel durum (Türkiye, Finlandiya, AB)

**Türkiye** (22 ek arama; patent veri tabanları engellendi): Üç aşamayı birleştiren hiçbir ürün, patent, proje veya tez bulunamadı. Sanayi: Sensemore (bulut, ESA + titreşim, RUL iddiası, uyarı), Artesis e-MCM (model tabanlı sensörsüz motor izleme; "patentli" deniyor ama numara doğrulanamadı), ASELSAN HUMS (helikopter için gömülü titreşim teşhisi; yalnızca teşhis), FNSS zırhlı araç kestirimci bakımı (trend analizi → operatöre uyarı), Polat Group Redüktör + Adeon (TÜBİTAK SAYEM 1832 dişli kutusu izleme), TEKNOPAR (yüzer rüzgar türbini SHM + RUL), OPEVA (TÜBİTAK 222N269: araç arızasında filo rotası yeniden planlama; araç üstü değil). Akademi: İTÜ Hajiyev/Çalışkan (Kalman yenilik tabanlı FDI + uçuş kontrolcüsü yeniden yapılandırma; kitap 2003; simülasyon), Kabaoğlu & Eksin (İTÜ Dergisi 2011: SVM ile arıza tipi tanıma + doğrudan FTC; simülasyon), Gebze TÜ (ANN eyleyici arızası + robust-adaptif FTC, 2026), Anadolu (UIO + Hamming NN FDI + yeniden yapılandırma, 2013), Kocaeli (Erentürk, LMI tabanlı FT izleme, 2014), Fırat Üniv. (Aydın, Karaköse, Akın: **FPGA'da gerçek zamanlı** asenkron motor FDD serisi, 2010–2019), Sabancı (Ünel: ayrı ayrı quadrotor FTC simülasyonu ve Ford Otosan filo anomali tespiti). Ege Üniv. (Meşe) çok fazlı hata toleranslı sürücü çalışmaları bu taramada bulunamadı. Türk FTC araştırması havacılık odaklı ve simülasyon tabanlı; sanayi PdM'i uyarıda bitiyor.

**Finlandiya / LUT:** Üç aşamayı birleştiren Finlandiya kaynaklı ürün/patent/yayın yok. Gömülü ürünlerde teşhis + koruyucu/yedek davranış var ama öğrenilmiş kestirim veya teşhis güdümlü kontrolcü seçimi yok: Valmet/Neles ND9000 konumlandırıcı (doğrulandı; FTC kısmi), VACON/Danfoss Vaasa sürücü içi CBM, Wärtsilä UNIC (koruyucu yük azaltma; kestirim gemi dışı). Araştırma: Tampere (Mattila: Beckhoff CX2030'da 1 kHz FTC, gerçek 6,65 t robot; Badihi: rüzgar çiftliği FTC + SCADA FDD, simülasyon), Aalto (FT-MPC, simülasyon), Vaasa + LUT (2026: PV arıza teşhisi → denetleyici MPPT anahtarlama; yazılım benchmark'ı), VTT (Research Notes 2343, 2006; Smart Predictive Maintenance servisi), ABB Oy Helsinki (US7688603B2 sürücü öz-izleme; IEEE TPEL 2025 federated transfer learning ile dönüştürücü izleme). **LUT'un kendi içinde:** (1) grubunuzun Aşama 1 çalışmaları (Canseven vd., IET Power Electronics 2026: PMSM sürücüde 8 invertör arızasının açık veri setinde FDD'si; Sadik & Canseven, IEEE Access 2026: cobot'ta alarm tetiklemeli FDD; Canseven & Sadık, ECAI 2026); (2) Ahola/Ahonen/Tamminen/Lindh sürücü tabanlı sensörsüz izleme geleneği (2003–2021; pompa/fan/rulman; Lindh 2003 tezi; LUT profillerinde üç patent başlığı, numaraları doğrulanamadı); (3) Sopanen/Nutakor/Jastrzebski açık AMB/rulman veri setleri ve transfer öğrenme teşhisi (IEEE Access 2025); (4) Aşama 3'e en yakın LUT çalışması "Optimal control of powertrain and energy balance to recover an equipment fault on a marine vessel" (2021, O. Pyrhönen, Lindh, Peltoniemi vd.) ve J. Pyrhönen/Niemelä'nın hata toleranslı modüler statorlu PM makine tasarımları. LUT'ta teşhis + kestirim + FTC'yi birleştiren yayın veya tez bulunamadı: fikir LUT içinde yeni görünüyor, ancak mevcut LUT teşhis IP'siyle örtüşüyor; buluş sahipliğini erken netleştirin. LUTPub/research.lut.fi bu ortamdan erişilemedi; LUT patentlerini yerelde kontrol edin.

**AB:** Yukarıdaki EU projeleri; Nordik FTC teorisi (DTU Blanke, Aalborg Odgaard/Stoustrup rüzgar türbini FDI/FTC benchmark'ı, Linköping Fault Diagnosis Toolbox — Pi sınıfı hedefe C kodu üretebilen model tabanlı teşhis aracı) güçlü ama kestirimsiz. Fransız/Alman akademik "health-aware control" hattı (CRAN Nancy, UPC, Troyes, fortiss) simülasyon düzeyinde.

---

## 5. Yenilik boşlukları (fikrinizin nerede "yeni" görünebileceği)

1. **Makineden bağımsız entegrasyon:** Üç aşamayı makineden bağımsız biçimde tek bir düşük maliyetli gerçek zamanlı kontrolcüde birleştiren ürün yok; patentler ya alana özel (motor 1999, asansör invertörü, hidroelektrik pompa, EMA, İHA, maglev, rüzgar, gaz türbini, gemi, PV izleyici) ya yalnızca karar mantığı (Xerox) ya da geri çekilmiş (CN118963327A).
2. **Arıza sınıfı + RUL → FTC strateji seçimi:** Çin başvurularında arıza tipine/derecesine göre hazır strateji seçimi istemleniyor, fakat hepsi el ile kodlanmış, varlığa özel ve çoğu beklemede. **Bulunmayan:** ML teşhis sınıfı, şiddet, RUL ve teşhis belirsizliğini birlikte kullanan, makine sınıfına göre parametrelendirilebilen genel bir strateji kütüphanesi ve güvenlik kapılaması (yanlış pozitifte güvenli davranış).
3. **Çok veri setli teşhis modelinin gömülü kestirim ve kontrole bağlanması:** Foundation modeller (UniFault, VibFM, BearLLM, RmGPT) teşhiste kalıyor; patentlerde açık veri setine yalnızca CN120143610A atıf yapıyor (tek rulman seti). "Çok veri setli ön eğitim + kendi düzenek verisiyle ince ayar + gömülü kestirim + FTC" zinciri bulunmadı.
4. **Kendi düzeneklerinizle veri boşluğu doldurma:** Aalto (sentetik + ölçüm) ve Siemens US8868985B2 benzer fikirleri içeriyor; sistematik bir "açık korpusta olmayan arıza modları için düzenek verisi üretip aynı taksonomiye ekleme" yöntemi görülmedi (tek başına patentlenebilir olmayabilir; eğitim verisinin genişliği istem sınırlaması sayılmaz).

---

## 6. Riskler ve uyarılar

**Teknik**

- "Olası tüm arızaları teşhis" iddiası savunulamaz; hiçbir ürün, program veya standart bunu iddia etmiyor. ISO 17359 / FMECA ile makine sınıfı başına **sınırlı bir arıza taksonomisi** tanımlayıp, kapsanan modları ve "bilinmeyen/anomali" sınıfını açıkça belirtmek hem teknik hem IP açısından daha sağlam.
- Alan kayması: açık veri setleri küçük laboratuvar düzeneklerinden, tohumlanmış (EDM) arızalardan ve çoğunlukla rulman titreşiminden oluşuyor.
- Raspberry Pi'de sert gerçek zamanlı FTC: PREEMPT_RT + CPU izolasyonu ile yüzlerce µs; ML çıkarımı aynı SoC'de jitter kaynağı; işlevsel güvenlik sertifikasyonu Pi üzerinde pratikte imkânsıza yakın; koruyucu trip katmanını (API 670 / ISO 20816 mantığı) ML'den bağımsız deterministik bir yolda tutun.
- Sağlık-farkında kontrolün literatürde raporlanan kazanımları mütevazı (EHA örneğinde %2,75–3,22 RUL); ürün vaadini buna göre kurun.

**Fikri mülkiyet (hukuki görüş değildir)**

- Yürürlükte ve en yakın Batı patentleri: **Xerox US11402833B2** (~2040), **GE US12504725B2** (~2044), Siemens US10146611B2 (~2034), GM US11133771B2 (~2039), Omron US10591886B2 (~2038), RTX US10423473B2 (~2037), GE US11193387B2 (~2037), Augury US11853047B2, Equinor US10378515B2, Fischer Block US11808248B2, SWJTU US12500532B1 (ABD, 2025; kenar AI teşhis + FTC), Doosan KR102383775B1.
- **Çin başvuru kümesi (2024–2026):** CN120802909A, CN122386948A, CN120143610A, CN122450188A, CN116594314A, CN118732480A, CN121680485A, CN120278009A, CN120630935A, CN116317827A, CN121484876A. Çoğu beklemede ve yalnızca Çin'de geçerli olacak; ancak hem yenilik değerlendirmesinde önceki teknik sayılırlar hem de Çin pazarı için FTO'yu etkilerler.
- Süresi dolmuş/düşmüş, **serbestçe kullanılabilir fakat yeniliğinizi sınırlayan** önceki teknik: Rockwell US6326758B1 ailesi, GE US6823675B2, GM US8612079B2, Vestas US8577509B2, Boeing US8942882B2, Toyota/UConn US7536277B2, Siemens US9134713B2, Honeywell US9221535B2, Intel US10539932B2, Xerox US6892317B1; geri çekilmiş CN118963327A.
- "Teşhis → kestirim → kestirimin kontrol döngüsüne alınması" yol haritası 2007'den beri standart; patent başvurusu **yönteme** (strateji seçim politikası, belirsizlik kapılama, hibrit RT mimari, taksonomi eşleme) dayanmalıdır.

---

## 7. Aşama 1 için açık erişimli veri seti kataloğu

Hazır kataloglar: VictorBauler/awesome-bearing-dataset (94 set, DOI'lerle), CHAOZHAO-1/Machine-Fault-Dataset (30+ kategori), hustcxl/Rotating-machine-fault-data-set (20 set), PHM-Vibench (20+ set), UniFault Tablo 1, VibFM README, Zhao vd. DL-based-Intelligent-Diagnosis-Benchmark / UDTL, PyPHM, NASA PCoE listesi.

| Veri seti | Makine / bileşen | Arıza tipleri | Not |
|---|---|---|---|
| CWRU | 2 hp motor rulmanı | İç/dış bilezik, bilye (EDM) | Kanonik benchmark |
| Paderborn (KAt) | 425 W PMSM rulmanı | Yapay + gerçek hasar; titreşim + motor akımı 64 kHz | Ticari kullanım izne tabi |
| MFPT | Rulman | İç/dış bilezik + 3 gerçek makine | GitHub (MathWorks) aynası |
| IMS (NASA PCoE) | Rulman, run-to-failure | İç bilezik, makara, dış bilezik | Kestirim benchmark'ı |
| XJTU-SY | Rulman, hızlandırılmış ömür | Aşınma, kafes kırılması | RUL benchmark'ı |
| FEMTO / PRONOSTIA | Rulman, run-to-failure | 17 rulman, 3 koşul | NASA PCoE aynası |
| JNU | Rulman | İç/dış/makara çentik | Lisans belirsiz |
| SEU | Dişli kutusu + rulman | Kırık/eksik diş, çatlak, aşınma | 8 kanal |
| HUST (Huazhong) | Rulman, dişli, motor, aktarma | 9 durum × 11 koşul | RESS 2024 |
| HUST (Hanoi) | 5 rulman tipi | 6 sınıf, bileşik dahil | CC BY 4.0 |
| Ottawa 2018 / UORED-VAFCLS 2023 | Rulman | Değişken hız; kafes dahil; mikrofon | CC BY 4.0 |
| MaFaulDa | SpectraQuest MFS | **Dengesizlik, hizasızlık**, rulman | Mil düzeyi arızalar |
| KAIST | Döner makine, çok modlu | Rulman, hizasızlık, dengesizlik; **3 faz akım** | + run-to-failure |
| USP/UNIOESTE broken rotor bar | Asenkron motor | 1–4 kırık çubuk; akım + gerilim + titreşim | IEEE DataPort |
| ZeMA hidrolik (UCI #447) | Hidrolik düzenek | Soğutucu, valf, pompa kaçağı, akümülatör | Tek yaygın hidrolik set |
| MIMII / DCASE Task 2 | Valf, pompa, fan, ray (ses) | Kontaminasyon, kaçak, dengesizlik | 100 GB |
| MCC5-THU | Dişli kutusu, 12 koşul | Pitting, aşınma, kırılma, çatlak | Data in Brief 2024 |
| DIRG (PoliTo) | Havacılık rulmanı | Çentik + 230 saat dayanım | Zenodo 3559553 |
| UoC | İki kademeli dişli kutusu | 9 pinyon durumu | Figshare |
| NASA PCoE deposu | Turbofan, freze, CNC, batarya, güç elektroniği | Run-to-failure | 21 set |
| PHM Society Data Challenges 2008–2026 | Dişli, helikopter, bilyalı vida vb. | Yıla göre değişir | data.phmsociety.org |
| CARE / Kelmarsh / Penmanshiel / NREL | Rüzgar türbini SCADA | Jeneratör, dişli kutusu, ana rulman öncesi anomaliler | CC BY-SA |
| Bosch CNC Machining | 3 CNC, 15 operasyon | İyi/kötü etiketli titreşim | Makineler arası kayma |
| LUT AMB yüksek hızlı makine setleri (IEEE Access 2025) | Aktif manyetik yatak | Çeşitli | Kurum içi varlık |
| Tennessee Eastman | Kimyasal proses (simülasyon) | 20 arıza | Döner makine dışı |

Gözlem: korpus büyük ölçüde rulman titreşimi; doğal bozunumlu setler az; motor akımlı setler nadir; gerçek saha verisi rüzgar ve CNC. Pompa, kompresör, hidrolik, elektriksel ve proses arızaları için kendi düzenekleriniz zorunlu; bu, önerinizdeki "eksik eğitimler için düzenek kurma" adımını haklı çıkarıyor.

---

## 8. Önerilen sonraki adımlar

1. **Profesyonel yenilik ve FTO araştırması** (patent vekili): Espacenet, PATENTSCOPE, CNIPA, TÜRKPATENT, PRH; CPC G05B23/0283, G05B23/0275, G05B23/0289, G05B23/0262, G05B9/02, G05B13/02–13/042, G01M13/04–13/045, H02P29/028, G06N3/08; anahtar kelimeler "reconfigurable control", "controller adaptation", "health trims", "countermeasure", "standby device", "degraded mode", "life extending control", "health-aware", 故障预诊 / 剩余寿命 / 容错控制 / 自愈控制 / 故障等级, Rekonfiguration, Restlebensdauer, "hata toleranslı kontrol", "kestirimci bakım". Bu taramada engellenen sorguları (Türkçe terimler, başvuran: Lappeenrannan teknillinen yliopisto / LUT-yliopisto, ABB Oy, Vacon, Artesis, Aselsan, Sensemore; Japonca terimler) engellenmeyen bir ağdan tekrarlayın.
2. **İstemleri yönteme odaklayın:** arıza sınıfı × şiddet × RUL × teşhis belirsizliği → strateji kütüphanesi eşlemesi ve güvenlik kapılaması; Linux SBC + RT mikrodenetleyici + bağımsız koruma rölesi hibrit mimarisi; çapraz veri seti taksonomi eşleme ve düzenek verisiyle ince ayar.
3. **Kapsamı dürüstçe sınırlayın:** "tüm arızalar" yerine makine sınıfı başına FMECA tabanlı liste + "bilinmeyen" sınıfı; PHM-Vibench ve HUST DG benchmark'ı ile çapraz makine performansını raporlayın.
4. **LUT IP durumu:** LUT'un sürücü tabanlı izleme patentleri ve güncel dijital ikiz çalışmalarıyla örtüşmeyi ve buluş sahipliğini LUT teknoloji transfer birimiyle erken netleştirin.
5. **Güvenlik ayrımı:** ML teşhisi yalnızca "yumuşak" FTC (derating, sensörsüz geçiş, yük yeniden tahsisi) tetiklesin; sert koruma deterministik eşiklerle ayrı kanalda kalsın.
6. **Savunma amaçlı yayın** alternatifi: entegrasyon mimarisi patentlenemezse, hakemli yayın + açık kaynak sürümü başkalarının aynı entegrasyonu patentlemesini engeller.

---

## 9. Ek tarama sonuçları ve kalan boşluklar

Oturum limiti nedeniyle geciken dört ek tarama tamamlandı:

- **Türkiye/Finlandiya:** Bölüm 4.5'e işlendi. Üç aşamayı birleştiren bölgesel bir sistem yok; en yakın gömülü ürünler Valmet ND9000 (doğrulandı, puan 4) ve Wärtsilä UNIC (düşük güven). Patent ofisleri (TÜRKPATENT, PRH, Espacenet) ve LUTPub bu ortamdan erişilemedi; bu bir **kapsam boşluğu**dur, yokluk kanıtı değildir.
- **Start-up'lar / "self-healing" söylemi (2023–2026):** Bölüm 4.3'e işlendi. İngilizce, Çince, Almanca, Japonca, Korece, Türkçe ve Fince aramalarda otomatik arıza güdümlü kontrol düzeltmesi yapan hiçbir start-up veya maker cihazı bulunamadı; pazar "tespit → teşhis → erken uyarı → iş emri"nde yakınsamış.
- **Raspberry Pi / kenar:** Bölüm 4.4'e işlendi; doğrulanmış gecikme ölçümleri eklendi.
- **Çin/Japon/Kore patentleri ve CPC kesişimleri:** Bölüm 3.2'ye işlendi. Çince tırnaklı sorgular verimli; Japonca sorguların üçü engellendi (Japon kapsamı eksik); Korece'de yalnızca Doosan KR102383775B1 bulundu. CPC G05B23/0283 ∩ "fault tolerant/reconfigur*" sorgusu 260 kayıt verdi; çoğu veri toplama yeniden yapılandırması (Strong Force IoT, Boeing/Honeywell/GE sağlık izleme), kontrol yasası yeniden yapılandırması değil.
- **Doğrulanamayan adaylar (model limiti):** iFactory "self-healing manufacturing" sayfası, Tampere Badihi rüzgar çiftliği FTC, Wärtsilä UNIC, Gebze TÜ robust-adaptif FTC, Anadolu FDI + yeniden yapılandırma, Tampere iMoro FTC mimarisi, Vaasa+LUT PV teşhis + MPPT, "Self-Healing Motor Controller" blog yazısı, Kabaoğlu & Eksin SVM FTC. Bunlar birincil kaynaktan okunmuş fakat ikinci incelemeden geçmemiştir.

---

## Ek A. Taramada kullanılan başlıca birincil kaynaklar

- Google Patents sayfaları (patents.google.com/patent/<numara>/en ve /zh), Google Patents JSON uç noktası (xhr/query), USPTO ppubs PDF'leri, patentimages PDF'leri, Lens.org bibliyografik kayıtları (istem metinleri doğrudan okundu).
- NASA DASHlink: "Prognostics in the Control Loop" (AAAI 2007), "Prognostics-enhanced ACM for Advanced Autonomous Systems" (PHM 2008); NASA PCoE sayfası ve veri deposu; NASA ProgPy GitHub.
- PHM Society makaleleri 1635 (Brown vd. 2009), 1870 (Bole vd. 2010), 4303 (PHM-Vibench), 4912 (VibFM); arXiv 2504.01373 (UniFault), 2409.17604 (RmGPT), 2408.11281 (BearLLM), 2412.01218 (FD-LLM), 2502.15481 (FaultGPT), 2502.03278 (Tampere FTC), 2505.02076 (LLM ajanları), 2604.19275 (Pi 5 RT ölçümleri); OSPERT 2024 (Dewit vd.); Electronics 2021 (Adam vd.).
- Üretici belgeleri: ABB ACS880 firmware kılavuzu, Siemens SINAMICS p0491, Danfoss VLT/VACON CBM, Nidec Unidrive M, Beckhoff TF3600/TF3800, Valmet ND9000 kılavuzu (7ND9071EN), ASELSAN HUMS veri sayfası, TI SSZTD64/ZHCT873, Edge Impulse Pi 4/5, Revolution Pi ve KUNBUS forumu, Monarco, CODESYS mağazası, LinuxCNC, PX4 ve ArduPilot dokümanları, PiLink PL-R4, Mechmine, Industrial Shields, Augury, Tractian, KCF, Novity, Sensemore, Artesis, Imubit, Phaidra, AISing, iFactory sayfaları.
- CORDIS proje raporları: SelSus 609382, MANTIS 662189, SERENA 767561, PROPHESY 766994, Z-BRE4K 768869, UPTIME 768634, AI-PROFICIENT 957391, IMPROVE 678867, RECONFIGURE 314544, ADDSAFE 233815.
- Standart kayıtları (EVS aynası): ISO 13374-1/-2, ISO 13381-1:2025, ISO 17359:2018, ISO 13379-1, ISO 20816-1; MIMOSA OSA-CBM; ECSS-E-ST-70-11C Rev.1; VTT Research Notes 2343.
- LUT profil ve laboratuvar sayfaları, Crossref API (affiliation/author sorguları), Sabancı Ünel grubu sayfası, İTÜ Dergisi, DergiPark, Konecranes, KONE, Wärtsilä, VTT, Valmet, Metso sayfaları.
