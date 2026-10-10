# Hairpin izolasyon malzemeleri ve yöntemleri

Çıplak dikdörtgen bakır hairpin iletkenler için 8 malzeme ailesinde 29 ana malzeme ve 6 uygulama yöntemi ailesi var. Hairpin iletkeninde seri üretimde yalnızca emaye (PEsI+PAI, PAI, korona dirençli PAI, PI) ve ekstrüde PEEK var; epoksi toz yalnızca kaynak uçlarında ve busbar'larda seri. 800 V kampanyası için referans grubu PEsI+PAI, PI ve korona dirençli emaye, 150–200 µm ekstrüde PEEK ve PI/FEP sarılı teldir. Çıplak iletkende ilk laboratuvar adayları PI/FEP bant, FEP/PFA ve PEEK shrink, epoksi toz ve [Parylene HT](https://nrf.aux.eng.ufl.edu/_files/documents/14389.pdf); hepsi eşit kalınlıkta, ≥180 °C'de PDIV ile karşılaştırılmalı.

## Genel bakış

Altı yöntem ailesinden yalnızca emaye ve PEEK ekstrüzyonu hairpin iletken izolasyonunda seri üretimde ([SEI TR 84](https://global-sei.com/technology/tr/bn84/pdf/84-19.pdf); [hpw 2023](https://webdisclosure.com/press-release/hpw-metallwerk-gmbh-etr-hpw-metallwerk-significantly-expands-production-of-peek-high-performance-wires-and-responds-to-high-demand-in-the-electromobility-sector-4JiKH4q2n8L)). Epoksi toz ise yalnızca kaynak uçlarında ve busbar'larda seri ([bdtronic](https://bdtronic.com/en-en/impregnation-applications/stator-coating); [Electronic Design 2026](https://www.electronicdesign.com/55381411)). Diğer kombinasyonlar ticari ürün olarak var ama hairpin'de seri kullanılmıyor ya da patent ve laboratuvar düzeyinde.

| Yöntem ailesi | Süreç varyantları | Uygulanan malzemeler | Hairpin'de durum |
|---|---|---|---|
| 1. Emaye / sıvı kaplama | Kalıp veya keçe ile çok pasolu emaye hattı (2–5 µm/paso, 500–700 °C fırın); laboratuvarda daldırma, silme kalıbı, fırça, sprey | PEsI, PEsI+PAI, PAI, korona dirençli PAI, PI, köpük PI; PU ve polivinil asetal (düşük sınıf) | **Seri** (PEsI+PAI, PAI, PI, korona dirençli PAI) |
| 2. Ekstrüzyon ve eriyik işleme | Çapraz kafa (crosshead) ekstrüzyonu doğrudan Cu veya emaye üzerine; bağ katmanı, ko-ekstrüzyon, harman; enjeksiyon overmolding; eriyik kaynaklama | PEEK, PEKK, PPS, PEI, PPSU/PES, TPI, PET, PA, PFA/FEP | **Seri** yalnızca PEEK; diğerleri patent/lab; overmolding busbar'da |
| 3. Bant / kâğıt sarma | Helisel %50 bindirme (1–2 kat), alın alına (butt-lap), aralıklı (gap-lap), boyuna (kanıtsız); FEP ile ısıyla yapıştırma, PSA veya vernik/VPI; endüstride indüksiyon ön ısıtma + IR veya tuz banyosu sinterleme ([WTM](https://ssr.expometals.net/en/hall/plants/stand/wtm-srl/products/taping-lines-for-polyimide-fep)) | PI/FEP (Kapton, Apical), PI-PSA, PEEK, FEP/PTFE, PEN/PET, PEI filmleri; aramid kâğıt, mika, cam elyaf | Raylı çekiş ve endüstride seri (IEC 60317-44); EV hairpin'de seri kanıt yok |
| 4. Tüp ve ısıyla daralan kılıf | Kaydırmalı tüp; ısıyla daralan tüp (fırın, ısı tabancası); eriyik astarlı çift cidar; spiral sarılı tüp; örgü kılıf | PEEK, PTFE, FEP, PFA, ETFE, PVDF, PET, poliolefin, silikon, FKM; PI ve NKN; cam ve Nomex örgü | EV busbar ve motor uç bağlantılarında seri; hairpin oluğunda yalnızca NKN tüp (üretici beyanı) |
| 5. Toz / sıvı / elektroforez kaplama | Akışkan yatak (sıcak parça), elektrostatik sprey, elektrostatik akışkan yatak; jel kaplama, 2K döküm, UV veya ısıl kürlü daldırma; katodik/anodik elektroforez (ED/EPD) | Epoksi, PA11, PEEK, PFA/FEP/ETFE, PPS tozları; sıvı epoksi, silikon, UV reçine; epoksi, PI, PAI, PEI e-coat | Epoksi toz kaynak uçlarında ve busbar'da **seri**; ED patent/pilot |
| 6. Buhar fazı ve inorganik | Parylene CVD (oda sıcaklığı); plazma polimer; plazma sprey (APS); sol-jel; anodizasyon (yalnızca Al) | Parylene N/C/D/HT/VT-4; plazma polimer; Al2O3; sol-jel hibrit; seramik izolasyonlu tel | Parylene hairpin'de patent düzeyi; diğerleri araştırma veya niş |

## Gereksinimler

800 V SiC beslemeli hairpin sargıda dönüş-dönüş (T/T) PD'siz çalışma hedefi, IEC 60034-18-41 denklemiyle yaklaşık 1,3–2,3 kVpp çıkıyor (hesaplama). Varsayımlar: bakır iletken, 800 V DC bara, SiC evirici, ısıl sınıf 180–220 °C ve olası ATF yağ soğutması. Kısaltmalar: kVp = tepe, kVpp = tepeden tepeye, T/T = dönüş-dönüş, P/G = faz-toprak, P/P = faz-faz.

Kritik gerilim Vc = Vdc · OF · WF · EF_PD · EF_T · EF_Yaşlanma bağıntısıyla bulunuyor ([Lusuardi vd., IEEE Access 2021](https://zenodo.org/records/4562202)). Faktörler:

- OF (aşma faktörü) = motor terminalindeki tepe gerilim / DC bara gerilimi; ölçülmeli.
- WF (sargı faktörü), ölçüm veya simülasyon yoksa: P/P 2; P/G 1,4; T/T 0,7.
- EF_PD = 1,25, çünkü PD söndürme gerilimi PDIV'nin altında.
- EF_T = 1,3 (T/T, P/P) ve 1,1 (P/G, daha soğuk çalıştığı için).
- EF_Yaşlanma = max(1; 1,2 · Ts/Tc) doğrulama testinde; yeterlilik testinde 1, çünkü numune gerçekten yaşlandırılıyor.

800 V hesabında OF 1,2–1,5 varsayıldı ve EF_Yaşlanma 1,2 alındı (Ts = Tc). Değerler Vdc ile doğrusal ölçekleniyor; 900 V maksimum batarya gerilimi yaklaşık %12,5 ekliyor (hesaplama). Hat gerilimi 700 V rms altında kaldığı için motor Type I (PD'siz) kapsamında ([IEC 60034-18-41 önizleme](https://cdn.standards.iteh.ai/samples/18905/b95c2f0bc77e4b658894b3e6629e3aa2/IEC-60034-18-41-2014.pdf); tahmin).

| Gereksinim | Hedef veya tipik değer (birimli) | Hairpin için önemi | İlgili test / standart |
|---|---|---|---|
| PDIV/RPDIV, T/T | 1,31–1,64 kVpp; en kötü durum ≈2,3 kVpp (1,47 p.u., rastgele sargılı motor örneği, [Part III](https://zenodo.org/records/4562202)); hesaplama | Bitişik iletkenler arası hava kaması; terminal gerilimi evirici geriliminin iki katına çıkabilir ([Zhou vd. 2024](https://mdpi-res.com/d_attachment/energies/energies-17-01987/article_deploy/energies-17-01987.pdf)) | [IEC 60034-18-41](https://cdn.standards.iteh.ai/samples/18905/b95c2f0bc77e4b658894b3e6629e3aa2/IEC-60034-18-41-2014.pdf); [IEC 60270:2025](https://www.vde-verlag.de/iec-normen/preview-pdf/info_iec60270%7Bed4.0%7Db.pdf); [IEC TS 61934:2024](https://webstore.iec.ch/en/publication/91294) |
| PDIV, P/G | 2,2–2,8 kVpp (hesaplama) | Oluk astarıyla birlikte değerlendirilmeli; ince veya astarsız varyant da test edilmeli (tahmin) | Aynı; iletken-plaka veya oluk maketi |
| PDIV, P/P | 3,7–4,7 kVpp (hesaplama) | En yüksek gerilim (WF 2); tam statorda AC testi daha muhafazakâr | Aynı |
| Patent PDIV eşikleri (referans) | ≥0,7–1,0 kVp (25 °C); tercih 1,3–2,5 kV; 250 °C'de ≥%50 korunum (patent verisi) | Yalnızca 400 V T/T için yeterli görünüyor (tahmin) | AC 50 Hz, 10 pC ([US9224523B2](https://patents.google.com/patent/US9224523B2/en); [US9324476B2](https://patents.google.com/patent/US9324476B2/en)) |
| Kısa süreli delinme gerilimi | >10 kV (patent hedefi); 250 °C değeri 25 °C değerinin ≥%50'si (patent verisi) | Şekillendirme ve ısıl hasarı gösterir | [IEC 60851-5](https://www.vde-verlag.de/iec-normen/preview-pdf/info_iec60851-5%7Bed4.2%7Db.pdf) Test 13, madde 4.7 (dikdörtgen tel) |
| Isıl sınıf / sıcaklık indeksi | TI ≥220 °C, ısıl şok ≥240 °C (800 V PAI Grade 3 hairpin spesifikasyonu, [He vd. 2025](https://d-nb.info/1376542846/34)) | Normal çalışma 40–160 °C; uç durumda >180 °C | [IEC 60172:2020](https://www.vde-verlag.de/iec-normen/preview-pdf/info_iec60172%7Bed5.0%7Db.pdf); [IEC 60216-1](https://www.vde-verlag.de/iec-normen/preview-pdf/info_iec60216-1%7Bed6.0%7Db.pdf); [IEC 60851-6](https://www.vde-verlag.de/iec-normen/preview-pdf/info_iec60851-6%7Bed3.0%7Db.pdf) Test 9 |
| Şekillendirme / bükme | 180° bükme, 1,0 mm göbek, 5 µm çizik ([US11232885B2](https://patents.google.com/patent/US11232885B2/en)); 90° bükme, 4,0 mm mandrel; burulma ≥30 tur, 100 N | Hairpin kırılmalarının kök nedeni her durumda çatlak ([Mancinelli vd. 2017](https://cris.unibo.it/handle/11585/598944)) | [IEC 60851-3:2023](https://www.vde-verlag.de/iec-normen/preview-pdf/info_iec60851-3%7Bed4.0%7Db.pdf) Test 6/8; JIS C 3216-3; NEMA MW 1000-2012 |
| ATF / yağ ve hidroliz | 150 °C, 500 h, %0,5 su ([US11232885B2](https://patents.google.com/patent/US11232885B2/en)); 150 °C, 1000 h, %0,2 su (yuvarlak tel, [US12100532B2](https://patents.google.com/patent/US12100532B2/en)); oil bomb 150 °C, ~2000 h (patent verisi) | Su ve hava ATF'yi asidik ürünlere çevirip hidrolizi hızlandırır ([Insulating Materials 2024](https://castjournals.cast.org.cn/joweb/jycl/EN/1209927011296997871)) | [IEC 60851-4](https://www.vde-verlag.de/iec-normen/preview-pdf/info_iec60851-4%7Bed3.0%7Db.pdf) Test 20; ASTM D1676-03 |
| Soyma / kaynak | Kalıntı <1 µm, floresan <9 RFU (üretici beyanı, [Novanta](https://novanta.com/precision-manufacturing/resources/whitepapers/unlocking-efficiency-in-electric-motors-the-power-of-hairpin-stripping/)); soyma boyu 4–7 mm (patent verisi) | Kaynak ≥950 °C; PI özellikleri ≥500 °C'de değişebilir ([US12068636B2](https://patents.google.com/patent/US12068636B2/en)); PEEK 4 cm²/s ile PAI'den (ort. 7, en çok 13 cm²/s) yavaş soyuluyor ([TRUMPF 2021](https://chargedevs.com/wp-content/uploads/2021/04/TRUMPF_Whitepaper_Laser-stripping_welding_EV.pdf)) | Standart yok; FTIR/ATR, SEM, soyulma (peel) testi |
| Oluk doluluk | Hairpin doluluk %70'e kadar ([Zhou vd. 2024](https://mdpi-res.com/d_attachment/energies/energies-17-01987/article_deploy/energies-17-01987.pdf)); 3,5 × 2,0 mm'de Cu payı 40 µm'de %94,0, 200 µm'de %74,8 (hesaplama) | Kalın izolasyon bakır kesitini ve verimi düşürür | [IEC 60851-2](https://www.vde-verlag.de/iec-normen/preview-pdf/info_iec60851-2%7Bed3.2%7Db.pdf) Test 4 (boyut, köşe) |
| Kalınlık eşitliği / köşe | Köşe-yüzey farkı ≤%20 ([US9330817B2](https://patents.google.com/patent/US9330817B2/en)); eş merkezlilik 1,1–1,5 ([US9324476B2](https://patents.google.com/patent/US9324476B2/en)); patent verisi | En ince ve en eğri bölge PDIV ile delinmeyi belirler | IEC 60851-2 Test 4 ve kesit mikroskopisi |
| Nem ve basınç | RH ve rakım için ek EF önerisi; PDIV minimumu 50–70 mbar ([Elorza Azpiazu vd. 2023](https://mdpi-res.com/d_attachment/applsci/applsci-13-02417/article_deploy/applsci-13-02417.pdf)) | Nem PDIV'yi iki yönde kaydırır | [IEC 60034-18-41 AMD1](https://cdn.standards.iteh.ai/samples/23527/a1d9bbea464c4242a53f644c696783a0/IEC-60034-18-41-2014-AMD1-2019.pdf) |

## Malzeme × yöntem matrisi

29 malzeme × 8 yöntem matrisinde hairpin iletkeninde seri olan kombinasyon sayısı beş: dört emaye türü ve PEEK ekstrüzyonu. Epoksi toz (kaynak ucu, busbar) ve poliolefin shrink (busbar) yalnızca benzer EV kullanımında seri.

| Malzeme | Emaye/sıvı kaplama | Ekstrüzyon | Film bant sarma | Tüp | Isıyla daralan (shrink) | Toz kaplama | Elektroforez (e-coat) | CVD/buhar |
|---|---|---|---|---|---|---|---|---|
| PEsI / PEsI+PAI (çift kat) | S | – | – | – | – | – | – | – |
| PAI | S | – | – | – | – | – | L | – |
| Korona dirençli (nano dolgulu) emaye | S | – | – | – | – | – | – | – |
| Köpük / düşük εr emaye (mikro hücreli PI) | L | – | – | – | – | – | – | – |
| PI (aromatik poliimid) | S | – | T | T | – | – | T | – |
| PEEK | – | S | L | T | T | T | – | – |
| PEKK / LM-PAEK | – | L | – | – | – | – | – | – |
| PPS | – | L | L | – | – | T | – | – |
| PEI | L | L | L | – | – | – | L | – |
| PPSU / PSU / PES | L | L | – | – | – | – | – | – |
| TPI (termoplastik PI) | – | T | – | – | – | L | – | – |
| PA (PA11, PA66) | – | T | L | – | – | T | – | – |
| PET / PEN | – | L | T | T | T | – | – | – |
| LCP | – | – | – | – | – | – | – | – |
| Poliolefin | – | – | – | – | S | – | – | – |
| PTFE | – | T | T | T | T | – | – | – |
| FEP | – | T | T | T | T | T | – | – |
| PFA | – | T | L | T | T | T | – | – |
| ETFE | – | – | L | T | T | T | – | – |
| PVDF | – | – | – | T | T | – | – | – |
| FKM (Viton) | – | – | – | – | T | – | – | – |
| Epoksi | T | – | – | – | – | S | T | – |
| Silikon | T | – | – | – | T | – | – | – |
| Parylene | – | – | – | – | – | – | – | T |
| Plazma polimer | – | – | – | – | – | – | – | L |
| Aramid kâğıt (Nomex) | – | – | T | T | – | – | – | – |
| Mika | – | – | T | – | – | – | – | – |
| Cam elyaf | – | – | T | T | – | – | – | – |
| İnorganik / seramik (alümina, sol-jel, anodik oksit) | L | – | – | – | – | L | – | – |

S: seri (hairpin veya benzer EV kullanımı); T: ticari, hairpin'de seri değil; L: laboratuvar/patent; –: uygulanamaz, uygun değil veya kanıt yok.

## Emaye kaplamalar

Emaye hairpin'de en olgun yöntem: PEsI+PAI (sınıf 200), PAI (220) ve PI (240) seri üretimde, ama emaye ~120–130 µm ile sınırlı ([Bekaert](https://www.linkedin.com/pulse/enamel-vs-peek-why-wire-coating-matters-high-voltage-vermeersch); [Victrex](https://cdn.victrex.com/-/media/downloads/literature/ja/victrex_auto_ebook_wirecoatings_04_2024.pdf)). Kesik çubuğa emaye için yayımlanmış laboratuvar protokolü yok; referanslar hazır tel olarak tedarik edilmeli.

| Malzeme – yöntem | Tipik kalınlık (µm) | Sınıf / sürekli sıcaklık (°C) | Olgunluk | Bare numuneye uygulanabilirlik | Artılar / riskler | Örnek ürün / kaynak |
|---|---|---|---|---|---|---|
| THEIC-PEsI tek kat — emaye hattı | — | 180 ([IEC 60317-28](https://webstore.iec.ch/en/publication/96016)); 200 ([IEC 60317-82](https://www.boutique.afnor.org/en-gb/standard/iec-60317822020/specifications-for-particular-types-of-winding-wires-part-82-polyesterimide/xs137256/248845)) | Seri | İyi (krezilik çözücü, düşük kür) | + düşük maliyet, "düşük εr" (nitel); – ısıl şok ≤180 °C | [Axalta THEIC-PEsI tabanları](https://www.axalta.com/electricalinsulation_global/en_US/wire-enamels/what-are-wire-enamels.html) |
| PEsI (veya PE) taban + PAI üst kat — emaye hattı | — | 200 ([IEC 60317-29, 1990](https://webstore.iec.ch/publication/1387); NEMA MW 36) | Seri; Çin EV korona dirençli telinin ana tipi (patent verisi) | Orta (iki emaye, iki kür penceresi) | – ATF çevriminde korona ömrü 36 h 52 dk → 3 h 18 dk, delinme 15,39 → 5,53 kV (patent verisi) | [Essex GP/MR-200](https://www.electro-wind.com/superior-essex-130-312-heavy-gp-mr-200-mw-36-magnet-wire-24in); [US12159731B2](https://patents.google.com/patent/US12159731B2/en) |
| PAI tek kat — emaye hattı | 40–80 (400 V BEV); maks. ~120–130 | 220 ([IEC 60317-58](https://assets.vde-verlag.de/iec-normen/preview-pdf/info_iec60317-58%7Bed1.0%7Db.pdf)); Victrex 180 diyor (çelişkili) | Seri (Sumitomo AIW, Japon HEV/EV) | Orta (NMP çözücü, yüksek kür sıcaklığı) | + aşınma ve yağ dayanımı; – εr 4,3–4,6, su emme %4,5 | [Bekaert Ampact sunumu](https://www.bekaert.com/content/dam/corporate/en/events/wire-d%C3%BCsseldorf/docs-mobility/Ampact%20copper%20magnet%20wire%20for%20e-motors.pdf); Hitachi Chemical HI-406 ([US10418151B2](https://patents.google.com/patent/US10418151B2/en)) |
| Korona dirençli PAI (TiO2, SiO2, Al2O3 nano dolgu) — tek, taban, ara veya üst kat | — | 200 ([Voltatex 8536](https://www.axalta.com/electricalinsulation_global/en_US/wire-enamels/product-catalog/Voltatex-8536.html)) | Seri | Orta (dolgu çökmesi, kalıp aşınması) | + PDIV üstünde ömür ~3× ile ~43× (patent verisi); – %10 uzamada ömrün <%20'si kalıyor ([EMCA 2017](https://opaj.napstic.cn/periodicalArticle/0120171002033563)) | [Axalta Voltron 7700/8500](https://www.axalta.com/electricalinsulation_global/en_US/wire-enamels/what-are-wire-enamels.html); [ELANTAS CORONA-PROTECT, ELAN-SHIELD](https://elantas.com/tongling/products/wire-enamels/polyamideimide-enamels.html); [US6337442B1](https://patents.google.com/patent/US6337442B1/en) |
| Aromatik PI — emaye (poliamik asit, ~500 °C kür) | 60 | 240 ([IEC 60317-47](https://webstore.iec.ch/en/publication/95918)) | Seri (Sumitomo PIW) | Zor (imidizasyon, su çıkışı) | + εr 3,0, uzama ~%80, su %3,0; – maliyet, kür derecesi ölçümü zor ([SEI TR 90](https://global-sei.com/technology/tr/bn90/pdf/E90-05.pdf)) | [Sumitomo PIW](https://global-sei.com/technology/tr/bn84/pdf/84-19.pdf); [ELANTAS PI](https://www.elantas.com/en-br/stories/wire-enamels-pi/) |
| Mikro hücreli (köpük) PI — emaye hattı | 44–60 | PI tabanlı | Geliştirme (2019–2020); patent | Elle uygulanamaz | + εr 2,2 (%30 hücre); 60 µm'de PDIV 1230 → 1440 Vp; – kapalı hücre kontrolü, ATF verisi yok | [Sumitomo, SEI TR 88](https://global-sei.com/technology/tr/bn88/pdf/E88-10.pdf); [SEI TR 90](https://global-sei.com/technology/tr/bn90/pdf/E90-04.pdf); [US10418151B2](https://patents.google.com/patent/US10418151B2/en) |
| Emaye — laboratuvar daldırma veya elle çekilen silme kalıbı (kesik çubuk) | 3–5 / kat | malzemeye bağlı | Lab (protokol yayımlanmamış) | Kısmen (0,3–1 m çubuk, ürüne özel kalıp) | – köşe incelmesi, kalın katta kabarcık, >20 pasoda yapışma düşüşü | [US9330817B2](https://patents.google.com/patent/US9330817B2/en); [US3850773A (1974)](https://patents.google.com/patent/US3850773A/en) |
| PU, polyester, polivinil asetal — emaye (referans) | — | PU 155–180; polivinil asetal 120 | Seri (düşük sınıf) | — | Çekiş hairpin'i için uygun değil | [Leone 2022](https://pubblicazioni.unicam.it/bitstream/11581/483506/1/30_05_2022%20PhD%20Thesis%20Ezio%20Leone.pdf); [IEC 60317-80](https://webstore.iec.ch/en/publication/60783) |

- Köşe incelmesi: 20 µm hedefte kalıp emayesi köşede 12–13 µm, düz yüzde 15–26 µm verdi ([US9330817B2](https://patents.google.com/patent/US9330817B2/en), patent verisi). Çıkıntılı kalıp köşeyi 23–24 µm'ye çıkarıp delinmeyi 3,26 kV'tan 4,71 kV'a yükseltti.
- Şekillendirme: PI emayeli hairpin'lerde PDIV ve PDEV düz çubuğa yakın kaldı, delinme gerilimi ise belirgin düştü ([Kettering 2014](https://researchprofiles.kettering.edu/en/publications/electrical-discharge-in-enamel-insulated-hairpin-copper-conductor/); sayısal veri yok).
- NMP: REACH Ek XVII madde 71 tel kaplamada 9 Mayıs 2024'ten beri geçerli; işçi DNEL'i soluma için 14,4 mg/m³ ([EUR-Lex 2018/588](https://eur-lex.europa.eu/eli/reg/2018/588/oj)). Laboratuvar emayesi çeker ocakta uygulanmalı.

## PAEK ailesi (PEEK, PEKK, LM-PAEK)

PEEK, emaye dışında hairpin iletkeninde seri üretilen tek malzeme; emaye+PEEK 25 °C'de 200 µm toplamda 2,2 kVp PDIV verdi ([US10109389B2](https://patents.google.com/patent/US10109389B2/en), patent verisi). Ekstrüzyon sürekli hat gerektirdiğinden kesik çubuğa yalnızca PEEK tüp, shrink, film bant, toz ve overmolding uygulanabiliyor.

| Malzeme – yöntem | Tipik kalınlık (µm) | Sınıf / sürekli sıcaklık (°C) | Olgunluk | Bare numuneye uygulanabilirlik | Artılar / riskler | Örnek ürün / kaynak |
|---|---|---|---|---|---|---|
| PEEK — ekstrüzyon doğrudan Cu üzerine (tek katman) | 80–300; YG motorda ≤180 | 220 (Victrex web) / 240 (tahmini RTI) / 260 (polimer); çelişkili | Seri | Hayır (sürekli hat; bobin hâlinde fason) | + çözücüsüz, tek paso; – Cu'ya yapışma, kristallik; 2012 tasarımı sarım+ısıtmada başarısız görünüyor (doğrulanmalı, [US9514863B2](https://patents.google.com/patent/US9514863B2/en)) | [Bekaert Ampact](https://www.bekaert.com/content/dam/corporate/en/events/wire-d%C3%BCsseldorf/docs-mobility/Ampact%20copper%20magnet%20wire%20for%20e-motors.pdf); [Syensqo KT-857](https://www.compositesworld.com/products/peek-for-monolayer-e-motor-magnet-wire-insulation); [Mavel 2025](https://magneticsmag.com/mavel-powertrain-selects-syensqo-materials-for-high-performance-ev-motor-project/); [Victrex XPI](https://www.victrex.com/en/emotor-solutions) |
| PEEK — emaye (PAI/PI 20–60 µm) üzerine ekstrüzyon, ± PEI/PPSU bağ katmanı 5–10 µm | 85–280 toplam | 220 sürekli (patent); "sabit 240" (üretici beyanı) | Seri (HVWW; [Magnetics Magazine](https://magneticsmag.com/sumitomo-advances-development-manufacturing-of-its-rectangular-magnet-wire-for-evs/) PEEK diyor, basın bülteni polimeri açıklamıyor) | Hayır | + µm başına en yüksek belgelenmiş PDIV; – yapışma penceresi: aşırı yapışma çatlağı iletkene taşıyor | [Essex Furukawa HVWW 2021](https://kyodonewsprwire.jp/index.php/release/202108138772); [US9324476B2](https://patents.google.com/patent/US9324476B2/en); [US10109389B2](https://patents.google.com/patent/US10109389B2/en) |
| PEEK — ko-ekstrüzyon (PEI/PEEK, PPSU/PEEK) veya harman tek katman | 112–280 | dış PEEK ≥240 (patent) | Patent (Essex, 2020) | Hayır | + PEI/PEEK 280 µm'de 2758 V; – ko-ekstrüzyon kafası gerekir | [US12278026B2](https://patents.google.com/patent/US12278026B2/en); [US10037833B2](https://patents.google.com/patent/US10037833B2/en) |
| PEEK — tüp (yuvarlak, kaydırmalı) | cidar 38–1590 | 250–260 | Ticari (hairpin'de yok) | Evet, ama 4 × 2 mm çubukta ~1,1 mm hava (hesaplama) | – PD testine uygun değil; dikdörtgen profil özel kalıp ister | [Optinova PEEK tüp](https://optinova.com/peek-tubing/); [Zeus PEEK ekstrüzyon](https://www.zeusinc.com/wp-content/uploads/2024/06/PEEK-Extrusions-V2R2.pdf); [Zeus özel profil](https://zeusinc.com/products/tubing/custom-profiles) |
| PEEK — ısıyla daralan (PEEKshrink) | 76–457 (standart 127–229) | 260 | Ticari (hairpin'de yayımlanmış kullanım yok) | Evet, zor: 343–385 °C, oran ≤1,4:1; 4 × 2 mm örneğinde giriş payı 0,26 mm (hesaplama) | – erime noktasına yakın süreç, Cu oksitlenmesi; εr 23 °C'de 3,2, 200 °C'de 4,5 | [Zeus PEEKshrink](https://www.zeusinc.com/products/heat-shrinkable-tubing/peekshrink/); [Zeus V1R4 2024](https://www.zeusinc.com/wp-content/uploads/2024/06/PEEKshrink-Heat-Shrink-V1R4.pdf); [Optinova 2022](https://optinova.com/app/uploads/2022/09/optinova-peek-tubing.pdf) |
| PEEK — düşük sıcaklık shrink | 50–300 (ID 4,5–20 mm) | — | Geliştirme | Numune talebiyle | + 150 °C'de büzülmeye başlıyor; – ≤%25 büzülme, veriler yalnızca görselde | [Gunze PEEK tüp](https://www.gunze.co.jp/e/epd/products/peek/) |
| PEEK — film bant (APTIV) | film 8–750 (pratik 25) | 250 üst çalışma (distribütör) | Lab | Orta (kanıtlı bağlama yolu yok) | + uzama >%150, su %0,04; – füzyon, yapışkan veya vernik gerekli | [Victrex APTIV 1000](https://www.victrex.com/-/media/ul-datasheet/aptiv-films-1000-series.pdf); [Goodfellow APTIV](https://www.goodfellow.com/uk/victrex-aptiv-1000-peek-film-group) |
| PEEK — toz (VICOTE, elektrostatik sprey) | <100–500 | 260 (UL 746B RTI) | Ticari (hairpin'de yok) | Düşük–orta (450 °C fırın, kumlama) | – Cu oksitlenmesi ve tavlanma; dielektrik verisi yok | [Victrex VICOTE 700](https://www.victrex.com/en/downloads/datasheets/vicote-700-series) |
| PEEK, PPS, PPA, PA11 — enjeksiyon overmolding | ölçülmemiş (kalın) | reçineye bağlı | Busbar'da seri; hairpin bacağında yok | Evet (kesik segment) | – ince, düzgün cidar yok; sonradan şekillendirilemez | [Arkema EV](https://hpp.arkema.com/en/markets-and-applications/automotive-and-transportation/electric-vehicles); [e-Mobility Engineering](https://www.emobility-engineering.com/?p=16587) |
| PEKK — ekstrüzyon (Kepstan 6000/7000) | 69–102 (1 mm yuvarlak tel); tercih 50–250 | — | Patent / lab | Hayır | + 330–350 °C'de işleniyor, amorf hâlde sarılıp tavlanabiliyor; – dikdörtgen tel verisi yok | [US12148548B2](https://patents.google.com/patent/US12148548B2/en); [Arkema Kepstan](https://hpp.arkema.com/en/product-families/kepstan-pekk-polymers/wire-coatings/) |
| LM-PAEK, PEK, PEKEKK | — | — | Kanıt yok (yalnızca patent listesi) | — | Tel verisi bulunamadı | [US10037833B2](https://patents.google.com/patent/US10037833B2/en) |

- Kalınlık–PDIV: 25 °C'de emaye+PEEK yaklaşık 10–11 Vp/µm, emaye tek başına yaklaşık 8 Vp/µm artıyor (hesaplama). ≥1,5 kVp için ~130–150 µm toplam gerekiyor (hesaplama); emaye tek başına 60–100 µm'de 0,82–1,14 kVp verdi ([US10109389B2](https://patents.google.com/patent/US10109389B2/en)).
- Üst kalınlık sınırı: 220 µm ekstrüzyon ve PAI 40 + PEEK 185–212 µm yapı sarım+ısıtma sonrası delinmede başarısız ([US9514863B2](https://patents.google.com/patent/US9514863B2/en); [US9224523B2](https://patents.google.com/patent/US9224523B2/en); patent verisi).
- Sıcaklık: PEEK Tg 143 °C; εr 25 °C'de 3,1, 250 °C'de 4,7 ([US9224523B2](https://patents.google.com/patent/US9224523B2/en)). 76 µm cidarın dayanımı 240 °C'de 1443 V/mil'e düşüyor ([Zeus PEEK tel](https://www.zeusinc.com/wp-content/uploads/2026/07/PEEK-Insulated-Wire-V2R5.pdf), meta veri 2020); PDIV ≥180 °C'de ölçülmeli.

## Poliimid (PI)

PI üç olgun formda var: emaye (sınıf 240), FEP ile ısıyla yapıştırılan bant ([IEC 60317-44](https://webstore.iec.ch/publication/1424)) ve elektroforez; termoset PI daraltılamıyor. 800 V için en güçlü sarma adayı korona dirençli PI/FEP bant: [Kapton ECRC](https://www.qnityelectronics.com/blogs/kapton-polyimide-film-addresses-impact-of-higher-switching-frequency-and-faster-voltage-rise.html), FN'e göre ortalama ~8 kat ömür verdi (üretici beyanı).

| Malzeme – yöntem | Tipik kalınlık (µm) | Sınıf / sürekli sıcaklık (°C) | Olgunluk | Bare numuneye uygulanabilirlik | Artılar / riskler | Örnek ürün / kaynak |
|---|---|---|---|---|---|---|
| PI — emaye (ayrıntı Emaye bölümünde) | 60 | 240 | Seri | Zor | + εr 3,0, uzama ~%80 | [Sumitomo PIW](https://global-sei.com/technology/tr/bn84/pdf/84-19.pdf) |
| PI/FEP ısıyla yapıştırılan bant, helisel %50, 1–2 kat (FN, FWN, FWR, PRN) | bant 30–64; yapı 120–300 (çift taraflı) | IEC 240 (ABD 220); UL RTI 240 el. / 200 mek. | Ticari; raylı, endüstri, rüzgâr, ESP'de seri; EV hairpin'de seri kanıt yok | Orta (elle sarma kolay; 280–350 °C yapıştırma fikstürü) | + εr 2,6–3,1, FEP–Cu soyulma ≥300 g/in; – bindirme boşlukları, büküm ve U-bükümde kalkma | [Kapton FWN](https://www.qnityelectronics.com/kapton-fwn.html); [Kapton FWR](https://www.qnityelectronics.com/kapton-fwr.html); [Kapton PRN](https://www.qnityelectronics.com/kapton-prn.html); [DuPont bülten (2014)](https://ca.electro-wind.com/web-files/DuPont%5CLiterature%5CKapton-motor-magnet-wire-bulletin.pdf); [Kapton spesifikasyon (2012)](https://ca.electro-wind.com/web-files/DuPont%5CLiterature%5CKapton-general-specs-2.pdf) |
| Korona dirençli PI/FEP bant (150FCRC019, ECRC, Apical CR) | bant 38; %53 bindirmede 210 (çift taraflı) | RTI 240 (100CRC); FCRC sayfasında 130 (çelişkili, UL iQ'da doğrulanmalı) | Ticari; inverter beslemeli raylı çekişte seri; ECRC EV için pazarlanıyor | Orta | + CR ömrü >100 000 h, HN 200 h (20 kV/mm; üretici beyanı, 2007); – ECRC belgeleri erişime kapalı | [Kapton FCRC](https://www.qnityelectronics.com/kapton-fcrc.html); [Kapton ECRC 2020](https://www.qnityelectronics.com/blogs/kapton-polyimide-film-addresses-impact-of-higher-switching-frequency-and-faster-voltage-rise.html); [CRRC 2023](https://castjournals.cast.org.cn/joweb/jycl/EN/PDF/10.16790/j.cnki.1009-9239.im.2023.02.011); [P. Leo 1K063CR (2007)](https://pleo.com/wp-content/uploads/2024/02/1K063CR_EN.pdf) |
| PI + silikon PSA bant, elle helisel | bant 63–76; %50'de ~250–300 | 180 (3M 92); 220 (Leo CR) | Ticari (bobin sarma; tel standardı yok) | Yüksek (en basit) | + ısı adımı yok; – kalın yapışkan, düşük sınıf, ATF etkisi bilinmiyor | [3M 92 (2013)](https://ca.electro-wind.com/web-files/3M%5CDatasheets%5C3M92.pdf); [CMC Kapton CR bantları](https://www.cmc.de/en/teilentladungsfeste-klebebaender) |
| PI film, yapışkansız sarma + vernik (Kapton HN/CRC/MT, Upilex-S, Apical) | film 7,5–127 | HN UL 220–240 el.; Upilex 290 (20 000 h, çekme) | Lab | Orta | – Upilex uzama %40, modül 9,1 GPa (büküme hassas); HN sıcak suda hidrolize uğruyor | [Kapton özellikleri (2000)](https://www.electro-wind.com/web-files/DuPont%5CLiterature%5CKapton-summary-of-properties.pdf); [Kapton CRC](https://www.qnityelectronics.com/kapton-crc.html); [Kapton MT](https://www.qnityelectronics.com/kapton-mt.html); [UBE Upilex-S 2022](https://ube.com/upilex/catalog/pdf/upilex_s_e.pdf); [Apical 50AV](https://polymerfilms.com/wp-content/uploads/2024/09/Apical50AV-FILM.pdf) |
| PI — spiral sarılı tüp (Kapton, Nomex/Kapton/Nomex) | 130–190 (NKN) | 220 | Ticari; hairpin için pazarlanıyor (üretici beyanı) | Orta (dikdörtgen mandrelde üretilirse) | – spiral dikiş ve oturma boşluğu; PD iddiası bağımsız doğrulanmamış | [Politubes EVtubes, CWIEME 2023](https://berlin.cwiemeevents.com/articles/e-motor-400---800v-insulation-thermal-managem); [Pleo tüp/kılıf 2024](https://pleo.com/wp-content/uploads/2024/02/Tube-Sleeve.pdf) |
| PI — film-cast tüp | cidar 10–254; ID ≤2,3 mm | 220 (20 000 h) | Ticari; hairpin kesitine uygun değil | Hayır | – ısıyla daralmıyor, hairpin kesitine sığmıyor | [MicroLumen](https://www.microlumen.com/medical-tubing/polyimide/); [Zeus PI tüp](https://www.zeusinc.com/wp-content/uploads/2026/07/Polyimide-Tubing-V2R9.pdf); [Nordson PI](https://interventional-solutions.nordsonmedical.com/files/interventional-solutions-nordsonmedical-com/Literature/Sell%20Sheets/MAR-Polyimide-DS-01-DIGITAL.pdf) |
| PI — elektroforez (anyonik veya katyonik PI e-coat) | 5–100 | Tg ≥200; >250 (Honey Kasei) | Ticari (Japonya'da busbar) | Orta (tedarikçi banyosu, 200–300 °C pişirme) | + 2,5 mm kare Cu'da kenar kaplama >%80; 220 °C × 500 h sonra >10 kV; – ince, köpürme | [Toyochem PI ED](https://www.artiencegroup.com/en/products/metal-coatings/electrocoating/polyimide.html); [Honey Kasei](https://pr.mono.ipros.com/en/honny/product/detail/2001642863/); [Shimizu Elecoat PI](https://mono.ipros.com/en/cg2/Electrochemical%20Paint) |

- Yapı aritmetiği: bindirme oranı p için katman sayısı 1/(1−p); %50'de 38 µm bant ~0,15 mm, iki kat ~0,30 mm çift taraflı yapı veriyor (hesaplama). CRRC'nin ölçtüğü yapı 0,21 mm, basit hesap 0,152 mm.
- Hidroliz: Kapton HN sıcak suda dayanım kaybediyor; ATF testinde WR veya FWR çekirdekli dereceler seçilmeli ([DuPont bülten (2014)](https://ca.electro-wind.com/web-files/DuPont%5CLiterature%5CKapton-motor-magnet-wire-bulletin.pdf)).
- Çelişki: TRUMPF "PAI+FEP"i (PI folyolu PAI) yaygın hairpin kaplamaları arasında sayıyor ([TRUMPF 2021](https://chargedevs.com/wp-content/uploads/2021/04/TRUMPF_Whitepaper_Laser-stripping_welding_EV.pdf)); seri EV hairpin kullanımı başka kaynakta doğrulanamadı.

## Diğer termoplastikler (PPS, PEI, PPSU, PA, LCP, TPI)

PPS, PEI, PPSU ve TPI emaye üzerine ekstrüde edildi ve patentlerde PEEK'e yakın PDIV verdi; hiçbiri hairpin'de ticari ürün değil. Aralarındaki seçim oda sıcaklığı PDIV'sine değil, ısıl sınıf, sıcak PDIV, ATF ve şekillendirme davranışına dayanmalı.

| Malzeme – yöntem | Tipik kalınlık (µm) | Sınıf / sürekli sıcaklık (°C) | Olgunluk | Bare numuneye uygulanabilirlik | Artılar / riskler | Örnek ürün / kaynak |
|---|---|---|---|---|---|---|
| PPS — emaye üzerine ekstrüzyon | PPS 45–195; toplam 125–275 | Tm 278–285; 300 °C × 168 h testinde başarısız | Patent / lab | Hayır | + 125 µm'de 1400 Vp, 275 µm'de 2950 Vp; – UV'ye hassas, yapışkan veya yüzey işlemi gerekli | [US10109389B2](https://patents.google.com/patent/US10109389B2/en); [US8847075B2](https://patents.google.com/patent/US8847075B2/en); [US9514863B2](https://patents.google.com/patent/US9514863B2/en); [Hi-ECOWIRE](https://vb.nweurope.eu/media/13371/hi-ecowire_technical_sheet_polymer_extrusion.pdf) |
| PPS — film bant | — | — | Lab (patent listesi) | Orta | – Torelina film verisi doğrulanamadı | [US12665103B2](https://patents.google.com/patent/US12665103B2/en) |
| PPS — toz (Ryton M2000 FP) | — | ≤200 | Ticari (petrol-gaz) | Orta | – dielektrik veri yok | [Ryton PPS, Interplas 2025](https://interplasinsights.com/plastics-materials/latest-plastics-materials-news/syensqo-ryton-polyphenylene-sulfide-coating-grade/) |
| PEI — tek katman, bağ katmanı veya ko-ekstrüzyon iç katmanı | tek 324; bağ 5–11 | Tg 215–225 | Patent / lab | Hayır | + yapışkan; ULTEM 1000 324 µm'de 1513 V, 16 kV; – Tg sınırı, sıcak ATF'de çatlama riski (tahmin) | [US12278026B2](https://patents.google.com/patent/US12278026B2/en); [US9514863B2](https://patents.google.com/patent/US9514863B2/en) |
| PEI — film bant (ULTEM 1000B) | 25–50 | Tg 217 | Lab | Yüksek (ısıyla yapıştırılabilir) | + termoplastik bağlayıcı katman adayı; – εr verilmemiş | [SABIC ULTEM 1000B (2017)](https://polymerfilms.com/wp-content/uploads/2023/06/Polymerfilms-SABIC-ultem%E2%84%A2-1000b-natural-25-%C2%B5m-%E2%80%9350-%C2%B5m-film-datasheet.pdf) |
| PEI — elektroforetik biriktirme (kuaterner PEI) | 2–6 | 250 °C'de yeniden imidizasyon | Araştırma | Düşük | + ~5 µm film 50 V'a dayandı (~10 kV/mm); – hairpin veya PD testi yok | [KTH/Scania, RSC Adv. 2021](https://pmc.ncbi.nlm.nih.gov/articles/PMC9042725/) |
| PPSU / PSU / PES — ekstrüzyon, ko-ekstrüzyon, bağ katmanı | 112–354 | PPSU "200 sınıfı"; Tg ≈220 | Patent / lab | Hayır | + yüksek hidroliz direnci; PPSU 354 µm'de 1764 V; – PEEK ile arayüz yapışması | [US12278026B2](https://patents.google.com/patent/US12278026B2/en); [Hi-ECOWIRE](https://vb.nweurope.eu/media/13371/hi-ecowire_technical_sheet_polymer_extrusion.pdf); [MFL denemeleri](https://www.wirecable.in/?p=32084) |
| PPSU veya TFE kopolimeri — yalnızca kenar ve omuzlara ekstrüzyon | — | RADEL R 180; ACUDEL 220 | Patent (2004, süresi dolmuş) | Hayır | + ~%75 daha az polimer | [US7125604B2](https://patents.google.com/patent/US7125604B2/en) |
| TPI (AURUM) — ekstrüzyon | 105 (patent) | Tg 245; "150 °C'nin çok üstü" (üretici beyanı) | Ticari (havacılık teli); hairpin'de yok | Hayır | + 105 µm'de 1460 Vp, 22,4 kV; "PEEK'ten %30–40 ince" (üretici beyanı); – az veri | [Mitsui AURUM](https://us.mitsuichemicals.com/service/product/aurum.htm); [WIRE 2024](https://umformtechnik.net/wire/Content/Reports/Polyimide-coated-magnet-wires); [US8847075B2](https://patents.google.com/patent/US8847075B2/en) |
| TPI — toz kaplama | — | — | Lab (busbar çalışması) | Orta | – veri yok | [WIRE 2024](https://umformtechnik.net/wire/Content/Reports/Polyimide-coated-magnet-wires) |
| PA (PA11, PA66, PPA) — ekstrüzyon, overmolding, akışkan yatak toz | PA66 28 (patent); PA11 tek daldırmada ≤500 | PA11 Tm 186 | Ticari (EV busbar) | Yüksek (PA11 toz) | + CTI >600 V, astarsız; – sınıf 180–220 için uygun değil; PAI 25 + PA66 28 µm PDIV'de başarısız | [Arkema PA11 toz](https://hpp.arkema.com/en/markets-and-applications/powder-metal-coatings/electrical-applications-and-battery-components/); [Rilsan T Blue 7444 MAC](https://hpp.arkema.com/en/products/product/f/spa_hpp_RilsanPowders/p/rilsan-pa11-t-blue-7444-mac/); [US9224523B2](https://patents.google.com/patent/US9224523B2/en) |
| PET / PEN — ekstrüzyon, film bant, spiral tüp, shrink | PET ekstr. 103; film 12–500; shrink 2,5–100 | PEN RTI 180 el. / 160 mek.; PET shrink 135 | Patent (ekstr.); ticari (film, tüp, shrink) | Yüksek | + PAI üzerine PET 103 µm 1450 Vp; ucuz prova bandı; – sınıf yetersiz | [US8847075B2](https://patents.google.com/patent/US8847075B2/en); [Teonex Q51](https://www.mueller-ahlhorn.com/wp-content/uploads/2024/04/Teonex-Q51-TC-00141-ENG.pdf); [Mylar](https://converting-tasm.pl/wp-content/uploads/2024/01/info-mylar-a-electrical-properties_ekotech_2023.pdf); [Zeus PET SLW](https://www.zeusinc.com/wp-content/uploads/2026/08/PET-SLW-Heat-Shrink-V1R1.pdf); [Nordson PET](https://interventional-solutions.nordsonmedical.com/files/interventional-solutions-nordsonmedical-com/Literature/Sell%20Sheets/MAR-PET-Heat-Shrink-Tubing-DS-01-DIGITAL.pdf) |
| LCP — overmolding veya film | — | — | Kanıt yok | Overmolding (tahmin) | – tel, film sarma veya overmolding verisi bulunamadı | — |
| Poliolefin — shrink (tek cidar veya yapışkan astarlı çift cidar) | busbar 2500–4100; çift cidar 900–1950 | 120–150 | Seri (EV busbar) | Çok kolay | + EV ürün hatları, 2500 V; – sınıf altında, astar ~85 °C'de yumuşuyor | [TE VOLINSU EVSW](https://www.te.com/en/products/heat-shrink-tubing/orange-heat-shrink-tubing/intersection/volinsu-heat-shrink-tubing/electric-vehicle-single-wall-tubing.html); [TE EVBB](https://www.te.com/en/products/heat-shrink-tubing/orange-heat-shrink-tubing/resources/volinsu-heat-shrink-tubing/electric-vehicle-busbar-tubing.html); [TE EVDW](https://www.te.com/en/products/heat-shrink-tubing/orange-heat-shrink-tubing/resources/volinsu-heat-shrink-tubing/electric-vehicle-dual-wall.html); [Farnell (2014)](https://www.farnell.com/datasheets/1937594.pdf); [WKK (2022)](https://www.wkk-europe.com/news/post/busbar-insulation-tubing-what-is-it-and-for-which-applications-is-it-used) |

- Eşit toplam kalınlıkta PPS ve PEEK emaye üzerinde benzer PDIV verdi: ~125 µm'de ~1,4 kVp, 195–200 µm'de 2,15–2,2 kVp ([US10109389B2](https://patents.google.com/patent/US10109389B2/en), patent verisi).
- PEI ve PPSU tek başına değil, PEEK altında bağ veya iç katman olarak kullanılmalı; sıcak ATF verisi yok (tahmin).
- Tasarlanmış arayüz olmadan çift ekstrüzyon katmanlar arası yapışmayı bozdu: PES 50 µm + modifiye PEEK/PPS 50 µm ([US9514863B2](https://patents.google.com/patent/US9514863B2/en)).

## Floropolimerler (PTFE, FEP, PFA, ETFE, PVDF)

Floropolimerler en düşük εr'yi (≈2,0–2,1) sunduğu için hava boşluğu kalan shrink'te en yüksek PD payını veriyor, ama hiçbiri hairpin'de seri değil. Sınıf 220 için yalnızca PTFE, PFA ve PTFE/PFA çift cidar 260 °C'ye çıkıyor; FEP 205, PVDF 175, ETFE 150 °C'de kalıyor ([Zeus 2026](https://www.zeusinc.com/wp-content/uploads/2026/08/Heat-Shrink-Comparison-Recovery-Guide-V1R7.pdf)).

| Malzeme – yöntem | Tipik kalınlık (µm) | Sınıf / sürekli sıcaklık (°C) | Olgunluk | Bare numuneye uygulanabilirlik | Artılar / riskler | Örnek ürün / kaynak |
|---|---|---|---|---|---|---|
| PTFE — shrink (2:1, 4:1, Sub-Lite-Wall) | SLW 25–127; 4:1'de 152–635 | 260 | Ticari | Evet (343 ± 10 °C fırın) | + oran 4:1'e kadar; – boy değişimi ±%20, 600 V/mil | [Zeus shrink kılavuzu 2026](https://www.zeusinc.com/wp-content/uploads/2026/08/Heat-Shrink-Comparison-Recovery-Guide-V1R7.pdf) |
| PTFE — ince kaydırmalı tüp | ≥38 | 250 | Ticari | Kolay; dikdörtgende hava boşluğu | – yuvarlak tüp geniş yüzde boşluk bırakıyor | [Daburn DTT500](https://www.daburn.com/dtt500-thin-wall-ptfe.aspx); [Daburn DUT](https://www.daburn.com/dut-ultra-thin-wall-ptfe.aspx) |
| PTFE — PSA bant | 50 film, 96 toplam | 204 | Ticari (ayırıcı bant) | Yüksek | – dielektrik değer verilmemiş | [3M 5480 (2022)](https://multimedia.3m.com/mws/media/1571419O/5480-ptfe-plastic-film-tape-data-sheet.pdf) |
| PFA, PTFE, FEP — tel ekstrüzyonu (dikdörtgen profil dahil) | ≥25 | PFA 260 | Ticari; EV hairpin'de yok | Hayır | + PFA telde "üstün PDIV", PAI'den %50 ince izolasyon (üretici beyanı, değer yok) | [Zeus PEEK/PFA tel](https://zeusinc.com/products/insulated-wire/peek-wire); [Daikin blog 2025](https://www.daikinchem.de/blog/boosting-electric-motor-performance/) |
| FEP — shrink (1,3/1,6/2:1) | 76–762 | 205 | Ticari | Kolay (216 ± 10 °C) | + düşük daraltma sıcaklığı, εr 2,1; – sınıf 220 için yetersiz, boy ±%15 | [Zeus shrink kılavuzu 2026](https://www.zeusinc.com/wp-content/uploads/2026/08/Heat-Shrink-Comparison-Recovery-Guide-V1R7.pdf) |
| FEP — film bant ve ısıyla yapışan katman | 12,5–500 | 205 | Ticari (PI/FEP içinde seri; tek başına lab) | Orta–yüksek | + εr 2,0; 25 µm'de 260 kV/mm; – soğuk akma, 21 MPa çekme dayanımı | [Chemours Teflon FEP](https://polymerfilms.com/wp-content/uploads/2023/06/Chemours-Teflon_FEP-Datasheet-cobranded-pf.pdf) |
| PFA — shrink | 102–508 | 260 | Ticari | Kolay (210 ± 10 °C) | + 260 °C sınıfında en düşük daraltma sıcaklığı; – oran ≤1,6:1 | [Zeus shrink kılavuzu 2026](https://www.zeusinc.com/wp-content/uploads/2026/08/Heat-Shrink-Comparison-Recovery-Guide-V1R7.pdf) |
| Eriyik astarlı çift cidar: PTFE/FEP (Dual-Shrink), PTFE/PFA (HTDS) | toplam ≤1651 | 205 / 260 | Ticari | Evet (343 ± 10 °C) | + iç katman eriyip boşluğu dolduruyor, uçları mühürlüyor; – kalın, düzensiz cidar, oran 1,3–1,4:1 | [Zeus shrink kılavuzu 2026](https://www.zeusinc.com/wp-content/uploads/2026/08/Heat-Shrink-Comparison-Recovery-Guide-V1R7.pdf) |
| PFA, FEP, ETFE — toz (NEOFLON) | 100–2000 | Tm 305 / 270 / 220 | Ticari (kimyasal astar) | Düşük–orta | + uzama %250–400; – elektriksel veri yok, Cu üzerinde pişirme sıcaklığı | [Daikin AC-5539 (2018)](https://www.daikinchemicals.com/library/pb_common/pdf/tds/Fluoropolymer_Coatings/NEOFLON_Coating_Powder/tds-ac-5539-E_ver01_Mar_2018.pdf); [NC-1539N (2018)](https://www.daikinchemicals.com/library/pb_common/pdf/tds/Fluoropolymer_Coatings/NEOFLON_Coating_Powder/tds-nc-1539n-E_ver01_Mar_2018.pdf); [EC-6510 (2018)](https://www.daikinchemicals.com/library/pb_common/pdf/tds/Fluoropolymer_Coatings/NEOFLON_Coating_Powder/tds-ec-6510-E_ver01_Mar_2018.pdf); [NEOFLON toz](https://www.daikinchemicals.com/solutions/products/fluoro-coatings/neoflon-powder.html) |
| PFA, FEP, ETFE, PVDF — özel profil tüp (shrink olmayan) | — | ≤260 | Ticari (özel profil) | Kolay; dikdörtgen kalıp gerekli | – kalıp maliyeti, oturma boşluğu | [Zeus özel profil](https://zeusinc.com/products/tubing/custom-profiles) |
| ETFE, PFA, FEP — film bant | — | — | Lab (patent listesi) | Orta | – PFA film verisi açılamadı | [US12665103B2](https://patents.google.com/patent/US12665103B2/en) |
| ETFE — shrink | — | 150 | Ticari | Kolay | – sınıf altında; εr 2,6 | [Wiremasters AS23053/14](https://www.wiremasters.com/product/harness-management-products/heat-shrink-tubing/m23053/m23053-14); [Fluorotherm](https://www.fluorotherm.com/technical-information/materials-overview/material-comparison/) |
| PVDF (Kynar) — shrink | 300 | 175 | Ticari | Kolay | – εr 8,4 (PD için en kötü), sınıf altında | [HellermannTyton Kynar](https://www.hellermanntyton.com/shared/assets/TDS_332-51273_com.pdf) |
| FKM (Viton-E) — shrink | 1200 | 200 | Ticari (uç bağlantı, ek yeri) | Kolay | + FKM elastomer ATF'de yüksek/orta uyumlu (100 °C); – 8 kV/mm, kalın cidar | [HellermannTyton Viton-E](https://www.hellermanntyton.com/shared/assets/TDS_330-01270_com.pdf); [García-Tuero 2022](https://mdpi-res.com/d_attachment/applsci/applsci-12-06213/article_deploy/applsci-12-06213.pdf) |

- Boyutlandırma: 4 × 2 mm, r 0,5 mm çubukta genişletilmiş ID >4,16 mm, serbest daralmış ID <3,55 mm olmalı. Asgari oran 1,17, pratikte 1,3–1,6:1 gerekiyor (hesaplama).
- Hava boşluğu modeli 20 µm boşluk ve 327 V Paschen minimumu varsayıyor ([Paschen yasası](https://en.wikipedia.org/wiki/Paschen%27s_law)). FEP 0,254 mm cidarda PDIV alt sınırı ≈2,3 kV; PEEKshrink 23 °C'de ≈1,24 kV, 200 °C'de ≈0,97 kV (hesaplama, büyüklük sırası).
- FEP ve PTFE dış yüzeyi ıslanmıyor; empregnasyon reçinesi yalnızca yapıştırılabilir Tip C ve C-20 filmlere tutunuyor ([Chemours Teflon FEP](https://polymerfilms.com/wp-content/uploads/2023/06/Chemours-Teflon_FEP-Datasheet-cobranded-pf.pdf)).

## Epoksi ve diğer termoset kaplamalar

Epoksi toz, hairpin kaynak uçlarında seri yöntem: ön ısıtılmış statorun kaynak uçları empregnasyondan sonra akışkan yatağa daldırılıyor ([bdtronic](https://bdtronic.com/en-en/impregnation-applications/stator-coating); [Gehring 2025](https://gehring-group.com/wp-content/uploads/2025/11/gehring-emobility_WEB-EN.pdf)). Belgelenen epoksi tozlarda uzama yalnızca >%5 olduğundan kaplama şekillendirme ve kaynaktan sonra yapılmalı; köşe kaplaması düz yüzeyin %30–40'ı kadar ([3M 5555 (2002)](https://multimedia.3m.com/mws/media/22602O/3mtm-scotchcasttm-electrical-resin-5555.pdf)).

| Malzeme – yöntem | Tipik kalınlık (µm) | Sınıf / sürekli sıcaklık (°C) | Olgunluk | Bare numuneye uygulanabilirlik | Artılar / riskler | Örnek ürün / kaynak |
|---|---|---|---|---|---|---|
| Epoksi toz — akışkan yatak daldırma (sıcak parça) | 1–5 s'de 200–2000 | 155 / 180 (UL 1446, hairpin dereceleri) | Seri (kaynak uçları) | Yüksek (ön ısıtma, küçük akışkan yatak, fırın) | + düzgün film; – köşe inceliği, pinler arası köprüleme, ön ısıtmada Cu oksitlenmesi | [AkzoNobel Resicoat EV (2025)](https://powdercoatings.brand.akzonobel.com/m/28e49a6fd077c2f1/original/NAM-Electric-Vehicle-Brochure.pdf); [Resicoat EL (2024)](https://powdercoatings.brand.akzonobel.com/m/e90ff93aef69124f/original/FUNC-Resicoat-Electrical-Insulation-Brochure-EN.pdf); [bdtronic toz makinesi](https://bdtronic.com/en-en/impregnation-machines/powder-coating-machine); [Braun](https://www.braun-sondermaschinen.de/en/special-machine-construction-and-epoxy-coating-systems/epoxy-coating-and-hairpin-systems/) |
| Epoksi toz — elektrostatik sprey veya elektrostatik akışkan yatak (soğuk parça + kür) | 100–300; busbar 100–1000 | 130–180; busbar dereceleri Tg2 100–112 | Seri (busbar toz kaplamasının ~%95'i elektrostatik sprey) | Yüksek (tabanca, fırın) | + 30–85 kV/mm; – çoklu kat, pinler arasında Faraday kafesi (tahmin) | [Resicoat HLG09R (2016)](https://powdercoatings.brand.akzonobel.com/m/4cc5273cdc960aa3/original/NAM-TDS-Resicoat-EL-HLG09R_US.pdf); [Resicoat HLF59R (2019)](https://powdercoatings.brand.akzonobel.com/m/41be4e412784d15e/original/TDS-Resicoat-EL-HLF59R-FR.pdf); [Axalta Alesta](https://secure.axalta.com/content/dam/general-industrial/segments/battery-solutions/Axalta_Battery_Solutions_2014.pdf); [US12119141B2](https://patents.google.com/patent/US12119141); [Electronic Design 2026](https://www.electronicdesign.com/55381411) |
| Epoksi toz (Scotchcast 5555, 265) — sıcak daldırma veya elektrostatik | test 300–380 | 5555: UL 1446 120–180; 265: 200 (helisel bobin) | Ticari (motor; 2002, 2007) | Yüksek | + 1300 V/mil (~51 kV/mm), cut-through >340 °C; – kenar %30–40 | [3M Scotchcast 5555 (2002)](https://multimedia.3m.com/mws/media/22602O/3mtm-scotchcasttm-electrical-resin-5555.pdf); [3M Scotchcast 265 (2007)](https://multimedia.3m.com/mws/media/22591O/3m-tm-scotchcast-tm-electrical-resin-265.pdf) |
| Dolgulu sıvı epoksi — kaynak ucu daldırma (CaCO3 %40–55, anhidrit kür) | 50–1000 | ≥155 | Patent (Hitachi, 2010) | Çok yüksek | + 5–11 kV AC; – kenar kaplama %21–39, sarkma | [US8735724B2](https://patents.google.com/patent/US8735724) |
| Jel kaplama, 2K döküm, ısı veya UV kürlü daldırma (kaynak uçları) | — | — | Piyasa yöntemi; ürün adı yok | Yüksek | – UV kürde gölge bölgeler (tahmin) | [bdtronic stator kaplama](https://bdtronic.com/en-en/impregnation-applications/stator-coating) |
| Epoksi macun — fırça veya sürme (Scotchcast 10N) | mm düzeyi | 130 | Ticari (onarım) | Çok yüksek | – 13,8 kV/mm, εr 5,3, düşük sınıf | [3M Scotchcast 10N (2016)](https://multimedia.3m.com/mws/media/1289663O) |
| Epoksi e-coat (katodik) | 20–45 | belirtilmemiş | Ticari (batarya parçaları) | Orta (banyo, DC kaynak) | + 70–150 kV/mm; – ısıl sınıf yok, ince | [Axalta AquaEC](https://secure.axalta.com/content/dam/general-industrial/segments/battery-solutions/Axalta_Battery_Solutions_2014.pdf) |
| Katodik ED — kaynak uçları (novolak epoksi, PAI, PI, akrilik vb.) | 5–50 | reçineye bağlı | Patent (Hitachi Astemo, 2013) | Orta | + tozdan daha iyi atış gücü; kalınlık PDIV'ye göre seçiliyor; – PDIV değeri yok | [US10630129B2](https://patents.google.com/patent/US10630129) |
| PAI veya PI — elektroforez düz tel | 10–100 | — | Patent (Mitsubishi Materials) | Orta (≥150–500 V DC, iki adımlı pişirme) | + 40 µm'de 3,5–6,0 kV, 100 µm'de 9,5 kV; – köşe şişmesi, arayüz oksidi | [US10706992B2](https://patents.google.com/patent/US10706992); [US9947436B2](https://patents.google.com/patent/US9947436); [US12278025B2](https://patents.google.com/patent/US12278025) |
| UV kürlü sıvı dielektrik ve dielektrik toz | — | — | Ticari (batarya) | Yüksek (UV lamba) | – ısıl sınıf kanıtsız | [PPG RAYCRON, ENVIROCRON (2023)](https://eventguides.informaengage.com/wp-content/uploads/2023/07/PPG-Solutions-for-EV-Battery-Packs.pdf) |
| Akrilik ve üretan konformal kaplama | — | 82 / 121 | Ticari (elektronik; el kitabı verisi 2002–04) | Çok yüksek | – sınıf yetersiz | [SCS tablosu (2016)](https://nrf.aux.eng.ufl.edu/_files/documents/14389.pdf) |
| Empregnasyon reçinesi (epoksi modifiye) | — | ≤220 (R) | Seri (sargı empregnasyonu) | — | Kaynak ucu ürünü değil; vernik uyumu testinde gerekli | [Axalta Energy Solutions (2023)](https://www.axalta.com/content/dam/general-industrial/segments/energy-solutions/Brochure_Energy_Solutions_2024.pdf); [ELANTAS empregnasyon](https://elantas.com/products/impregnating-materials.html) |

- Arayüz oksidi: ED PAI, 90° kenar bükmede (r = 3,25 mm) yalnızca 7–10 nm Cu oksitle A sınıfı yapışma verdi ([US12278025B2](https://patents.google.com/patent/US12278025), patent verisi). Toz için 160–260 °C'ye ısıtılan bakır havada oksitleniyor.
- Dielektrik dayanım kalınlığa bağlı: 70 µm'de 85 kV/mm, 0,30–0,38 mm'de ~51 kV/mm ölçüldü; test kalınlığı sabitlenmeli ([Axalta Alesta](https://secure.axalta.com/content/dam/general-industrial/segments/battery-solutions/Axalta_Battery_Solutions_2014.pdf); [3M 5555 (2002)](https://multimedia.3m.com/mws/media/22602O/3mtm-scotchcasttm-electrical-resin-5555.pdf)).
- Hiçbir kaynakta toz veya sıvı kaplı hairpin kaynak uçları için PDIV, ısıl çevrim veya ATF verisi yok.

## Parylene, silikon, seramik ve hibrit kaplamalar

[Parylene HT](https://nrf.aux.eng.ufl.edu/_files/documents/14389.pdf) köşeler dahil tam konformal, εr ≈2,2 ve havada 350 °C sürekli; ancak ≤75 µm kalınlıkla tek başına 800 V için yetersiz (tahmin). Silikon kaplamalar 200 °C'ye çıkıyor ama dielektrik dayanımları düşük; seramik ve sol-jel kaplamalar araştırma düzeyinde.

| Malzeme – yöntem | Tipik kalınlık (µm) | Sınıf / sürekli sıcaklık (°C) | Olgunluk | Bare numuneye uygulanabilirlik | Artılar / riskler | Örnek ürün / kaynak |
|---|---|---|---|---|---|---|
| Parylene HT (AF-4) — CVD, oda sıcaklığında | tercih 1–40; ≤75 | 350 sürekli / 450 kısa | Ticari hizmet; hairpin'de patent (Essex, 2016) | Yüksek (hizmet; maskeleme, A-174 astar) | + 5400 V/mil, uzama %200, su <%0,01; – ince, yavaş, pahalı | [SCS parylene tablosu (2016)](https://nrf.aux.eng.ufl.edu/_files/documents/14389.pdf); [US10510459B2](https://patents.google.com/patent/US10510459); [Parylene, Wikipedia](https://en.wikipedia.org/wiki/Parylene) |
| Parylene F (VT-4) — CVD | tercih 1–40; ≤75 | 200 uzun süreli / 250 kısa | Ticari hizmet | Yüksek | – elektriksel veri sınırlı | [HZO parylene](https://hzo.com/coatings/parylene-coating/properties) |
| Parylene C, N, D — CVD | — | 80 / 60 / 100 | Ticari | Yüksek | – sınıf 180–220 için uygun değil | [SCS servis sıcaklıkları (2022)](https://scscoatings.com/newsroom/blog/a-guide-to-parylene-service-temperatures/) |
| Plazma polimer — atmosferik veya düşük basınçlı plazma | <2 | — | Araştırma | Düşük | + çözücüsüz, PFAS'sız, "PD dirençli" (sayı yok); – birincil izolasyon için çok ince | [Fraunhofer IFAM](https://www.ifam.fraunhofer.de/en/technologies/electrical-insulation-coatings.html) |
| Silikon konformal kaplama (DOWSIL 3-1953) — sprey, fırça, daldırma | — | 200 | Ticari; hairpin kanıtı yok | Çok yüksek | + esnek; – 400 V/mil (~16 kV/mm), sıcak ATF'de şişme bilinmiyor | [DOWSIL 3-1953](https://www.ellsworth.com/products/conformal-coatings/silicone/dow-3-1953-silicone-conformal-coating-18.1-kg-pail/) |
| Silikon kauçuk shrink (ST-OR) | — | 200 | Ticari (EV busbar, 2024) | Muhtemelen kolay (veri yok) | + 28 kV/mm, esnek; – kalın ve yumuşak | [Shin-Etsu ST-OR (2024)](https://s24.q4cdn.com/622300748/files/doc_news/Shin-Etsu-Chemical-Develops-Industry-First-Heat-Shrinkable-Silicone-Rubber-Tubing-for-Busbar-Covering-2024.pdf) |
| Plazma sprey alümina (APS) | 183–217 | inorganik | Araştırma | Orta (fason termal sprey, kumlama) | – 10,5–12,9 kV/mm, εr 11–16, gözeneklilik %5–6, mikro çatlak; Cu genleşmesi Al2O3'ün ~3 katı | [Junge vd., Coatings 2022](https://depositonce.tu-berlin.de/items/73969378-3419-4ab0-8285-59cd6d136bdb) |
| Sol-jel organik-inorganik hibrit — tel kaplama cihazı | — | kür 380–425 | Araştırma | Düşük (sentez ve yüksek kür) | + ince Cu telde >200 V/µm, çatlaksız esneklik; – dikdörtgen tel verisi yok | [Pfeifer vd., sol-jel](https://opus4.kobv.de/opus4-w-hs/frontdoor/index/index/year/2018/docId/2832) |
| Seramik izolasyonlu tel (Ceramawire, Fujithermo M) | — | 20–400 (karakterizasyon aralığı) | Ticari (niş) | Hayır | – sayısal veri açık değil (2007) | [Strathclyde (2007)](https://strathprints.strath.ac.uk/37068/) |
| Anodizasyon (yalnızca Al iletken) | <15 (tercih <10) | >280 hedef bağlamı | Araştırma; Cu'ya uygulanamaz | Hayır | – 400–800 V için organik üst kat gerekli (tahmin) | [US6261437B1 (1996)](https://patents.google.com/patent/US6261437); [Energies 2022](https://ideas.repec.org/a/gam/jeners/v15y2022i15p5362-d870474.html) |

- Parylene C en yaygın ve en ucuz tür, ama havada sürekli 80 °C ile sınırlı; yalnızca HT veya VT-4 seçilmeli ([SCS (2022)](https://scscoatings.com/newsroom/blog/a-guide-to-parylene-service-temperatures/)).
- Kaynaklar çelişiyor: N için kısa süreli servis 80 °C (SCS) ve 95 °C (HZO); HT için εr 2,17–2,21 (SCS) ve ~2,5 (Wikipedia).
- Matriste plazma sprey alümina, en yakın yöntem olarak "Toz kaplama" sütununda gösterildi.

## Kâğıt, mika ve cam elyaf esaslı sargılar

Kâğıt, mika ve cam elyaf sargılar olgun ama gözenekli ve kalın (çift taraflı ≥0,2–0,54 mm); empregnasyonsuz 800 V'ta PD'siz olmaları beklenmiyor (tahmin). Test planında birincil iletken izolasyonu olarak değil, PD dayanımı karşılaştırıcısı ve oluk astarı veya kılıf olarak yer almalılar.

| Malzeme – yöntem | Tipik kalınlık (µm) | Sınıf / sürekli sıcaklık (°C) | Olgunluk | Bare numuneye uygulanabilirlik | Artılar / riskler | Örnek ürün / kaynak |
|---|---|---|---|---|---|---|
| Nomex 410 bant, %50 bindirme, çift sarım (DNX) + vernik | kâğıt ≥50; kat başına ≳200 (çift taraflı) | RTI 220 | Ticari (trafo, form bobin; NEMA MW 60) | Yüksek (elle) | + ATF uyumu (üretici beyanı), vernikle uyumlu; – gözenekli, 18–34 kV/mm, sürekli gerilim ≤1,6 kV/mm önerisi | [Arclin Nomex 410 (2026)](https://arclin.com/wp-content/uploads/2026/04/Arclin%E2%84%A2-Nomex%C2%AE-410-Technical-Datasheet-04-2026.pdf); [Essex DNX](https://www.electro-wind.com/114-x-258-double-nomex-wrapped-dnx-rectangular-mw-60-copper-magnet-wire-220c-white-250-lb-24-reel-average-wght) |
| Nomex 818 (aramid + %50 mika) bant | 80–250 | 220 sınıfı aile | Ticari (YG iletken ve bobin sarma) | Yüksek | + 410'dan iyi korona dayanımı, 28–39 kV/mm; – kalın | [Arclin Nomex 818 (2025)](https://arclin.com/wp-content/uploads/2026/04/Arclin_Nomex_818_Technical_Data_Sheet_2025.pdf) |
| Nomex/Kapton/Nomex (NKN) veya Nomex/Mylar/Nomex (NMN) spiral tüp (oluk astarı) | 130–190 | UL sistem 220 | Ticari (400/800 V için; üretici beyanı) | Orta | + "12 kV'a kadar" (üretici beyanı); – dikiş, Nomex tozu | [Politubes, CWIEME 2023](https://berlin.cwiemeevents.com/articles/e-motor-400---800v-insulation-thermal-managem); [Electric Motor Engineering](https://www.electricmotorengineering.com/e-motor-400-800v-insulation-thermal-management-for-hairpin-stator-slot-liner/) |
| Mika bant (Samicafilm; PET veya cam destekli), alın alına 2–3 kat veya %50 bindirme | bant 90; yapı 300–540 | TI 155 (çıplak) / 180 (emayeli) | Ticari (YG makineler) | Orta (kırılgan; B-aşama için 160 °C, 2,5 MPa pres) | + en iyi PD dayanımı; – kenar bükme ≥3× genişlik, pul dökülmesi | [Von Roll Samicafilm (2007)](https://hallaweb.jlab.org/tech/Detectors/public_html/manuals/data_sheets-manuals/U-V/von_roll/Samicafilm-Taped-315.15-01.pdf); [ELANTAS bantlar](https://www.elantas.com/en/electrical/innovative-insulation-tapes); [Isovolta 437320](https://www.electro-wind.com/web-files/Isovolta%5CDatasheets%5C4373-tech.pdf) |
| Mika + korona dirençli PI hibrit bant | — | — | Patent (1996–98); film destekli mika tur bantları ticari | Orta | + Al2O3 dolgulu Kapton destek; – statör çubuğunda 7–16 kat | [US5973269A](https://patents.google.com/patent/US5973269A/en) |
| Cam elyaf (Daglas) sarma + reçine | — | TI 180; 220 (üretici, MW-46C) | Ticari (alan bobinleri) | Düşük (sarma makinesi gerekli) | – gözenekli, kalın, reçinesiz PD riski | [IEC 60317-31](https://webstore.iec.ch/publication/23565); [Von Roll broşür](https://media.eis-inc.com/m/da351a69383baeb1/original/PH22-77877_9.pdf); [Rea](https://www.reawire.com/products/data-sheets/) |
| Cam elyaf örgü kılıf (akrilik, silikon veya Viton kaplı) | — | 155 / 200 / 220 | Ticari (motor uç bağlantıları) | Kolay (kaydırmalı) | + NEMA Grade A ≥7 kV ortalama; – gözenekli, hacimli | [Daburn D155](https://www.daburn.com/D155-DAFLEX-Acrylic-Coated-Fiberglass-Sleeving-MIL-I-3190/3.aspx); [Daburn D200](https://www.daburn.com/d200-rubber-fiberglass.aspx); [Daburn D220](https://www.daburn.com/d220-viton-fiberglass.aspx) |
| Nomex örgü kılıf | — | ≤240 | Ticari | Kolay | – dielektrik veri yok | [Textile Technologies](https://www.textiletechnologies.co.uk/en-sv/products/nomex-braided-sleeving.oembed) |

- Kâğıt ve örgü numuneleri hem kuru hem empregne hâlde test edilmeli; aradaki fark hava boşluğunun etkisini ölçer (tahmin).
- Mika şekillendirme sınırları: kenar ≥3× genişlik, düz ≥2× kalınlık; preslemeden sonra şekillendirme önerilmiyor ([Samicafilm (2007)](https://hallaweb.jlab.org/tech/Detectors/public_html/manuals/data_sheets-manuals/U-V/von_roll/Samicafilm-Taped-315.15-01.pdf)).
- Sarma yapıları 3,5 × 2,0 mm iletkende Cu payını 0,10 mm yapıda %92,6'ya, 0,36 mm yapıda %76,8'e düşürüyor (hesaplama).

## Malzeme özellikleri

εr sıcaklıkla en çok PEEK'te artıyor (25 °C'de 3,1, 250 °C'de 4,7); en düşük εr floropolimerlerde (2,0–2,1) ve [Parylene HT](https://nrf.aux.eng.ufl.edu/_files/documents/14389.pdf)'de (≈2,2). Değerler veri sayfası ve patentlerden; ölçüm koşulları farklı olduğundan dielektrik dayanımlar yalnızca tarama içindir.

| Malzeme | εr (sıcaklık, frekans) | Tg / Tm (°C) | Sürekli kullanım / sınıf (°C) | Dielektrik dayanım (kalınlık) | Kopma uzaması (%) | ATF / hidroliz notu | Kaynak |
|---|---|---|---|---|---|---|---|
| PAI (emaye) | 4,3; 4,55 (25 °C) ve 4,59 (180 °C); 3,9 → 4,4 (25 → 250 °C, 100 Hz) | Tg 280 | 220 (IEC); 180 (Victrex; çelişkili) | 150–190 V/µm | ~45 | Su emme %4,5; tek kat PAI ATF çevriminde 15,52 → 10,82 kV (patent verisi) | [SEI TR 84](https://global-sei.com/technology/tr/bn84/pdf/84-19.pdf); [Gao vd. 2023](https://cris.unibo.it/bitstream/11585/955904/3/PDIV%20prediction%20Gao%20PREPRINT_clean.pdf); [US9224523B2](https://patents.google.com/patent/US9224523B2/en); [US12159731B2](https://patents.google.com/patent/US12159731B2/en) |
| PI (emaye) | 3,0; 3,5 → 4,0 (25 → 250 °C, 100 Hz) | Tg 350 | 240 | 150–190 V/µm | ~80 | Su emme %3,0 | [SEI TR 84](https://global-sei.com/technology/tr/bn84/pdf/84-19.pdf); [Leone 2022](https://pubblicazioni.unicam.it/bitstream/11581/483506/1/30_05_2022%20PhD%20Thesis%20Ezio%20Leone.pdf) |
| THEIC-PEsI (emaye) | "düşük" (sayı yok) | — | 180–200 | 130–160 V/µm | — | PEsI/PAI kompozit ATF çevriminde 15,39 → 5,53 kV (patent verisi) | [Leone 2022](https://pubblicazioni.unicam.it/bitstream/11581/483506/1/30_05_2022%20PhD%20Thesis%20Ezio%20Leone.pdf); [US12159731B2](https://patents.google.com/patent/US12159731B2/en) |
| Mikro hücreli PI | 2,2 (%30 hücre); 1,7 (%50 hücre) | — | — | 10,8 kV (folyo testi); açık hücre 4,9 kV | — | — | [SEI TR 88](https://global-sei.com/technology/tr/bn88/pdf/E88-10.pdf) |
| PEEK (ekstrüzyon, film, tüp) | 3,20 (23 °C, 1 kHz); 3,2 → 4,5 (23 → 200 °C, 50 Hz); 3,1 → 4,7 (25 → 250 °C, 100 Hz); 2,2–3,0 (1 MHz, 2014; çelişkili) | Tg 143 (shrink 161) / Tm 343 | 220 / 240 (tahmini RTI) / 260 (polimer); çelişkili | 16,6 kV @100 µm (film, 2000 V/s); 190 kV/mm @50 µm; 23 kV/mm @2 mm | 45 (tüp malzemesi); >150 (film) | ATF 180 °C, 2000 h (üretici beyanı); su %0,04 (%50 RH) – %0,45 (doyma) | [XPI 150](https://victrex.com/de/downloads/datasheets/victrex-xpi-150-polymer); [Optinova (2022)](https://optinova.com/app/uploads/2022/09/optinova-peek-tubing.pdf); [APTIV 1000](https://www.victrex.com/-/media/ul-datasheet/aptiv-films-1000-series.pdf); [Zeus RESINATE (2014)](https://www.zeusinc.com/wp-content/uploads/2014/03/RESINATE_No3-PEEKInsWire_Zeus.pdf) |
| PEKK (Kepstan) | ≤3,5 hedef (tercih ≤3,1), 1 kHz | — | — | — | — | — | [US12148548B2](https://patents.google.com/patent/US12148548B2/en) |
| PPS | — | Tm 278–285 | ≤200 (toz derecesi) | 21,4–22,5 kV (PPS 100–105 µm + PAI 30–34 µm) | — | UV'ye zayıf | [US8847075B2](https://patents.google.com/patent/US8847075B2/en); [Hi-ECOWIRE](https://vb.nweurope.eu/media/13371/hi-ecowire_technical_sheet_polymer_extrusion.pdf) |
| PEI (ULTEM) | — | Tg 215–225 (film 217) | — | ~252 kV/mm (film) | — | Su %1,25 (24 h daldırma), %0,48 (%50 RH) | [SABIC ULTEM 1000B (2017)](https://polymerfilms.com/wp-content/uploads/2023/06/Polymerfilms-SABIC-ultem%E2%84%A2-1000b-natural-25-%C2%B5m-%E2%80%9350-%C2%B5m-film-datasheet.pdf) |
| PPSU | — | Tg ≈220 | "200 sınıfı" (patent) | 12,6 kV (354 µm, shotbox) | — | "Yüksek hidroliz direnci" | [Hi-ECOWIRE](https://vb.nweurope.eu/media/13371/hi-ecowire_technical_sheet_polymer_extrusion.pdf); [US12278026B2](https://patents.google.com/patent/US12278026B2/en) |
| TPI (AURUM) | — | Tg 245 | ">150" (üretici beyanı) | 22,4 kV (TPI 105 µm + PAI/PI 30 µm) | — | — | [Mitsui AURUM](https://us.mitsuichemicals.com/service/product/aurum.htm); [US8847075B2](https://patents.google.com/patent/US8847075B2/en) |
| PA11 | — | Tm 186 | — | CTI >600 V | — | — | [Arkema PA11 toz](https://hpp.arkema.com/en/markets-and-applications/powder-metal-coatings/electrical-applications-and-battery-components/) |
| PEN (Teonex Q51) | 3,0 (60 Hz) | Tm 269 | RTI 180 el. / 160 mek. | 250 kV/mm | 90 | Su %0,3 | [Teonex Q51](https://www.mueller-ahlhorn.com/wp-content/uploads/2024/04/Teonex-Q51-TC-00141-ENG.pdf) |
| PET (Mylar, shrink) | 3,0 (1 MHz) | Tm 245 (shrink) | 135 (shrink) | >600 kV/mm @6 µm; ~80 kV/mm @350 µm | — | — | [Mylar](https://converting-tasm.pl/wp-content/uploads/2024/01/info-mylar-a-electrical-properties_ekotech_2023.pdf); [Nordson PET](https://interventional-solutions.nordsonmedical.com/files/interventional-solutions-nordsonmedical-com/Literature/Sell%20Sheets/MAR-PET-Heat-Shrink-Tubing-DS-01-DIGITAL.pdf); [Professional Plastics (2008)](https://www.professionalplastics.com/professionalplastics/content/downloads/ElectricalPropertiesofPlastics.pdf) |
| Kapton HN | 3,4 (1 kHz, 25–50 µm) | Tg 360–410 (ikinci derece geçiş); erimez | UL 220–240 el. / 200–220 mek. | 303 kV/mm @25 µm (tipik); min. 236 | 72 | Sıcak suda bozunma; nem ≤%4,0 (24 h daldırma) | [Kapton özellikleri (2000)](https://www.electro-wind.com/web-files/DuPont%5CLiterature%5CKapton-summary-of-properties.pdf); [Kapton spesifikasyon (2012)](https://ca.electro-wind.com/web-files/DuPont%5CLiterature%5CKapton-general-specs-2.pdf) |
| Kapton FN / FWN / FWR (PI/FEP) | 2,6–3,1 | FEP Tm 260–280 | RTI 240 el. / 200 mek. | 142–272 kV/mm | 55–92 | FWR: geliştirilmiş hidroliz direnci | [Kapton FWN](https://www.qnityelectronics.com/kapton-fwn.html); [Kapton FWR](https://www.qnityelectronics.com/kapton-fwr.html); [Kapton FN (2006)](https://cshyde.com/Asset/Data%20Sheet%2018-__F%20Dupont%20Kapton%C2%AE%20FN%20Film.pdf) |
| Kapton 100CRC / 150FCRC019 | 3,4 | — | RTI 240/200 (CRC); 130 (FCRC sayfası; çelişkili) | 256 kV/mm (25,4 µm); 173 kV/mm (38,1 µm) | 65 / 79 | — | [Kapton CRC](https://www.qnityelectronics.com/kapton-crc.html); [Kapton FCRC](https://www.qnityelectronics.com/kapton-fcrc.html) |
| Kapton MT | 4,2 | — | RTI 240 / 200 | 217 kV/mm @25,4 µm | 80–100 | — | [Kapton MT](https://www.qnityelectronics.com/kapton-mt.html) |
| Upilex-S | 3,5 (25 °C), 3,3 (200 °C), 1 kHz | — | 290 (20 000 h, çekme) | ~272 kV/mm (25 µm; 25 ve 200 °C) | 40 | Su %1,4 (24 h) | [UBE Upilex-S 2022](https://ube.com/upilex/catalog/pdf/upilex_s_e.pdf) |
| Apical 50AV | 3,0 (1 kHz) | — | — | ~374 kV/mm @12,7 µm | 100–104 | Su %2,7 | [Apical 50AV](https://polymerfilms.com/wp-content/uploads/2024/09/Apical50AV-FILM.pdf) |
| FEP | 2,0 (100 Hz–1 MHz); 1,93–2,02 (−40…225 °C) | Tm 260–280 | 205 | 260 kV/mm @25 µm; 70 kV/mm @0,5 mm | 300 | Kimyasal olarak inert | [Chemours Teflon FEP](https://polymerfilms.com/wp-content/uploads/2023/06/Chemours-Teflon_FEP-Datasheet-cobranded-pf.pdf) |
| PTFE | 2,0–2,1 | Tm 327 | 260 | ~23,6 kV/mm (shrink); diğer kaynaklarda 18–170 kV/mm (çelişkili) | 100–400 | — | [Zeus shrink kılavuzu 2026](https://www.zeusinc.com/wp-content/uploads/2026/08/Heat-Shrink-Comparison-Recovery-Guide-V1R7.pdf); [Fluorotherm](https://www.fluorotherm.com/technical-information/materials-overview/material-comparison/); [UBE 2022](https://ube.com/upilex/catalog/pdf/upilex_s_e.pdf) |
| PFA | 2,05–2,1 | Tm 305 | 260 | ~79 kV/mm (shrink) | 250–350 (toz) | — | [Zeus shrink kılavuzu 2026](https://www.zeusinc.com/wp-content/uploads/2026/08/Heat-Shrink-Comparison-Recovery-Guide-V1R7.pdf); [Daikin AC-5539 (2018)](https://www.daikinchemicals.com/library/pb_common/pdf/tds/Fluoropolymer_Coatings/NEOFLON_Coating_Powder/tds-ac-5539-E_ver01_Mar_2018.pdf) |
| ETFE | 2,6 (1 MHz) | Tm 275 (Fluorotherm) / 220 (Daikin toz); çelişkili | 149–150 | 25–79 kV/mm (kütle) | 400 (toz) | — | [Fluorotherm](https://www.fluorotherm.com/technical-information/materials-overview/material-comparison/); [Daikin EC-6510 (2018)](https://www.daikinchemicals.com/library/pb_common/pdf/tds/Fluoropolymer_Coatings/NEOFLON_Coating_Powder/tds-ec-6510-E_ver01_Mar_2018.pdf) |
| PVDF | 8,4 (1 MHz) | Tm 177 | 175 | 30 kV/mm (shrink); 13 kV/mm (kütle) | — | — | [HellermannTyton Kynar](https://www.hellermanntyton.com/shared/assets/TDS_332-51273_com.pdf); [Professional Plastics (2008)](https://www.professionalplastics.com/professionalplastics/content/downloads/ElectricalPropertiesofPlastics.pdf) |
| FKM (Viton-E shrink) | — | — | 200 | 8 kV/mm (1,2 mm cidar) | ≥500 | FKM elastomer ATF'de yüksek/orta uyum (100 °C) | [HellermannTyton Viton-E](https://www.hellermanntyton.com/shared/assets/TDS_330-01270_com.pdf); [García-Tuero 2022](https://mdpi-res.com/d_attachment/applsci/applsci-12-06213/article_deploy/applsci-12-06213.pdf) |
| Epoksi toz | 4,0 (100 Hz–1 MHz) | Tg2 100–112 (busbar dereceleri) | 155–180 (hairpin); 130 (busbar) | 30–45 kV/mm; 85 kV/mm @70 µm; ~51 kV/mm @0,30–0,38 mm | >5 | "Hairpin akışkanlarına dayanım" (üretici beyanı) | [Resicoat HLF59R (2019)](https://powdercoatings.brand.akzonobel.com/m/41be4e412784d15e/original/TDS-Resicoat-EL-HLF59R-FR.pdf); [AkzoNobel EV (2025)](https://powdercoatings.brand.akzonobel.com/m/28e49a6fd077c2f1/original/NAM-Electric-Vehicle-Brochure.pdf); [Axalta Alesta](https://secure.axalta.com/content/dam/general-industrial/segments/battery-solutions/Axalta_Battery_Solutions_2014.pdf) |
| Epoksi macun (Scotchcast 10N) | 5,3 | — | 130 | 13,8 kV/mm @3,175 mm | 15 | Yağ ve yakıt dayanımı (üretici beyanı) | [3M Scotchcast 10N (2016)](https://multimedia.3m.com/mws/media/1289663O) |
| Silikon | 3,1–4,2 (60 Hz; el kitabı 2002–04) | — | 200 (ürün); 260 (genel) | ~16 kV/mm (kaplama); 28 kV/mm (shrink) | — | Silikon elastomer ATF'de yüksek/orta uyum | [SCS tablosu (2016)](https://nrf.aux.eng.ufl.edu/_files/documents/14389.pdf); [DOWSIL 3-1953](https://www.ellsworth.com/products/conformal-coatings/silicone/dow-3-1953-silicone-conformal-coating-18.1-kg-pail/); [García-Tuero 2022](https://mdpi-res.com/d_attachment/applsci/applsci-12-06213/article_deploy/applsci-12-06213.pdf) |
| Parylene HT | 2,21 / 2,20 / 2,17 (60 Hz / 1 kHz / 1 MHz); ~2,5 (çelişkili) | Tm >500 | 350 | 5400 V/mil (~213 kV/mm) | 200 | Su <%0,01 (24 h) | [SCS tablosu (2016)](https://nrf.aux.eng.ufl.edu/_files/documents/14389.pdf); [Parylene, Wikipedia](https://en.wikipedia.org/wiki/Parylene) |
| Parylene C | 3,15 / 3,10 / 2,95 (60 Hz / 1 kHz / 1 MHz) | Tm 290 | 80 | 5600 V/mil | 200 | Su <%0,1 | [SCS tablosu (2016)](https://nrf.aux.eng.ufl.edu/_files/documents/14389.pdf); [SCS (2022)](https://scscoatings.com/newsroom/blog/a-guide-to-parylene-service-temperatures/) |
| Nomex 410 | 1,6 (0,05 mm) – 3,7 (0,76 mm), 60 Hz | — | RTI 220 | 18–34 kV/mm | 10–23 (MD) | ATF uyumu (üretici beyanı) | [Arclin Nomex 410 (2026)](https://arclin.com/wp-content/uploads/2026/04/Arclin%E2%84%A2-Nomex%C2%AE-410-Technical-Datasheet-04-2026.pdf) |
| Nomex 818 | 23–250 °C arasında "esasen değişmez" | — | 220 (aile) | 28,1–39,3 kV/mm | — | — | [Arclin Nomex 818 (2025)](https://arclin.com/wp-content/uploads/2026/04/Arclin_Nomex_818_Technical_Data_Sheet_2025.pdf) |
| Mika bant (Samicafilm) | — | — | TI 155 / 180 | 3,5–7,0 kV (düz tel, asgari; 300–540 µm yapı) | — | — | [Samicafilm (2007)](https://hallaweb.jlab.org/tech/Detectors/public_html/manuals/data_sheets-manuals/U-V/von_roll/Samicafilm-Taped-315.15-01.pdf) |
| APS alümina | 15,6–10,8 (50 Hz) | — | inorganik | 10,5–12,9 kV/mm @183–217 µm | — | — | [Junge vd., Coatings 2022](https://depositonce.tu-berlin.de/items/73969378-3419-4ab0-8285-59cd6d136bdb) |
| PI e-coat (Toyochem) | — | Tg ≥200 | — | >10 kV (220 °C × 500 h sonrası) | — | — | [Toyochem PI ED](https://www.artiencegroup.com/en/products/metal-coatings/electrocoating/polyimide.html) |

## Yöntemlerin numune hazırlamaya etkisi

Kesik çıplak iletkene laboratuvarda sarma, tüp/shrink, toz, sıvı, elektroforez ve parylene uygulanabiliyor; emaye ve ekstrüzyon yalnızca sürekli hatta mümkün. Köşe kaplaması en iyi elektroforez ve parylene'de, en kötü toz ve sıvı daldırmada ([artience/Toyochem](https://www.artiencegroup.com/en/products/metal-coatings/electrocoating/polyimide.html); [3M 5555 (2002)](https://multimedia.3m.com/mws/media/22602O/3mtm-scotchcasttm-electrical-resin-5555.pdf)).

| Yöntem | Kesik çıplak iletkene lab'da uygulanabilir mi? | Köşe / kenar kaplaması | Hava boşluğu / PD riski | Kalınlık kontrolü | Ekipman veya dış hizmet | Şekillendirmeye göre sıra |
|---|---|---|---|---|---|---|
| Emaye, endüstriyel hat | Hayır; hazır tel alınmalı | Köşe inceliyor (20 µm hedefte 12–13 µm) | Düşük (yapışık film) | İyi (2–5 µm/paso) | Emaye hattı veya tel üreticisi | Önce (tel şekillendiriliyor) |
| Emaye, lab daldırma veya silme kalıbı | Kısmen (yayımlanmış protokol yok) | Kenarda ince, ortada kalın | Kabarcık, eksik kür | Zayıf | Çeker ocak (NMP), fırın, özel kalıp | Önce |
| Ekstrüzyon | Hayır (sürekli hat); bobin hâlinde fason | İyi; kenar/yüz kalınlık oranı kalıpla 1,01–5 ayarlanabilir | Düşük; yapışma zayıfsa delaminasyon | İyi (eş merkezlilik 1,1–1,5) | [Rosendahl RA-I](https://umformtechnik.net/wire/Content/Reports/Paving-the-way-for-800V-and-more), [MFL test hattı](https://ssr.expometals.net/en/hall/plants/stand/mfl-group/news/peek-extrusion-lines-tackling-new-electrical-insulation-challenges), Zeus özel üretim | Önce |
| Enjeksiyon overmolding | Evet | Kalıba bağlı | Yapışma boşluğu (busbar'da belgelendi, [EP4345850A1](https://data.epo.org/publication-server/rest/v1.2/patents/EP4345850NWA1/document.html)) | Kalın cidar | Enjeksiyon kalıbı | Sonra (şekillendirilemez) |
| Film bant sarma + ısıyla yapıştırma | Evet (elle, 6–12 mm bant) | Köşede gerilme, bindirme basamağı | Orta–yüksek (bindirme boşlukları) | Orta (bant kalınlığı × kat sayısı) | 280–350 °C fikstür veya fırın | Önce (sonra pratik değil) |
| PSA bant | Evet | Orta | Yapışkan katman ve basamak boşlukları | Orta | Yok | Önce |
| Kâğıt, mika, cam sarma | Evet (elle); cam için sarma makinesi | Kalın; mika kırılgan | Yüksek (gözenek); empregnasyon şart | Orta | Vernik veya VPI; mika için sıcak pres | Önce |
| Kaydırmalı tüp (yuvarlak) | Evet | Yalnızca köşelere oturuyor | Çok yüksek (4 × 2 mm'de ~1,1 mm; hesaplama) | Cidar iyi, oturma kötü | Yok | Önce veya yalnızca düz bacak |
| Isıyla daralan tüp | Evet | Köşe ince (önce temas), yüz kalın (tahmin) | Oran asgari değerin altındaysa yüzde boşluk | Orta (boy ±%15–20) | Fırın (FEP 216 °C; PEEK 343–385 °C) | Önce (bükmede kırışma) veya sonra (yalnızca düz bölüm) |
| Spiral sarılı NKN/Kapton tüp | Evet (dikdörtgen mandrelde üretilmişse) | İyi (ön şekilli) | Dikiş ve oturma boşluğu | İyi | Tedarikçi | Oluğa astar olarak takılıyor |
| Epoksi toz | Evet (yüksek) | Kenar, düz yüzün %30–40'ı | Düşük; köşe inceliği | Zayıf (200–2000 µm, daldırma süresine bağlı) | Ön ısıtma fırını, küçük akışkan yatak veya tabanca, kür fırını | Sonra (>%5 uzama) |
| Sıvı daldırma, fırça | Evet (çok yüksek) | Kenar %21–39 | Sarkma, boşluk | Zayıf | Basit | Sonra |
| Elektroforez | Orta (tedarikçi banyosu) | En iyi (>%80; köşe ≥ yüz) | Düşük; kabarcık, köpürme | İyi (5–100 µm; gerilim ve süre ile) | 150–500 V DC kaynak, banyo, 200–300 °C fırın | Sonra; kontrollü arayüzle önce olası |
| Termoplastik toz (PEEK, PFA, PA11) | PA11 yüksek; PEEK ve PFA düşük | Bilinmiyor | — | Orta | Kumlama, ≤450 °C fırın, onaylı kaplamacı | Sonra; floropolimerde önce olası (tahmin) |
| Parylene CVD | Evet (hizmet) | Tam konformal | En düşük | Çok iyi (oda sıcaklığı) | Kaplama hizmeti, maskeleme, A-174 astar | Sonra (Essex rotası); %200 uzama önceye de izin verebilir |
| APS alümina, sol-jel | Fason veya laboratuvar sentezi | APS'de görüş hattı (tahmin) | Gözenek, mikro çatlak | Orta | Termal sprey atölyesi; 380–425 °C kür | Sonra (kırılgan) |

- Yuvarlak tüp dikdörtgen çubukta hava bırakıyor: 4,2 mm ID tüp, 4 × 2 mm çubuğun geniş yüzlerinin ortasında ~1,1 mm boşluk bırakıyor (hesaplama). Bu numune PD testinde kullanılmamalı.
- Shrink boyutlandırma kuralı (a × b çubuk, köşe yarıçapı r): D_c = √((a−2r)² + (b−2r)²) + 2r ve P = 2(a+b) − (8−2π)r. Genişletilmiş ID_min > D_c, serbest daralmış ID_max < P/π, asgari oran R_min = π·D_c/P (hesaplama).
- Ön şekilli dikdörtgen shrink tüp kırışma ve boşluğu önlüyor; tüp bükmeden önce takılıp koruyucu bükme aparatı kullanılıyor ([EP1154543B1 (2000)](https://patents.google.com/patent/EP1154543B1/en)). PET tüp kare mandrelde şekillendirilip ısıl sabitlenebiliyor ([Nordson PET](https://interventional-solutions.nordsonmedical.com/files/interventional-solutions-nordsonmedical-com/Literature/Sell%20Sheets/MAR-PET-Heat-Shrink-Tubing-DS-01-DIGITAL.pdf)).
- PEEKshrink erime noktasına (343 °C) çok yakın daraltılıyor; Zeus ısı tabancası yerine fırın öneriyor ve sıcaklığa ulaştıktan sonra 10 dk tutuyor ([Zeus 2026](https://www.zeusinc.com/wp-content/uploads/2026/08/Heat-Shrink-Comparison-Recovery-Guide-V1R7.pdf)).
- Eşit toplam kalınlıkta karşılaştırın: PDIV kalınlıkla ~8–11 Vp/µm artıyor, Cu payı 40 µm'de %94,0'dan 200 µm'de %74,8'e iniyor (hesaplama).
- PDIV'yi en yüksek sıcaklıkta ölçün: PEEK εr 3,1 → 4,7, PAI 3,9 → 4,4 (25 → 250 °C). PI-FEP numunede PDIV oda sıcaklığından 180 °C'ye ~0,2 kV düştü ([Gao vd. 2023](https://cris.unibo.it/bitstream/11585/955904/3/PDIV%20prediction%20Gao%20PREPRINT_clean.pdf)).
- Uçlar ve yüzey: kesik uçların çapağını alıp radyus verin; tüp ucu bakır-polimer-hava üçlü noktası olduğundan elektrotları uçlardan uzak tutun, tüpü %15–25 uzun kesin (tahmin). Ön ısıtma ve pişirme bakırda oksit büyütüyor; ED PAI'de en iyi bükme yapışması 7–10 nm oksitte ([US12278025B2](https://patents.google.com/patent/US12278025)).

## Test planı önerileri

Kampanya üç öncelik grubuyla kurulmalı ve tüm adaylar ~100, ~150 ve ~200 µm toplam kalınlıkta, ≥180 °C'de PDIV ile karşılaştırılmalı. Her test şekillendirme ve ATF yaşlandırmasından önce ve sonra tekrarlanmalı; kaplamalar en çok bu adımlarda ayrışıyor (tahmin).

### Öncelik grupları

| Grup | Kombinasyonlar | Amaç | Tedarik / uygulama yolu |
|---|---|---|---|
| Grup A — ticari referans teller | PEsI+PAI emaye (sınıf 200); PAI tek kat (220); korona dirençli PAI; PI emaye (240); ekstrüde PEEK tek katman (~150 ve ~200 µm); emaye + PEEK (~30 µm PAI + ~120 µm PEEK; ~200 µm); PI/FEP sarılı tel (120FN616 veya 150FN019 referans, 150FCRC019 korona dirençli) | Seri yapıların taban çizgisi; PDIV, şekillendirme ve ATF referansı | Bobin hâlinde, aynı bakır kesitiyle: [Essex Furukawa HVWW](https://kyodonewsprwire.jp/index.php/release/202108138772), [hpw](https://webdisclosure.com/press-release/hpw-metallwerk-gmbh-etr-hpw-metallwerk-significantly-expands-production-of-peek-high-performance-wires-and-responds-to-high-demand-in-the-electromobility-sector-4JiKH4q2n8L), [Bekaert Ampact](https://www.bekaert.com/content/dam/corporate/en/events/wire-d%C3%BCsseldorf/docs-mobility/Ampact%20copper%20magnet%20wire%20for%20e-motors.pdf), [Jiateng](https://tech.ifeng.com/c/8lbM26LSIAO), [Zeus PEEK tel](https://zeusinc.com/products/insulated-wire/peek-wire), [Sumitomo](https://global-sei.com/technology/tr/bn90/pdf/E90-04.pdf) |
| Grup B — çıplak iletkende laboratuvar | PI/FEP ve korona dirençli PI/FEP bant (elle, %50 bindirme, 1–2 kat, ısıyla yapıştırma); [PEEKshrink](https://www.zeusinc.com/products/heat-shrinkable-tubing/peekshrink/); FEP ve PFA shrink; HTDS PTFE/PFA eriyik astarlı shrink (boşluksuz referans); epoksi toz (akışkan yatak); [Parylene HT](https://nrf.aux.eng.ufl.edu/_files/documents/14389.pdf); [PI e-coat](https://www.artiencegroup.com/en/products/metal-coatings/electrocoating/polyimide.html); [NKN spiral tüp](https://berlin.cwiemeevents.com/articles/e-motor-400---800v-insulation-thermal-managem) | Yöntem etkisini aynı iletkende ölçmek | Ekip içi (sarma, fırın, akışkan yatak); parylene ve e-coat için hizmet sağlayıcı; [Kapton FCRC](https://www.qnityelectronics.com/kapton-fcrc.html) (Kasım 2025'ten beri [Qnity](https://en.wikipedia.org/wiki/Qnity_Electronics) markası), [Zeus shrink](https://www.zeusinc.com/wp-content/uploads/2026/08/Heat-Shrink-Comparison-Recovery-Guide-V1R7.pdf), [Resicoat EV](https://powdercoatings.brand.akzonobel.com/m/28e49a6fd077c2f1/original/NAM-Electric-Vehicle-Brochure.pdf) |
| Grup C — keşif | Mikro hücreli PI; PEKK, TPI, PPS ve PEI/PEEK ko-ekstrüzyonu; [VICOTE](https://www.victrex.com/en/downloads/datasheets/vicote-700-series) PEEK ve PFA tozu; [Gunze](https://www.gunze.co.jp/e/epd/products/peek/) düşük sıcaklık PEEK shrink; PEEK film bant; sol-jel, APS alümina, plazma polimer; [Nomex 818](https://arclin.com/wp-content/uploads/2026/04/Arclin_Nomex_818_Technical_Data_Sheet_2025.pdf) ve mika bant (PD dayanımı karşılaştırıcısı) | Yeni malzemelerin potansiyelini görmek | Tedarikçi numunesi; deneme hattı ([MFL](https://ssr.expometals.net/en/hall/plants/stand/mfl-group/news/peek-extrusion-lines-tackling-new-electrical-insulation-challenges)); Ar-Ge ortağı ([Materia Nova, Hi-ECOWIRE](https://vb.nweurope.eu/media/13371/hi-ecowire_technical_sheet_polymer_extrusion.pdf)); reçine üreticisi desteği ([Victrex e-kitap 2024](https://cdn.victrex.com/-/media/downloads/literature/ja/victrex_auto_ebook_wirecoatings_04_2024.pdf), [Arkema Kepstan](https://hpp.arkema.com/en/product-families/kepstan-pekk-polymers/wire-coatings/)) |

### Test tablosu

IEC 60317-0-2 madde yapısı (Test 4–23) tüm adaylar için test iskeleti olabilir, ama PD testi içermiyor ([IEC 60317-0-2](https://www.vde-verlag.de/iec-normen/preview-pdf/info_iec60317-0-2%7Bed4.0%7Db.pdf)). Dikdörtgen tel için aşınma (IEC 60851-3 Test 11) ve kesme-geçme (IEC 60851-6 Test 10) testi de yok; patentler JIS C 3216-6 kullanıyor. Emaye dışı kaplamalarda IEC 60851 yöntemleri benzetimle uygulanmalı ve sınır değerler anlaşmayla belirlenmeli.

| Test | Standart | Numune geometrisi | Koşullar | Kabul veya referans değer | Kaynak |
|---|---|---|---|---|---|
| PDIV, AC, tel çifti (T/T) | IEC 60270:2025; IEC 60034-18-41 | İki iletken, geniş yüzler 150 mm temasta; ayrıca kenar teması; sabit kelepçe kuvveti (ör. 7,8 N) | 50 Hz; 10–50 V/s rampa; sabit PD eşiği (5, 10 veya 50 pC); 25, 180 ve gerekirse 220 °C; sabit RH | 1,3–2,3 kVpp (hesaplama); patent: 25 °C'de ≥1 kVp, 250 °C'de ≥%50 | [US9224523B2](https://patents.google.com/patent/US9224523B2/en); [Wakimoto vd. 2016](https://nagoya.repo.nii.ac.jp/record/24052/files/IEEE-TDEI-2015-proofread.pdf); [Part III](https://zenodo.org/records/4562202) |
| RPDIV, tekrarlı darbe | IEC TS 61934:2024 | Tel çifti; 300 mm oluk içi hairpin | PWM, 70–120 ns yükselme; 20–180 °C | Sıcaklık etkisi yükselme süresi etkisinden büyük; yayılım RT'de ~200 V, 80–180 °C'de >400 V | [He vd. 2025](https://d-nb.info/1376542846/34) |
| PDIV, P/G | IEC 60034-18-41 | İletken + metal plaka veya oluk maketi; astarlı ve astarsız | İlk satırla aynı | 2,2–2,8 kVpp (hesaplama) | [Part III](https://zenodo.org/records/4562202) |
| Delinme gerilimi | IEC 60851-5 Test 13, madde 4.7 (2019 CSV veya 2026 Ed. 5.0 belirtilmeli) | Metal folyo sarılı veya metal bilye içinde; düz ve bükülmüş bölge | 50 Hz, 500 V/s, 5 mA; 25 ve 250 °C | 250 °C'de ≥%50 korunum (patent verisi); >10 kV hedef | [US9224523B2](https://patents.google.com/patent/US9224523B2/en); [IEC 60851-5:2026](https://www.technickenormy.cz/en/iec-60851-5-2026-rlv-winding-wires-test-methods-part-5-electrical-properties/) |
| Şekillendirme zinciri | IEC 60851-3:2023 Test 6 ve 8; JIS C 3216-3; NEMA MW 1000-2012 | 300 mm düz; 5 µm çizik; 180° bükme 1,0 mm göbek; 90° bükme 4,0 mm; gerçek taç yarıçapı | %1–30 ön uzama; düz ve kenar bükme; 100 N burulma; ardından delinme ve PDIV | Çatlak yok; burulma ≥30 tur (A) veya 10–<30 (B); düz numuneye göre PDIV ve delinme korunumu | [US11232885B2](https://patents.google.com/patent/US11232885B2/en); [US9324476B2](https://patents.google.com/patent/US9324476B2/en) |
| Isıl şok | IEC 60851-6 Test 9 | Gerilmiş veya bükülmüş numune | ≥240 °C; PI/FEP için 240 °C × 2 h × 10 çevrim | Çatlak yok; delinme ≥2,5 kV (CRRC gereksinimi) | [He vd. 2025](https://d-nb.info/1376542846/34); [CRRC 2023](https://castjournals.cast.org.cn/joweb/jycl/EN/PDF/10.16790/j.cnki.1009-9239.im.2023.02.011) |
| Isıl dayanıklılık (TI) | IEC 60172:2020; IEC 60216-1 | IEC 60172 madde 5.1.2 dikdörtgen tel numunesi | En az 3 sıcaklık (ör. 220/240/260 °C); 20 000 h'e ekstrapolasyon; her adımda PDIV ve kalınlık | TI ≥220 °C | [IEC 60172:2020](https://www.vde-verlag.de/iec-normen/preview-pdf/info_iec60172%7Bed5.0%7Db.pdf); [Part III](https://zenodo.org/records/4562202) |
| ATF + su | IEC 60851-4 Test 20; ASTM D1676-03 | 300 mm düz; kapalı paslanmaz çelik kap | 150 °C, 500 h, %0,5 su; 150 °C, 1000 h, %0,2 su; PEEK sınıfı için 180–200 °C | 1,0 mm göbekte 180° bükme sonrası çatlak yok; 1 kHz εr değişmez; PDIV ve delinme korunumu | [US11232885B2](https://patents.google.com/patent/US11232885B2/en); [US12100532B2](https://patents.google.com/patent/US12100532B2/en) |
| Gerilim dayanımı (V–t), PD altında | [IEC 60034-18-42](https://www.vde-verlag.de/iec-normen/preview-pdf/info_iec60034-18-42%7Bed1.1%7Db.pdf) (yalnızca PD'ye izin verilirse); IEC 61858 | Düz, bükülmüş ve ATF yaşlandırılmış numune | Ör. 155 °C, 20 kHz kare dalga, 3 kV; veya 10 kHz sinüs | Karşılaştırmalı; korona dirençli emayede %10 uzama ömrü <%20'ye indirdi | [US12159731B2](https://patents.google.com/patent/US12159731B2/en); [SEI TR 88](https://global-sei.com/technology/tr/bn88/pdf/E88-10.pdf); [EMCA 2017](https://opaj.napstic.cn/periodicalArticle/0120171002033563) |
| Elektro-ısıl yaşlandırma (formette) | IEC 60034-18-41 ve IEC 60034-18-21 alt çevrimleri | 300 mm oluk içi hairpin; ≥5 numune | PWM 1 kHz; 675–975 V; 20–210 °C; ≥250 h; titreşim ve fırın birlikte | Bozulma oranı (referans %20,5–29,5); RPDIV tek başına yaşlanma göstergesi değil | [He vd. 2025](https://d-nb.info/1376542846/34); [Zhou vd. 2024](https://mdpi-res.com/d_attachment/energies/energies-17-01987/article_deploy/energies-17-01987.pdf) |
| Soyma ve kaynak bölgesi | Standart yok | Soyulmuş uç; kaynaklı formette | Lazer soyma (CO2, CO2 + NIR, UV, fs); lazer kaynak | Kalıntı <1 µm ve <9 RFU (üretici beyanı); soyulma dayanımı 315 N (çıplak Cu referansı) | [Novanta](https://novanta.com/precision-manufacturing/resources/whitepapers/unlocking-efficiency-in-electric-motors-the-power-of-hairpin-stripping/); [ASSEMBLY 2025](https://www.assemblymag.com/articles/99369-laser-stripping-of-magnet-wire); [TRUMPF](https://www.apricon.fi/wp-content/uploads/trumpf-whitepaper-hairpin-welding-e-motors-en.pdf) |
| Nem ve basınç | IEC 60034-18-41 AMD1 | Tel çifti | %20 ve %90 RH; düşük basınç (PDIV minimumu 50–70 mbar) | Raporlanmalı; gerekirse ek EF | [Wakimoto vd. 2016](https://nagoya.repo.nii.ac.jp/record/24052/files/IEEE-TDEI-2015-proofread.pdf); [Elorza Azpiazu vd. 2023](https://mdpi-res.com/d_attachment/applsci/applsci-13-02417/article_deploy/applsci-13-02417.pdf) |
| Kesit, kalınlık ve kristallik | IEC 60851-2 Test 4 | Düz, köşe ve bükülmüş bölge kesiti | Mikroskop; PEEK için DSC ile kristallik | Köşe-yüz farkı ≤%20 (patent verisi); PEEK kristalliği ≥%50 (patent örneği) | [US9330817B2](https://patents.google.com/patent/US9330817B2/en); [US9514863B2](https://patents.google.com/patent/US9514863B2/en) |

### Numune geometrisi

- Tüm yöntemlerde aynı çıplak iletken kullanılmalı ve köşe yarıçapı raporlanmalı; patentler PD'yi bastırmak için r ≤0,6 mm (tercih 0,2–0,4 mm) kullanıyor ([US10109389B2](https://patents.google.com/patent/US10109389B2/en)). Köşe yarıçapı T/T PDIV'yi ve saçılımını değiştiriyor ([Naderiallaf vd. 2024](https://unnc.globalimpact.cn/en/publications/fillet-radius-impact-of-rectangular-insulated-wires-on-pdiv-for-t)).
- Düz numune 300 mm (bükme, ATF) olmalı; PDIV çifti 150 mm temas ve tanımlı kelepçe kuvvetiyle hazırlanmalı ([US9224523B2](https://patents.google.com/patent/US9224523B2/en); [Wakimoto vd. 2016](https://nagoya.repo.nii.ac.jp/record/24052/files/IEEE-TDEI-2015-proofread.pdf)).
- T/T için geniş yüz (flatwise) ve kenar (edgewise) temaslı iki çift tipi, P/G için iletken-plaka veya oluk maketi kullanılmalı (tahmin).
- Formette olarak 300 mm oluk içi hairpin kullanılmalı; U-büküm tacı, burulma bölgesi ve kaynak ucu ayrı test edilmeli ([He vd. 2025](https://d-nb.info/1376542846/34)).
- Her koşulda ≥5 numune; numune başına 3 ölçüm, 60 s arayla, sıcaklıkta 10 dk bekletmeden sonra ([Part III](https://zenodo.org/records/4562202); [Elorza Azpiazu vd. 2023](https://mdpi-res.com/d_attachment/applsci/applsci-13-02417/article_deploy/applsci-13-02417.pdf)).
- Sarma ve tüp numuneleri düz uygulanıp sonra şekillendirilmeli; "kılıf → bükme" ve "bükme → düz bölüme kılıf" çiftleri birlikte test edilmeli (tahmin).

### Açık sorular ve veri boşlukları

- 800 V için yayımlanmış OEM PDIV hedefi bulunamadı; gerçek evirici-motor bağlantısında OF ölçülmeli.
- Aynı kalınlık ve sıcaklıkta emaye ile ekstrüde PEEK'in bağımsız, hakemli PDIV karşılaştırması bulunamadı.
- Su içeriği belirtilmiş ATF yaşlandırması sonrası PDIV veya delinme için hakemli veri bulunamadı; yalnızca patent ve üretici beyanı var.
- Hairpin için ısıl şok (ör. −40/+180 °C) ve nemli ısı (85 °C / %85 RH) profili bulunamadı; OEM tanımlı değerler kullanılmalı.
- Bant ve shrink'in U-büküm, burulma ve oluğa yerleştirme sonrası davranışı ile köşe inceliği ölçülmemiş.
- Kaynak ısı etkisi bölgesinde izolasyon hasarı ve kaynak sonrası PDIV verisi yok.
- Isıl sınıf çelişkileri çözülmeli: PAI 180 veya 220 °C; PEEK 220, 240 veya 260 °C; Kapton FCRC RTI 130 veya 240 °C.
- PD eşiği (5, 10 veya 50 pC), rampa, dalga şekli ve RH sabitlenmeli; IEC 60034-18-41 Ed. 2 durumu ile Tablo 4, B.2 ve B.6 değerleri doğrulanmalı ([IEC webstore](https://webstore.iec.ch/en/publication/32755)).
- Hairpin üzerinde PD yöntemlerinin (iki iletken, çelik bilye banyosu, tuz banyosu) PAI, PPS ve PEEK karşılaştırması sayısal olarak açık erişimde değil ([Kilper vd. 2020](https://cris.fau.de/publications/270664426)).

## Kaynaklar

Raporda atıf yapılan 210 kaynak konuya göre gruplandı; notlara göre tümüne 10 Ekim 2026'da erişildi.

### Standartlar ve yönetmelik

- [IEC 60034-18-41:2014 önizleme (iTeh)](https://cdn.standards.iteh.ai/samples/18905/b95c2f0bc77e4b658894b3e6629e3aa2/IEC-60034-18-41-2014.pdf)
- [IEC 60034-18-41 AMD1:2019 önizleme (iTeh)](https://cdn.standards.iteh.ai/samples/23527/a1d9bbea464c4242a53f644c696783a0/IEC-60034-18-41-2014-AMD1-2019.pdf)
- [IEC 60034-18-41 birleştirilmiş sürüm, IEC webstore](https://webstore.iec.ch/en/publication/32755)
- [IEC 60034-18-42 Ed. 1.1 önizleme (VDE)](https://www.vde-verlag.de/iec-normen/preview-pdf/info_iec60034-18-42%7Bed1.1%7Db.pdf)
- [IEC TS 61934:2024, IEC webstore](https://webstore.iec.ch/en/publication/91294)
- [IEC 60270 Ed. 4.0 önizleme (VDE)](https://www.vde-verlag.de/iec-normen/preview-pdf/info_iec60270%7Bed4.0%7Db.pdf)
- [IEC 60317-0-2 Ed. 4.0 önizleme (VDE)](https://www.vde-verlag.de/iec-normen/preview-pdf/info_iec60317-0-2%7Bed4.0%7Db.pdf)
- [IEC 60317-28, PEsI sınıf 180 (IEC webstore)](https://webstore.iec.ch/en/publication/96016)
- [IEC 60317-82:2020, PEsI sınıf 200 (AFNOR)](https://www.boutique.afnor.org/en-gb/standard/iec-60317822020/specifications-for-particular-types-of-winding-wires-part-82-polyesterimide/xs137256/248845)
- [IEC 60317-29 (1990), PEsI + PAI sınıf 200 (IEC webstore)](https://webstore.iec.ch/publication/1387)
- [IEC 60317-58, PAI sınıf 220 önizleme (VDE)](https://assets.vde-verlag.de/iec-normen/preview-pdf/info_iec60317-58%7Bed1.0%7Db.pdf)
- [IEC 60317-47, PI sınıf 240 (IEC webstore)](https://webstore.iec.ch/en/publication/95918)
- [IEC 60317-80, polivinil asetal (IEC webstore)](https://webstore.iec.ch/en/publication/60783)
- [IEC 60317-44, PI bant sarılı tel (IEC webstore)](https://webstore.iec.ch/publication/1424)
- [IEC 60317-31:2015, cam elyaf sarılı tel (IEC webstore)](https://webstore.iec.ch/publication/23565)
- [IEC 60851-2 önizleme (VDE)](https://www.vde-verlag.de/iec-normen/preview-pdf/info_iec60851-2%7Bed3.2%7Db.pdf)
- [IEC 60851-3:2023 önizleme (VDE)](https://www.vde-verlag.de/iec-normen/preview-pdf/info_iec60851-3%7Bed4.0%7Db.pdf)
- [IEC 60851-4 önizleme (VDE)](https://www.vde-verlag.de/iec-normen/preview-pdf/info_iec60851-4%7Bed3.0%7Db.pdf)
- [IEC 60851-5 Ed. 4.2 önizleme (VDE)](https://www.vde-verlag.de/iec-normen/preview-pdf/info_iec60851-5%7Bed4.2%7Db.pdf)
- [IEC 60851-5:2026 kaydı (technickenormy)](https://www.technickenormy.cz/en/iec-60851-5-2026-rlv-winding-wires-test-methods-part-5-electrical-properties/)
- [IEC 60851-6 önizleme (VDE)](https://www.vde-verlag.de/iec-normen/preview-pdf/info_iec60851-6%7Bed3.0%7Db.pdf)
- [IEC 60172:2020 önizleme (VDE)](https://www.vde-verlag.de/iec-normen/preview-pdf/info_iec60172%7Bed5.0%7Db.pdf)
- [IEC 60216-1 önizleme (VDE)](https://www.vde-verlag.de/iec-normen/preview-pdf/info_iec60216-1%7Bed6.0%7Db.pdf)
- [AB Tüzüğü 2018/588, NMP kısıtlaması (EUR-Lex)](https://eur-lex.europa.eu/eli/reg/2018/588/oj)

### PD, PDIV ve hairpin test literatürü

- [Lusuardi vd., MEA'da PD Part III, IEEE Access 2021 (Zenodo)](https://zenodo.org/records/4562202)
- [Zhou vd., hairpin yalıtım yeterliliği, Energies 2024](https://mdpi-res.com/d_attachment/energies/energies-17-01987/article_deploy/energies-17-01987.pdf)
- [He, Tenbohlen, Beltle, hairpin elektro-ısıl yaşlanma, Energies 2025](https://d-nb.info/1376542846/34)
- [Elorza Azpiazu vd., PDIV modelleri, Appl. Sci. 2023](https://mdpi-res.com/d_attachment/applsci/applsci-13-02417/article_deploy/applsci-13-02417.pdf)
- [Wakimoto vd., nemde dikdörtgen tel PDIV, IEEE TDEI 2016](https://nagoya.repo.nii.ac.jp/record/24052/files/IEEE-TDEI-2015-proofread.pdf)
- [Gao vd., hairpin PDIV tahmini, IEEE TDEI 2023](https://cris.unibo.it/bitstream/11585/955904/3/PDIV%20prediction%20Gao%20PREPRINT_clean.pdf)
- [Naderiallaf vd., köşe yarıçapı ve PDIV, IEEE TDEI 2024 (özet)](https://unnc.globalimpact.cn/en/publications/fillet-radius-impact-of-rectangular-insulated-wires-on-pdiv-for-t)
- [Mancinelli vd., hairpin motor yeterliliği, IEEE TIA 2017 (özet)](https://cris.unibo.it/handle/11585/598944)
- [Kilper vd., hairpin PD test yöntemleri, EDPC 2020 (özet)](https://cris.fau.de/publications/270664426)
- [Taylor vd., emayeli hairpin'de deşarj, 2014 (özet)](https://researchprofiles.kettering.edu/en/publications/electrical-discharge-in-enamel-insulated-hairpin-copper-conductor/)
- [Gerilmiş korona dirençli tel, EMCA 2017 (özet)](https://opaj.napstic.cn/periodicalArticle/0120171002033563)
- [ATF'de 2000 h daldırma, Insulating Materials 2024](https://castjournals.cast.org.cn/joweb/jycl/EN/1209927011296997871)
- [García-Tuero vd., ATF ve elastomer uyumu, Appl. Sci. 2022](https://mdpi-res.com/d_attachment/applsci/applsci-12-06213/article_deploy/applsci-12-06213.pdf)
- [Paschen yasası (Wikipedia)](https://en.wikipedia.org/wiki/Paschen%27s_law)

### Emaye kaplamalar

- [Leone, NMP'siz tel emayeleri, doktora tezi 2022](https://pubblicazioni.unicam.it/bitstream/11581/483506/1/30_05_2022%20PhD%20Thesis%20Ezio%20Leone.pdf)
- [SEI Technical Review 84 (2017), mıknatıs teli geçmişi](https://global-sei.com/technology/tr/bn84/pdf/84-19.pdf)
- [SEI Technical Review 88 (2019), inverter motoru için dikdörtgen tel](https://global-sei.com/technology/tr/bn88/pdf/E88-10.pdf)
- [SEI Technical Review 90 (2020), EV sürüş motoru telleri](https://global-sei.com/technology/tr/bn90/pdf/E90-04.pdf)
- [SEI Technical Review 90 (2020), tel analiz teknikleri](https://global-sei.com/technology/tr/bn90/pdf/E90-05.pdf)
- [Axalta Voltatex 8536](https://www.axalta.com/electricalinsulation_global/en_US/wire-enamels/product-catalog/Voltatex-8536.html)
- [Axalta, tel emayeleri genel bakış](https://www.axalta.com/electricalinsulation_global/en_US/wire-enamels/what-are-wire-enamels.html)
- [ELANTAS PI tel emayeleri](https://www.elantas.com/en-br/stories/wire-enamels-pi/)
- [ELANTAS Tongling PAI emayeleri](https://elantas.com/tongling/products/wire-enamels/polyamideimide-enamels.html)
- [Essex GP/MR-200 dikdörtgen tel (Electro-Wind)](https://www.electro-wind.com/superior-essex-130-312-heavy-gp-mr-200-mw-36-magnet-wire-24in)
- [Sumitomo ve Essex PEEK kaplı tel (Magnetics Magazine)](https://magneticsmag.com/sumitomo-advances-development-manufacturing-of-its-rectangular-magnet-wire-for-evs/)
- [Bekaert, emaye ve PEEK karşılaştırması (2023)](https://www.linkedin.com/pulse/enamel-vs-peek-why-wire-coating-matters-high-voltage-vermeersch)

### Ekstrüzyon ve termoplastik teller

- [Essex Furukawa HVWW basın bülteni (2021)](https://kyodonewsprwire.jp/index.php/release/202108138772)
- [hpw Metallwerk PEEK teli basın bülteni (2023)](https://webdisclosure.com/press-release/hpw-metallwerk-gmbh-etr-hpw-metallwerk-significantly-expands-production-of-peek-high-performance-wires-and-responds-to-high-demand-in-the-electromobility-sector-4JiKH4q2n8L)
- [Bekaert Ampact sunumu (wire 2024)](https://www.bekaert.com/content/dam/corporate/en/events/wire-d%C3%BCsseldorf/docs-mobility/Ampact%20copper%20magnet%20wire%20for%20e-motors.pdf)
- [Syensqo KetaSpire KT-857 (CompositesWorld 2023)](https://www.compositesworld.com/products/peek-for-monolayer-e-motor-magnet-wire-insulation)
- [Mavel ve Syensqo (Magnetics Magazine 2025)](https://magneticsmag.com/mavel-powertrain-selects-syensqo-materials-for-high-performance-ev-motor-project/)
- [Mavel motor malzemeleri (e-Mobility Engineering)](https://www.emobility-engineering.com/?p=16587)
- [Victrex e-motor çözümleri](https://www.victrex.com/en/emotor-solutions)
- [Victrex XPI e-kitap (2024)](https://cdn.victrex.com/-/media/downloads/literature/ja/victrex_auto_ebook_wirecoatings_04_2024.pdf)
- [Victrex XPI 150 veri sayfası](https://victrex.com/de/downloads/datasheets/victrex-xpi-150-polymer)
- [Jiateng PEEK düz tel (ifeng 2025)](https://tech.ifeng.com/c/8lbM26LSIAO)
- [Zeus PEEK ve PFA tel](https://zeusinc.com/products/insulated-wire/peek-wire)
- [Zeus PEEK tel veri sayfası V2R5](https://www.zeusinc.com/wp-content/uploads/2026/07/PEEK-Insulated-Wire-V2R5.pdf)
- [Zeus RESINATE No. 3, PEEK tel (2014)](https://www.zeusinc.com/wp-content/uploads/2014/03/RESINATE_No3-PEEKInsWire_Zeus.pdf)
- [Arkema Kepstan PEKK tel kaplamaları](https://hpp.arkema.com/en/product-families/kepstan-pekk-polymers/wire-coatings/)
- [Arkema EV uygulamaları](https://hpp.arkema.com/en/markets-and-applications/automotive-and-transportation/electric-vehicles)
- [Rosendahl Nextrom RA-I hairpin hattı (WIRE 2023)](https://umformtechnik.net/wire/Content/Reports/Paving-the-way-for-800V-and-more)
- [MFL PEEK ekstrüzyon hatları (Expometals 2024)](https://ssr.expometals.net/en/hall/plants/stand/mfl-group/news/peek-extrusion-lines-tackling-new-electrical-insulation-challenges)
- [MFL/Frigeco PEEK ve PPSU teli (Wire & Cable India 2024)](https://www.wirecable.in/?p=32084)
- [Hi-ECOWIRE polimer ekstrüzyonu teknik sayfası](https://vb.nweurope.eu/media/13371/hi-ecowire_technical_sheet_polymer_extrusion.pdf)
- [Mitsui AURUM TPI](https://us.mitsuichemicals.com/service/product/aurum.htm)
- [TPI kaplı mıknatıs telleri (WIRE 2024)](https://umformtechnik.net/wire/Content/Reports/Polyimide-coated-magnet-wires)
- [Daikin NEOFLON PFA mıknatıs teli (blog 2025)](https://www.daikinchem.de/blog/boosting-electric-motor-performance/)

### Film, bant, kâğıt, mika ve cam elyaf

- [Kapton FCRC (Qnity)](https://www.qnityelectronics.com/kapton-fcrc.html)
- [Kapton FWN (Qnity)](https://www.qnityelectronics.com/kapton-fwn.html)
- [Kapton FWR (Qnity)](https://www.qnityelectronics.com/kapton-fwr.html)
- [Kapton PRN (Qnity)](https://www.qnityelectronics.com/kapton-prn.html)
- [Kapton CRC (Qnity)](https://www.qnityelectronics.com/kapton-crc.html)
- [Kapton MT (Qnity)](https://www.qnityelectronics.com/kapton-mt.html)
- [Kapton ECRC duyurusu (2020)](https://www.qnityelectronics.com/blogs/kapton-polyimide-film-addresses-impact-of-higher-switching-frequency-and-faster-voltage-rise.html)
- [Qnity Electronics (Wikipedia)](https://en.wikipedia.org/wiki/Qnity_Electronics)
- [Kapton genel spesifikasyonlar (2012)](https://ca.electro-wind.com/web-files/DuPont%5CLiterature%5CKapton-general-specs-2.pdf)
- [Kapton motor ve mıknatıs teli bülteni (2014)](https://ca.electro-wind.com/web-files/DuPont%5CLiterature%5CKapton-motor-magnet-wire-bulletin.pdf)
- [Kapton özellikler özeti (2000)](https://www.electro-wind.com/web-files/DuPont%5CLiterature%5CKapton-summary-of-properties.pdf)
- [Kapton FN veri sayfası (2006)](https://cshyde.com/Asset/Data%20Sheet%2018-__F%20Dupont%20Kapton%C2%AE%20FN%20Film.pdf)
- [P. Leo 1K063CR Kapton CR bant (2007)](https://pleo.com/wp-content/uploads/2024/02/1K063CR_EN.pdf)
- [CRRC, korona dirençli PI film ve tel (2023)](https://castjournals.cast.org.cn/joweb/jycl/EN/PDF/10.16790/j.cnki.1009-9239.im.2023.02.011)
- [CMC kısmi deşarja dayanıklı bantlar](https://www.cmc.de/en/teilentladungsfeste-klebebaender)
- [3M 92 PI bant (2013)](https://ca.electro-wind.com/web-files/3M%5CDatasheets%5C3M92.pdf)
- [Apical 50AV veri sayfası](https://polymerfilms.com/wp-content/uploads/2024/09/Apical50AV-FILM.pdf)
- [UBE Upilex-S kataloğu (2022)](https://ube.com/upilex/catalog/pdf/upilex_s_e.pdf)
- [Victrex APTIV 1000 film](https://www.victrex.com/-/media/ul-datasheet/aptiv-films-1000-series.pdf)
- [Goodfellow APTIV 1000](https://www.goodfellow.com/uk/victrex-aptiv-1000-peek-film-group)
- [Teonex Q51 PEN film](https://www.mueller-ahlhorn.com/wp-content/uploads/2024/04/Teonex-Q51-TC-00141-ENG.pdf)
- [Mylar elektriksel özellikler](https://converting-tasm.pl/wp-content/uploads/2024/01/info-mylar-a-electrical-properties_ekotech_2023.pdf)
- [SABIC ULTEM 1000B film (2017)](https://polymerfilms.com/wp-content/uploads/2023/06/Polymerfilms-SABIC-ultem%E2%84%A2-1000b-natural-25-%C2%B5m-%E2%80%9350-%C2%B5m-film-datasheet.pdf)
- [Chemours Teflon FEP film](https://polymerfilms.com/wp-content/uploads/2023/06/Chemours-Teflon_FEP-Datasheet-cobranded-pf.pdf)
- [3M 5480 PTFE bant (2022)](https://multimedia.3m.com/mws/media/1571419O/5480-ptfe-plastic-film-tape-data-sheet.pdf)
- [WTM PI/FEP sarma hatları](https://ssr.expometals.net/en/hall/plants/stand/wtm-srl/products/taping-lines-for-polyimide-fep)
- [Arclin Nomex 410 (2026)](https://arclin.com/wp-content/uploads/2026/04/Arclin%E2%84%A2-Nomex%C2%AE-410-Technical-Datasheet-04-2026.pdf)
- [Arclin Nomex 818 (2025)](https://arclin.com/wp-content/uploads/2026/04/Arclin_Nomex_818_Technical_Data_Sheet_2025.pdf)
- [Essex DNX Nomex sarılı tel (Electro-Wind)](https://www.electro-wind.com/114-x-258-double-nomex-wrapped-dnx-rectangular-mw-60-copper-magnet-wire-220c-white-250-lb-24-reel-average-wght)
- [Politubes EVtubes (CWIEME Berlin 2023)](https://berlin.cwiemeevents.com/articles/e-motor-400---800v-insulation-thermal-managem)
- [800 V hairpin oluk astarı (Electric Motor Engineering)](https://www.electricmotorengineering.com/e-motor-400-800v-insulation-thermal-management-for-hairpin-stator-slot-liner/)
- [Von Roll Samicafilm bant sarılı tel (2007)](https://hallaweb.jlab.org/tech/Detectors/public_html/manuals/data_sheets-manuals/U-V/von_roll/Samicafilm-Taped-315.15-01.pdf)
- [ELANTAS yalıtım bantları](https://www.elantas.com/en/electrical/innovative-insulation-tapes)
- [Isovolta 437320 mika bant](https://www.electro-wind.com/web-files/Isovolta%5CDatasheets%5C4373-tech.pdf)
- [Von Roll motor onarım yalıtım broşürü](https://media.eis-inc.com/m/da351a69383baeb1/original/PH22-77877_9.pdf)
- [Rea veri sayfaları](https://www.reawire.com/products/data-sheets/)

### Tüp ve ısıyla daralan kılıflar

- [Zeus PEEKshrink](https://www.zeusinc.com/products/heat-shrinkable-tubing/peekshrink/)
- [Zeus PEEKshrink veri sayfası V1R4 (2024)](https://www.zeusinc.com/wp-content/uploads/2024/06/PEEKshrink-Heat-Shrink-V1R4.pdf)
- [Zeus shrink karşılaştırma ve daraltma kılavuzu V1R7 (2026)](https://www.zeusinc.com/wp-content/uploads/2026/08/Heat-Shrink-Comparison-Recovery-Guide-V1R7.pdf)
- [Zeus PEEK ekstrüzyon tüpleri V2R2 (2024)](https://www.zeusinc.com/wp-content/uploads/2024/06/PEEK-Extrusions-V2R2.pdf)
- [Zeus özel profiller](https://zeusinc.com/products/tubing/custom-profiles)
- [Zeus PI tüp V2R9](https://www.zeusinc.com/wp-content/uploads/2026/07/Polyimide-Tubing-V2R9.pdf)
- [Zeus PET Sub-Lite-Wall shrink (2026)](https://www.zeusinc.com/wp-content/uploads/2026/08/PET-SLW-Heat-Shrink-V1R1.pdf)
- [Gunze PEEK ısıyla daralan tüp](https://www.gunze.co.jp/e/epd/products/peek/)
- [Optinova PEEK tüp](https://optinova.com/peek-tubing/)
- [Optinova PEEK tüp veri sayfası (2022)](https://optinova.com/app/uploads/2022/09/optinova-peek-tubing.pdf)
- [MicroLumen PI tüp](https://www.microlumen.com/medical-tubing/polyimide/)
- [Nordson PI tüp](https://interventional-solutions.nordsonmedical.com/files/interventional-solutions-nordsonmedical-com/Literature/Sell%20Sheets/MAR-Polyimide-DS-01-DIGITAL.pdf)
- [Nordson PET shrink](https://interventional-solutions.nordsonmedical.com/files/interventional-solutions-nordsonmedical-com/Literature/Sell%20Sheets/MAR-PET-Heat-Shrink-Tubing-DS-01-DIGITAL.pdf)
- [Pleo tüp ve kılıf (2024)](https://pleo.com/wp-content/uploads/2024/02/Tube-Sleeve.pdf)
- [Fluorotherm floropolimer karşılaştırması](https://www.fluorotherm.com/technical-information/materials-overview/material-comparison/)
- [Professional Plastics, plastiklerin elektriksel özellikleri (2008)](https://www.professionalplastics.com/professionalplastics/content/downloads/ElectricalPropertiesofPlastics.pdf)
- [Wiremasters AS23053/14 ETFE shrink](https://www.wiremasters.com/product/harness-management-products/heat-shrink-tubing/m23053/m23053-14)
- [Daburn DTT500 ince PTFE tüp](https://www.daburn.com/dtt500-thin-wall-ptfe.aspx)
- [Daburn DUT ultra ince PTFE tüp](https://www.daburn.com/dut-ultra-thin-wall-ptfe.aspx)
- [Daburn D155 akrilik kaplı cam kılıf](https://www.daburn.com/D155-DAFLEX-Acrylic-Coated-Fiberglass-Sleeving-MIL-I-3190/3.aspx)
- [Daburn D200 silikon kaplı cam kılıf](https://www.daburn.com/d200-rubber-fiberglass.aspx)
- [Daburn D220 Viton kaplı cam kılıf](https://www.daburn.com/d220-viton-fiberglass.aspx)
- [HellermannTyton Kynar shrink](https://www.hellermanntyton.com/shared/assets/TDS_332-51273_com.pdf)
- [HellermannTyton Viton-E shrink](https://www.hellermanntyton.com/shared/assets/TDS_330-01270_com.pdf)
- [TE VOLINSU EVBB busbar tüpü](https://www.te.com/en/products/heat-shrink-tubing/orange-heat-shrink-tubing/resources/volinsu-heat-shrink-tubing/electric-vehicle-busbar-tubing.html)
- [TE VOLINSU EVSW tek cidar](https://www.te.com/en/products/heat-shrink-tubing/orange-heat-shrink-tubing/intersection/volinsu-heat-shrink-tubing/electric-vehicle-single-wall-tubing.html)
- [TE VOLINSU EVDW çift cidar](https://www.te.com/en/products/heat-shrink-tubing/orange-heat-shrink-tubing/resources/volinsu-heat-shrink-tubing/electric-vehicle-dual-wall.html)
- [Farnell yapışkan astarlı çift cidar (2014)](https://www.farnell.com/datasheets/1937594.pdf)
- [WKK busbar yalıtım tüpü (2022)](https://www.wkk-europe.com/news/post/busbar-insulation-tubing-what-is-it-and-for-which-applications-is-it-used)
- [Shin-Etsu ST-OR silikon shrink (2024)](https://s24.q4cdn.com/622300748/files/doc_news/Shin-Etsu-Chemical-Develops-Industry-First-Heat-Shrinkable-Silicone-Rubber-Tubing-for-Busbar-Covering-2024.pdf)
- [Textile Technologies Nomex örgü kılıf](https://www.textiletechnologies.co.uk/en-sv/products/nomex-braided-sleeving.oembed)

### Toz, sıvı, elektroforez, buhar fazı ve inorganik kaplamalar

- [bdtronic stator kaplama](https://bdtronic.com/en-en/impregnation-applications/stator-coating)
- [bdtronic toz kaplama makinesi](https://bdtronic.com/en-en/impregnation-machines/powder-coating-machine)
- [Gehring e-mobilite broşürü (2025)](https://gehring-group.com/wp-content/uploads/2025/11/gehring-emobility_WEB-EN.pdf)
- [Braun Sondermaschinen epoksi ve hairpin sistemleri](https://www.braun-sondermaschinen.de/en/special-machine-construction-and-epoxy-coating-systems/epoxy-coating-and-hairpin-systems/)
- [AkzoNobel Resicoat EV broşürü (2025)](https://powdercoatings.brand.akzonobel.com/m/28e49a6fd077c2f1/original/NAM-Electric-Vehicle-Brochure.pdf)
- [AkzoNobel Resicoat EL broşürü (2024)](https://powdercoatings.brand.akzonobel.com/m/e90ff93aef69124f/original/FUNC-Resicoat-Electrical-Insulation-Brochure-EN.pdf)
- [Resicoat EL HLG09R (2016)](https://powdercoatings.brand.akzonobel.com/m/4cc5273cdc960aa3/original/NAM-TDS-Resicoat-EL-HLG09R_US.pdf)
- [Resicoat EL HLF59R (2019)](https://powdercoatings.brand.akzonobel.com/m/41be4e412784d15e/original/TDS-Resicoat-EL-HLF59R-FR.pdf)
- [3M Scotchcast 5555 (2002)](https://multimedia.3m.com/mws/media/22602O/3mtm-scotchcasttm-electrical-resin-5555.pdf)
- [3M Scotchcast 265 (2007)](https://multimedia.3m.com/mws/media/22591O/3m-tm-scotchcast-tm-electrical-resin-265.pdf)
- [3M Scotchcast 10N (2016)](https://multimedia.3m.com/mws/media/1289663O)
- [Axalta batarya çözümleri: Alesta, AquaEC (2024)](https://secure.axalta.com/content/dam/general-industrial/segments/battery-solutions/Axalta_Battery_Solutions_2014.pdf)
- [Axalta Energy Solutions broşürü (2023)](https://www.axalta.com/content/dam/general-industrial/segments/energy-solutions/Brochure_Energy_Solutions_2024.pdf)
- [Busbar toz kaplama uygulaması (Electronic Design 2026)](https://www.electronicdesign.com/55381411)
- [PPG EV batarya paketi çözümleri (2023)](https://eventguides.informaengage.com/wp-content/uploads/2023/07/PPG-Solutions-for-EV-Battery-Packs.pdf)
- [ELANTAS empregnasyon malzemeleri](https://elantas.com/products/impregnating-materials.html)
- [DOWSIL 3-1953 silikon kaplama (Ellsworth)](https://www.ellsworth.com/products/conformal-coatings/silicone/dow-3-1953-silicone-conformal-coating-18.1-kg-pail/)
- [artience/Toyochem PI elektroforez boyası](https://www.artiencegroup.com/en/products/metal-coatings/electrocoating/polyimide.html)
- [Honey Kasei PI elektroforez reçinesi (IPROS)](https://pr.mono.ipros.com/en/honny/product/detail/2001642863/)
- [Shimizu Elecoat elektroforez boyaları (IPROS)](https://mono.ipros.com/en/cg2/Electrochemical%20Paint)
- [Zirignon vd., PEI elektroforetik biriktirme, RSC Adv. 2021](https://pmc.ncbi.nlm.nih.gov/articles/PMC9042725/)
- [SCS parylene ve konformal kaplama tablosu (2016)](https://nrf.aux.eng.ufl.edu/_files/documents/14389.pdf)
- [SCS parylene servis sıcaklıkları (2022)](https://scscoatings.com/newsroom/blog/a-guide-to-parylene-service-temperatures/)
- [HZO parylene özellikleri](https://hzo.com/coatings/parylene-coating/properties)
- [Parylene (Wikipedia)](https://en.wikipedia.org/wiki/Parylene)
- [Fraunhofer IFAM plazma polimer yalıtım](https://www.ifam.fraunhofer.de/en/technologies/electrical-insulation-coatings.html)
- [Victrex VICOTE 700 PEEK toz](https://www.victrex.com/en/downloads/datasheets/vicote-700-series)
- [Arkema PA11 toz kaplamalar](https://hpp.arkema.com/en/markets-and-applications/powder-metal-coatings/electrical-applications-and-battery-components/)
- [Rilsan PA11 T Blue 7444 MAC](https://hpp.arkema.com/en/products/product/f/spa_hpp_RilsanPowders/p/rilsan-pa11-t-blue-7444-mac/)
- [Daikin NEOFLON PFA AC-5539 (2018)](https://www.daikinchemicals.com/library/pb_common/pdf/tds/Fluoropolymer_Coatings/NEOFLON_Coating_Powder/tds-ac-5539-E_ver01_Mar_2018.pdf)
- [Daikin NEOFLON FEP NC-1539N (2018)](https://www.daikinchemicals.com/library/pb_common/pdf/tds/Fluoropolymer_Coatings/NEOFLON_Coating_Powder/tds-nc-1539n-E_ver01_Mar_2018.pdf)
- [Daikin NEOFLON ETFE EC-6510 (2018)](https://www.daikinchemicals.com/library/pb_common/pdf/tds/Fluoropolymer_Coatings/NEOFLON_Coating_Powder/tds-ec-6510-E_ver01_Mar_2018.pdf)
- [Daikin NEOFLON kaplama tozları](https://www.daikinchemicals.com/solutions/products/fluoro-coatings/neoflon-powder.html)
- [Syensqo Ryton PPS toz kaplama (Interplas 2025)](https://interplasinsights.com/plastics-materials/latest-plastics-materials-news/syensqo-ryton-polyphenylene-sulfide-coating-grade/)
- [Junge vd., Cu üzerinde APS alümina, Coatings 2022](https://depositonce.tu-berlin.de/items/73969378-3419-4ab0-8285-59cd6d136bdb)
- [Pfeifer vd., sol-jel hibrit tel kaplama](https://opus4.kobv.de/opus4-w-hs/frontdoor/index/index/year/2018/docId/2832)
- [Timoshkin vd., seramik izolasyonlu teller (2007)](https://strathprints.strath.ac.uk/37068/)
- [Ait-Amar vd., anodize Al şerit tel, Energies 2022](https://ideas.repec.org/a/gam/jeners/v15y2022i15p5362-d870474.html)

### Soyma ve kaynak

- [TRUMPF lazer soyma ve kaynak beyaz kâğıdı (2021)](https://chargedevs.com/wp-content/uploads/2021/04/TRUMPF_Whitepaper_Laser-stripping_welding_EV.pdf)
- [TRUMPF hairpin kaynak beyaz kâğıdı (tarihsiz)](https://www.apricon.fi/wp-content/uploads/trumpf-whitepaper-hairpin-welding-e-motors-en.pdf)
- [Novanta hairpin soyma (2023)](https://novanta.com/precision-manufacturing/resources/whitepapers/unlocking-efficiency-in-electric-motors-the-power-of-hairpin-stripping/)
- [Lazer soyma karşılaştırması (ASSEMBLY 2025)](https://www.assemblymag.com/articles/99369-laser-stripping-of-magnet-wire)

### Patentler (patent verisi)

- [US9324476B2, Essex: emaye + ekstrüde PEEK (2014)](https://patents.google.com/patent/US9324476B2/en)
- [US9224523B2, Furukawa: inverter darbesine dayanıklı tel (2013)](https://patents.google.com/patent/US9224523B2/en)
- [US11232885B2, Essex Furukawa: termoset yığın + termoplastik (2015)](https://patents.google.com/patent/US11232885B2/en)
- [US12100532B2, Proterial: ATF dayanımlı yuvarlak tel](https://patents.google.com/patent/US12100532B2/en)
- [US10418151B2, Furukawa: köpük PI/PAI laminat (2013)](https://patents.google.com/patent/US10418151B2/en)
- [US6337442B1, ALTANA/Schenectady: PD dirençli üst kat (1997)](https://patents.google.com/patent/US6337442B1/en)
- [US12159731B2, Suzhou Jufeng: ATF ve korona dirençli tel (2020)](https://patents.google.com/patent/US12159731B2/en)
- [US9330817B2, Hitachi Metals: köşe kalınlığı ve kalıp (2010)](https://patents.google.com/patent/US9330817B2/en)
- [US3850773A, GE: elektrokaplama ve daldırma (1974)](https://patents.google.com/patent/US3850773A/en)
- [US9514863B2, Furukawa: PAI + PEI + PEEK (2012)](https://patents.google.com/patent/US9514863B2/en)
- [US10109389B2, Furukawa: çok katlı emaye + PEEK veya PPS (2014)](https://patents.google.com/patent/US10109389B2/en)
- [US8847075B2, Furukawa/Denso: yüzey işlemli emaye üzerine ekstrüzyon (2011)](https://patents.google.com/patent/US8847075B2/en)
- [US12278026B2, Essex: ko-ekstrüzyon (2020)](https://patents.google.com/patent/US12278026B2/en)
- [US10037833B2, Furukawa: kristal/amorf harman katmanı](https://patents.google.com/patent/US10037833B2/en)
- [US12148548B2, Arkema: psödo-amorf PAEK kılıf (2020)](https://patents.google.com/patent/US12148548B2/en)
- [US7125604B2, Rea: kenara ekstrüzyon (2004)](https://patents.google.com/patent/US7125604B2/en)
- [US12665103B2, Totoku: bant sarılı tel (2020)](https://patents.google.com/patent/US12665103B2/en)
- [US5973269A, GE Canada: mika + CR PI bant (1996)](https://patents.google.com/patent/US5973269A/en)
- [EP1154543B1, Alstom: dikdörtgen shrink tüp (2000)](https://patents.google.com/patent/EP1154543B1/en)
- [EP4345850A1, Rockwell: busbar hava boşluğu (2024)](https://data.epo.org/publication-server/rest/v1.2/patents/EP4345850NWA1/document.html)
- [US12068636B2, LG Magna: soyma boyu ve kaynak (2020)](https://patents.google.com/patent/US12068636B2/en)
- [US8735724B2, Hitachi: kaynak ucu epoksi daldırma (2010)](https://patents.google.com/patent/US8735724)
- [US10630129B2, Hitachi Astemo: kaynak ucunda ED (2013)](https://patents.google.com/patent/US10630129)
- [US10706992B2, Mitsubishi Materials: ED düz tel (2017)](https://patents.google.com/patent/US10706992)
- [US9947436B2, Mitsubishi Materials: ED köşe kalınlığı (2014)](https://patents.google.com/patent/US9947436)
- [US12278025B2, Mitsubishi Materials: ED PAI arayüz oksidi (2019)](https://patents.google.com/patent/US12278025)
- [US10510459B2, Essex: hairpin üzerinde parylene (2016)](https://patents.google.com/patent/US10510459)
- [US6261437B1, ABB: anodize sargı teli (1996)](https://patents.google.com/patent/US6261437)
- [US12119141B2, Dana TM4: busbar epoksi kaplama (2020)](https://patents.google.com/patent/US12119141)
