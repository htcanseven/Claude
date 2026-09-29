# 2. Arıza Türleri ve Akım Spektrumundaki İmzaları

[← Ana yol haritası](README.md)

Bu dosya **Aşama 2**'nin ayrıntılarını içerir. Her arıza türü için dört başlık var:
1. Fiziksel mekanizma
2. Akım spektrumundaki karakteristik frekans formülü
3. Tuzaklar ve karışıklıklar
4. Temel makaleler

**Doğrulama**
- Formüller en az bir yetkili kaynağa karşı kontrol edildi.
- **(TM)** işareti, formülün ya da ifadenin makalenin **tam metninde** kontrol edildiğini gösterir.
- Kısmen doğrulanabilenler ayrıca belirtildi.

**Gösterim**
- **Erişim:** `Açık`, `Ücretsiz kopya`, `Ücretli`.
- **Seviye:** **B** başlangıç, **O** orta, **İ** ileri.

> ⚠ **Kaçınılacak kaynak:** Culbert & Rhodes, *IEEE TIA* 43(2), 2007 makalesinde IEEE'nin "Notice of Violation of IEEE Publication Principles" notu var. Bu makaleye atıf yapmayın.

---

## Semboller

| Sembol | Anlamı |
|---|---|
| f_s | Besleme (şebeke, temel) frekansı |
| s | Kayma = (n_senk − n_r)/n_senk |
| p | Kutup **çifti** sayısı |
| f_r | Mil dönme frekansı = (1 − s)·f_s/p |
| k, m, n | Tam sayı indisler |
| R | Rotor çubuk (oluk) sayısı |
| n_d | Eksantriklik derecesi (0 = statik; 1, 2, … = dinamik) |
| ν | Stator zaman harmoniği mertebesi (1, 3, 5, …) |
| N_b, D_b, D_c, β | Rulmandaki bilye sayısı, bilye çapı, hatve (pitch) çapı, temas açısı |
| f_v | Rulmanın karakteristik titreşim frekansı |
| f_osc | Yük tork salınımının frekansı |

---

## Özet tablo

| Arıza | Akım spektrumundaki imza | Temel kaynaklar (açık erişimliler **kalın**) |
|---|---|---|
| Kırık rotor çubuğu / uç halka | (1 ± 2ks)·f_s; üst harmoniklerde f_s·[k(1−s)/p ± s]; tork, güç ve \|i_s\|'de 2ks·f_s | Kliman 1988; Filippetti 1998; Bellini 2001; **Riera-Guasp 2010**; **Bonet-Jara 2021** |
| Eksantriklik: oluk harmonikleri (statik n_d = 0, dinamik n_d ≥ 1) | f_s·[(kR ± n_d)(1−s)/p ± ν] | Cameron 1986; Nandi 2001; **MERL TR2024-119** |
| Eksantriklik: karma, düşük frekanslı | f_s·[1 ± k(1−s)/p] = f_s ± k·f_r | Dorrell 1997; Nandi 2002; **Bonet-Jara 2021** |
| Rulman (tek noktalı hasar) | \|f_s ± m·f_v\|, f_v ∈ {BPFO, BPFI, BSF, FTF}. İç bilezik için ayrıca f_s ± f_r ± k·BPFI | Schoen 1995; Blodt 2008; Stack 2004; Immovilli 2010; **Leite 2017**; **Lessmeier 2016** |
| Stator sarımlar arası kısa devre (asenkron motor) | f_s·[k ± n(1−s)/p], k = 1, 3; n = 1…2p−1 *(kısmen doğrulandı)*; negatif bileşen akımı I₂; Park vektörü elipsi; EPVA'da 2f_s çizgisi | Penman 1994; Thomson 2001; Kliman 1996; Cruz 2001; **Cardoso 1999** |
| Yük ve mekanik arızalar | f_s ± k·f_osc; dengesizlik ve hizasızlık için f_s ± k·f_r; dişli kutusu için f_s ± k·f_mesh | Blodt 2006; Kia 2009; Kral 2004; Obaid 2003; **Bravo-Imaz 2014** |
| PMSM rotor arızaları (eksantriklik, demanyetizasyon, kırık mıknatıs) | f_s·(1 ± k/p) = f_s ± k·f_r (yalnızca tek mertebeleri kullanan varyant da var). **Düzgün** demanyetizasyon yeni çizgi üretmez | Le Roux 2007; Ebrahimi 2009; Ruiz 2009; **Pietrzak 2023** |
| PMSM sarımlar arası kısa devre | f_s'de I₂, büyüyen 3f_s bileşeni, i_q'da 2. harmonik | Kim 2011; Gandhi 2011; **Pietrzak 2022** |
| DFIG eksantrikliği | Statorda f_s ± k·f_r; rotorda s·f_s ± k·f_r | Stefani 2008; Gritli 2013; **Delfa-Baena 2025** |
| Kapalı çevrim / VFD | FOC'ta i_d'de 2f_s (stator arızası) ve 2s·f_s (rotor arızası); arıza yan bantları inverter harmoniklerinin çevresinde de oluşur | Bellini 2000; Akın 2008; Tallam 2003; **Fernández-Cavero 2017** |

---

## (a) Kırık rotor çubuğu ve uç halka arızaları (sincap kafesli asenkron motor)

### Mekanizma
- Kırık ya da çatlak bir çubuk (veya uç halka parçası) rotor MMF'ini asimetrik yapar.
- Normal ileri alanın yanında, rotora göre −s·f_s frekansında dönen bir **geri alan** oluşur. Stator bu alanı **(1−2s)f_s** frekansında görür; bu, alt yan banttır.
- Bu akım ana akıyla etkileşerek **2s·f_s**'de bir tork titreşimi üretir.
- Tork titreşiminin yol açtığı hız dalgalanması, büyüklüğü eylemsizliğe bağlı olarak **(1+2s)f_s** bileşenini ve (1±2ks)f_s ailesini doğurur (Filippetti 1998; Bellini 2001).
- Açık bir uç halka da aynı imzayı verir (Kliman 1988).

### İmza
- Ana yan bantlar: **f_brb = (1 ± 2ks)·f_s**, k = 1, 2, 3, … (TM: Bonet-Jara 2021 denklem 1; Antonino-Daviu 2006).
- Üst MMF harmoniklerinin çevresinde: f = f_s·[k(1−s)/p ± s] (TM: Chisedzi & Muteba, *Sensors* 23:9079, 2023). Sık verilen "k/p = 1, 5, 7, 11, 13…" kümesi *doğrulanamadı*.
- Tork, anlık güç ve stator akımı uzay vektörünün modülünde bir **2s·f_s** çizgisi görünür (Bellini 2001).

### Şiddet için pratik kurallar
Aşağıdaki dB değerleri, temel bileşen (f_s) ile **(1−2s)f_s** yan bandı arasındaki farktır.

| f_s'nin kaç dB altında? | Durum | Eylem |
|---|---|---|
| > 60 | Mükemmel | — |
| 54–60 | İyi | — |
| 48–54 | Orta | Trend izleyin |
| 42–48 | Çatlak çubuk / yüksek dirençli bağlantı | Test aralığını kısaltın, trend izleyin |
| 36–42 | Kırık çubuk(lar); titreşimde de görülebilir | Doğrulayın, onarım planlayın |
| 30–36 | Birden çok kırık çubuk / uç halka sorunu | En kısa sürede onarın |
| < 30 | Ciddi | Hemen müdahale edin |

**Kaynaklar ve varyantlar**
- **Tablonun kaynağı:** H. W. Penrose, *Evaluating Induction Motor Rotor Bars with Electrical Signature Analysis*, 2006. Endüstri sunumu, [ücretsiz PDF](https://www.motordoc.org/wp-content/uploads/2019/01/Evaluating-Induction-Motor-Rotor-Bars.pdf) (TM).
  - Tablo sık sık Thomson & Fenger 2001'e atfedilir; bu atıf *doğrulanamadı*.
- **Culbert & Letal (2015):** (1−2s)f_s yan bandı temel bileşenin **45 dB ya da daha az** altındaysa kafes arızası vardır ([PDF](https://irispower.com/wp-content/uploads/2018/06/2015-PCIC-Signature-Analysis-For-On-Line-Motor-Diagnostics.pdf), TM).
- **Araştırma varyantı:**
  - −48 dB'in altı sağlam.
  - −48 ile −36 dB arası bir ya da birkaç kırık veya çatlak çubuk.
  - −36 dB'in üstü birden çok kırık çubuk.
  - Kaynak: Bonet-Jara 2021 (TM). Aynı makale bu sınırların **ampirik** olduğunu vurgular: eşit yan banda sahip iki motorda kırık çubuk sayısı farklı olabilir.
- **PdMA (cihaz üreticisi):** 54 dB'in altı gözlem, 45 dB'in altı dikkat, 36 dB'in altı ciddi. N. Bethel, "Rotor Testing With MCE", [PDF](https://www.pdma.com/pdfs/Articles/Rotortest.pdf) (TM).
- **Saha örneği:** Yan bantlar f_s'nin 38,8 dB ve 37,1 dB altındaydı; sökümde 4 kırık çubuk bulundu ([Iris Power](https://irispower.com/learning-centre/current-signature-test-finds-broken-rotor-bars-air-separation-motor/)).
- *Doğrulanmadı:* dB farkından kırık çubuk sayısı tahmini için sık görülen n ≈ 2R/(10^(N/20) + 2p) formülü. Kullanmadan önce Thomson & Culbert, Bölüm 4'ten kontrol edin.

### Tuzaklar
- **Kayma doğru bilinmeli.** 2 kutuplu 90 kW'lık bir pompa motorunda 3 d/d'lik hız hatası, sağlam motordaki çizgileri "kırık çubuk" gibi gösterdi (Bonet-Jara 2021, TM).
- **Boşta ya da hafif yükte** yan bantlar f_s tepesi ve sızıntısıyla birleşir (Antonino-Daviu 2006; Puche-Panadero 2009).
  - Pratik sonuç: Δf = 1/T. 2s·f_s ≈ 0,5 Hz ise en az 10–20 s kayıt ve yan lobu düşük bir pencere gerekir.
- **Yük ve eylemsizlik** yan bant genliklerini değiştirir.
- **2s·f_s yakınındaki yük salınımları** yanlış alarm üretebilir, ya da faz sönümlemesiyle gerçek arızayı gizleyebilir. Kaynaklar: dişli kutuları, hidrolik kaplinler, kompresörler, pistonlu yükler (Kim 2016; Göktaş & Arkan 2018; Thomson & Culbert Böl. 7–8).
- **Bitişik olmayan kırık çubuklar.**
  - Yaklaşık yarım kutup adımı aralıklı iki kırık çubuk (1−2s)f_s yan bandını tek kırık çubuktaki değerin bile **altına** düşürebilir; hasarlı kafes sağlam görünebilir.
  - Tam bir kutup adımı aralıklı iki çubuk ise yan bandı iki katına çıkarır (Riera-Guasp 2010, TM).
- **Çubuklar arası akımlar** asimetriyi ve yan bantları azaltır (Concari 2008).
- **Rotordaki eksenel hava kanalları** 2s·f_s bileşeni üreterek yanlış alarma yol açabilir, hatta gerçek kırığı maskeleyebilir (Lee 2013).
- **Önce sağlam spektrumu tanıyın:** oluk harmonikleri, doyma harmonikleri (Joksimović 2013).

### Temel makaleler
1. **Kliman, Koegl, Stein, Endicott, Madden (1988).** Noninvasive detection of broken rotor bars in operating induction motors. *IEEE TEC* 3(4):873–879.
   - [doi:10.1109/60.9364](https://doi.org/10.1109/60.9364) · `Ücretli` · **O**
   - Bilgisayar tabanlı ilk MCSA dedektörü: tek bir kırık çubuğa ya da açık uç halkaya duyarlı.
2. **Filippetti, Franceschini, Tassoni, Vas (1998).** AI techniques in induction machines diagnosis including the speed ripple effect. *IEEE TIA* 34(1):98–108.
   - [doi:10.1109/28.658729](https://doi.org/10.1109/28.658729) · `Ücretli` · **İ**
   - Hız dalgalanması etkisini modeller; yükten ve eylemsizlikten bağımsız bir teşhis indeksi önerir.
3. **Bellini, Filippetti, Franceschini, Tassoni, Kliman (2001).** Quantitative evaluation of induction motor broken bars by means of electrical signature analysis. *IEEE TIA* 37(5):1248–1255.
   - [doi:10.1109/28.952499](https://doi.org/10.1109/28.952499) · `Ücretli` · **O–İ**
4. **Thomson & Fenger (2001).** *IEEE Ind. Appl. Mag.* 7(4):26–34.
   - [doi:10.1109/2943.930988](https://doi.org/10.1109/2943.930988) · `Ücretli` · **B**
5. **Riera-Guasp, Cabanas, Antonino-Daviu, Pineda-Sánchez, García (2010).** Influence of nonconsecutive bar breakages in MCSA for the diagnosis of rotor faults in induction motors. *IEEE TEC* 25(1):80–89.
   - [doi:10.1109/TEC.2009.2032622](https://doi.org/10.1109/TEC.2009.2032622) · [Ücretsiz kopya](http://hdl.handle.net/10251/99056) · **O**
6. **Puche-Panadero vd. (2009).** Improved resolution of the MCSA method via Hilbert transform… *IEEE TEC* 24(1):52–59.
   - [doi:10.1109/TEC.2008.2003207](https://doi.org/10.1109/TEC.2008.2003207) · `Ücretli` · **O**
   - Düşük kaymadaki çakışma sorununu demodülasyonla çözer.
7. **Bonet-Jara, Quijano-Lopez, Morinigo-Sotelo, Pons-Llinares (2021).** Sensorless speed estimation for the diagnosis of induction motors via MCSA. Review and commercial devices analysis. *Sensors* 21(15):5037.
   - [doi:10.3390/s21155037](https://doi.org/10.3390/s21155037) · `Açık` · **B–O**
   - **Başlangıç için çok değerli:** formüller, dB kriterleri, kayma hatasının neden yanlış alarm ürettiği ve ticari cihazların zayıf yanları (79 endüstriyel motor).
8. **Thomson & Culbert (2017).** *Current Signature Analysis for Condition Monitoring of Cage Induction Motors*, Wiley-IEEE.
   - [doi:10.1002/9781119175476](https://doi.org/10.1002/9781119175476) · **B–O**
   - İlgili bölümler: Böl. 4 kafes arızaları; Böl. 7–8 salınımlı yükler ve yanlış alarmlar; Böl. 10–11 eksantriklik; Böl. 12 sarım kısa devresi ve rulmanlar için eleştirel değerlendirme; Böl. 13 alınan dersler.

**Ek kaynaklar**
- Concari, Franceschini, Tassoni (2008). *IEEE TIE* 55(12):4156–4166. [doi:10.1109/TIE.2008.2003212](https://doi.org/10.1109/TIE.2008.2003212). Çubuklar arası akımlar.
- Kim, Lee, Park, Kia, Capolino (2016). *IEEE TIA* 52(2):1460–1468. [doi:10.1109/TIA.2015.2508423](https://doi.org/10.1109/TIA.2015.2508423). Düşük frekanslı yük salınımları.
- Göktaş & Arkan (2018). Discerning broken rotor bar failure from low-frequency load torque oscillation in DTC induction motor drives. *Trans. Inst. Meas. Control* 40(1):279–286. [doi:10.1177/0142331216654964](https://doi.org/10.1177/0142331216654964).
- Lee vd. (2013). *IEEE TIA* 49(5):2024–2033. [doi:10.1109/TIA.2013.2259132](https://doi.org/10.1109/TIA.2013.2259132). Eksenel hava kanalları.
- Sizov, Sayed-Ahmed, Yeh, Demerdash (2009). *IEEE TIE* 56(11):4627–4641. [doi:10.1109/TIE.2008.2011341](https://doi.org/10.1109/TIE.2008.2011341). Bitişik ve bitişik olmayan kırık çubuklar.
- Halder vd. (2022). *Energies* 15(22):8569. [doi:10.3390/en15228569](https://doi.org/10.3390/en15228569) · `Açık`. MCSA ve kırık çubuk derlemesi.

---

## (b) Hava aralığı eksantrikliği: statik, dinamik, karma

### Mekanizma
- **Statik eksantriklik:** en küçük hava aralığının konumu uzayda sabittir. Nedenleri: stator ovalliği, yanlış yerleştirilmiş kapaklar ya da rulmanlar.
- **Dinamik eksantriklik:** en küçük aralık rotorla birlikte döner. Nedenleri: eğik mil, aşınmış rulman, rotor ovalliği.
- **Karma eksantriklik:** ikisi birlikte. İmalat toleransları ve kaplin hizasızlığı yüzünden neredeyse her motorda bir miktar bulunur (Bonet-Jara 2021).
- Düzgün olmayan aralık hava aralığı permeansını modüle eder. Rotor oluklarıyla birlikte ek akı dalgaları ve akım bileşenleri oluşur.

### İmza
- **Rotor oluk ve eksantriklik harmonikleri:** f = f_s·[(kR ± n_d)(1−s)/p ± ν].
  - k = 1, 2, 3, …; statikte n_d = 0 (temel oluk harmonikleri), dinamikte n_d = 1, 2, 3, …; ν = 1, 3, 5, …
  - TM: Bonet-Jara 2021 denklem 2; D. Liu & S. Tsuruta, MERL TR2024-119, 2024, denklem 3 ([ücretsiz PDF](https://www.merl.com/publications/docs/TR2024-119.pdf)).
- **Karma eksantriklik, düşük frekanslı çizgiler:** f = f_s·[1 ± k(1−s)/p] = f_s ± k·f_r (TM: Bonet-Jara 2021 denklem 3).

### Tuzaklar
- **Oluk harmonikleri yalnızca belirli R–p kombinasyonlarında oluşur** (Nandi 2001; genel kurallar Joksimović 2013'te). Motor sahibi R'yi çoğu zaman bilmez.
- **f_s ± f_r çizgileri hem statik hem dinamik eksantriklik gerektirir** (Dorrell 1997; Nandi 2002).
- **Aynı f_s ± f_r çizgileri başka nedenlerle de oluşur:** mekanik dengesizlik, hizasızlık ve f_r frekanslı yük torku (Kral 2004; Obaid 2003). Neredeyse her motorda bulundukları için **mutlak eşik yerine trend** izleyin.
- **2 kutuplu makineler.**
  - Karma eksantriklik çizgileri 0 Hz'e ve 2f_s'ye çok yakın düşer; oradaki hızdan bağımsız harmonikler tarafından maskelenir.
  - Kayma aralıkları dar olduğu için kayma kestirim hataları büyür (Bonet-Jara 2021).
- **Yük seviyesi**, imza genliklerinde eksantriklik derecesini taklit edebilir (Faiz 2009).
- **Statik ve dinamik eksantriklik**, yalnızca etiket bilgisiyle yapılan klasik MCSA ile birbirinden ayrılamaz (Thomson & Culbert Böl. 8).

### Temel makaleler
1. **Cameron, Thomson, Dow (1986).** Vibration and current monitoring for detecting airgap eccentricity in large induction motors. *IEE Proc. B* 133(3):155ff.
   - [doi:10.1049/ip-b.1986.0022](https://doi.org/10.1049/ip-b.1986.0022) · `Ücretli` · **O**
   - Temel MMF–permeans teorisi; santral motorlarında doğrulanmış.
2. **Dorrell, Thomson, Roach (1997).** *IEEE TIA* 33(1):24–34.
   - [doi:10.1109/28.567073](https://doi.org/10.1109/28.567073) · `Ücretli` · **İ**
3. **Nandi, Ahmed, Toliyat (2001).** Detection of rotor slot and other eccentricity related harmonics… *IEEE TEC* 16(3):253–260.
   - [doi:10.1109/60.937205](https://doi.org/10.1109/60.937205) · `Ücretli` · **İ**
   - Hangi R–p kombinasyonlarında oluk harmoniği oluştuğu.
4. **Nandi, Bharadwaj, Toliyat (2002).** Performance analysis of a three-phase induction motor under mixed eccentricity condition. *IEEE TEC* 17(3):392–399.
   - [doi:10.1109/TEC.2002.801995](https://doi.org/10.1109/TEC.2002.801995) · `Ücretli` · **İ**
   - Değiştirilmiş sargı fonksiyonu modeli; **simülasyon için iyi bir şablon**.
5. **Thomson & Barbour (1998).** *IEEE TEC* 13(4):347–357.
   - [doi:10.1109/60.736320](https://doi.org/10.1109/60.736320) · `Ücretli` · **İ**
   - Statik eksantriklik seviyesine göre çizgi frekans ve genliklerinin FEM ile tahmini.
6. **Faiz & Ojaghi (2009).** Different indexes for eccentricity faults diagnosis in three-phase squirrel-cage induction motors: a review. *Mechatronics* 19(1):2–13.
   - [doi:10.1016/j.mechatronics.2008.07.004](https://doi.org/10.1016/j.mechatronics.2008.07.004) · `Ücretli` · **B–O**

**Ek kaynaklar**
- Faiz, Ebrahimi, Akin, Toliyat (2009). *IEEE Trans. Magn.* 45(3):1764–1767. [doi:10.1109/TMAG.2009.2012812](https://doi.org/10.1109/TMAG.2009.2012812). Yük seviyesinin etkisi.
- Faiz & Moosavi (2016). Eccentricity fault detection – from induction machines to DFIG: a review. *Renew. Sustain. Energy Rev.* 55:169–179. [doi:10.1016/j.rser.2015.10.113](https://doi.org/10.1016/j.rser.2015.10.113).
- Joksimović, Riger, Wolbank, Perić, Vašak (2013). Stator-current spectrum signature of healthy cage rotor induction machines. *IEEE TIE* 60(9):4025–4033. [doi:10.1109/TIE.2012.2236995](https://doi.org/10.1109/TIE.2012.2236995). **Sağlam spektrumda ne olduğunu** gösteren referans.
- Liu, Zhang, He, Huang (2021). *Energies* 14(14):4296 · `Açık`. Eksantrikliğin modellenmesi ve teşhisi üzerine derleme.

---

## (c) Rulman arızaları

### Mekanizma
- Yerel bir hasar, kinematik bir f_v frekansında darbeler üretir. Bu darbeler iki yoldan etki eder (Schoen 1995; Blodt 2008):
  - Rotoru radyal olarak kaydırır. Bu, eksantrikliğe benzer bir **genlik modülasyonu** yaratır.
  - Yük torkunu salındırır. Bu da akımda bir **faz modülasyonu** yaratır.
- Her iki etki de f_s çevresinde yan bantlar oluşturur.
- Yayılı aşınma ("genel pürüzlülük") geniş bantlı, periyodik olmayan etkiler üretir; temiz çizgiler görünmez (Stack 2004).

### İmza
- **Karakteristik frekanslar:**
  - Dış bilezik: **BPFO** = (N_b/2)·f_r·[1 − (D_b/D_c)·cos β]
  - İç bilezik: **BPFI** = (N_b/2)·f_r·[1 + (D_b/D_c)·cos β]
  - Kafes: **FTF** = (f_r/2)·[1 − (D_b/D_c)·cos β]
  - Bilye: **BSF** = (D_c/(2D_b))·f_r·[1 − (D_b/D_c)²·cos²β]
  - TM: Ruiz-Sarrio, Antonino-Daviu, Martis, *Sensors* 24(21):6935, 2024, [doi:10.3390/s24216935](https://doi.org/10.3390/s24216935).
- **Akımda:** f_bng = |f_s ± m·f_v|, m = 1, 2, 3, … (Schoen 1995 modeli).
- **Blodt (2008) inceltmesi:** dış bilezikte f_s ± k·BPFO; iç bilezikte f_s ± f_r ± k·BPFI.
- MATLAB'da [`bearingFaultBands`](https://www.mathworks.com/help/predmaint/ref/bearingfaultbands.html) bu bantları sizin için hesaplar.

### Tuzaklar ve tespit edilebilirlik tartışması
- Bileşenler çok küçüktür ve gürültü tabanına yakındır (Leite 2017).
- Genlikleri yüke, hıza ve motor gücüne göre değişir; evrensel bir eşik yoktur (Zhang 2020).
- Sahada doğal olarak oluşan hasarlar ve genel pürüzlülük karakteristik çizgi üretmeyebilir (Zhou 2008; Stack 2004).
- Tork bozucusu olarak modellendiğinde akım, titreşimden daha az duyarlıdır (Immovilli 2010). Akım tabanlı sınıflandırıcılar titreşim tabanlılardan daha düşük başarım gösterir (Lessmeier 2016).
- Sürücülerde, kestirilen hız akımdan daha iyi bir taşıyıcı olabilir (Trajin 2009).
- Eleştirel endüstriyel bakış için Thomson & Culbert Böl. 12'ye, gelişen arızalarla olumlu bir sonuç için Corne 2018'e bakın.

### Temel makaleler
1. **Schoen, Habetler, Kamran, Bartheld (1995).** Motor bearing damage detection using stator current monitoring. *IEEE TIA* 31(6):1274–1279.
   - [doi:10.1109/28.475697](https://doi.org/10.1109/28.475697) · `Ücretli` · **B–O**
   - Klasik |f_s ± m·f_v| modeli.
2. **Blodt, Granjon, Raison, Rostaing (2008).** Models for bearing damage detection in induction motors using stator current monitoring. *IEEE TIE* 55(4):1813–1822.
   - [doi:10.1109/TIE.2008.917108](https://doi.org/10.1109/TIE.2008.917108) · [HAL'da ücretsiz](https://hal.science/hal-00270747) · **İ**
3. **Stack, Habetler, Harley (2004).** Fault classification and fault signature production for rolling element bearings in electric machines. *IEEE TIA* 40(3):735–739.
   - [doi:10.1109/TIA.2004.827454](https://doi.org/10.1109/TIA.2004.827454) · `Ücretli` · **B–O**
   - Tek noktalı hasar ile genel pürüzlülüğün ayrımı.
4. **Immovilli, Bellini, Rubini, Tassoni (2010).** Diagnosis of bearing faults in induction machines by vibration or current signals: a critical comparison. *IEEE TIA* 46(4):1350–1359.
   - [doi:10.1109/TIA.2010.2049623](https://doi.org/10.1109/TIA.2010.2049623) · `Ücretli` · **O**
   - Tespit edilebilirlik tartışmasının anahtar makalesi.
5. **Leite vd. (2015).** Detection of localized bearing faults in induction machines by spectral kurtosis and envelope analysis of stator current. *IEEE TIE* 62(3):1855–1865.
   - [doi:10.1109/TIE.2014.2345330](https://doi.org/10.1109/TIE.2014.2345330) · `Ücretli` · **İ**
   - Aynı grubun açık erişimli kitap bölümü: IntechOpen 2017, [doi:10.5772/67145](https://doi.org/10.5772/67145) · **B–O**.
6. **Lessmeier, Kimotho, Zimmer, Sextro (2016).** Condition monitoring of bearing damage in electromechanical drive systems by using motor current signals… *PHM Society European Conf.* 3(1).
   - [doi:10.36001/phme.2016.v3i1.1577](https://doi.org/10.36001/phme.2016.v3i1.1577) · `Açık` · **B**
   - Paderborn akım veri seti; MATLAB alıştırmaları için ideal.

**Ek kaynaklar**
- Immovilli, Cocconcelli, Bellini, Rubini (2009). *IEEE TIE* 56(11):4710–4717. [doi:10.1109/TIE.2009.2025288](https://doi.org/10.1109/TIE.2009.2025288). Genel pürüzlülük ve spektral kurtosis.
- Zhou, Habetler, Harley (2008). *IEEE TIE* 55(12):4260–4269. [doi:10.1109/TIE.2008.2005018](https://doi.org/10.1109/TIE.2008.2005018). Gürültü giderme.
- Frosini & Bassi (2010). *IEEE TIE* 57(1):244–251. [doi:10.1109/TIE.2009.2026770](https://doi.org/10.1109/TIE.2009.2026770).
- Trajin, Regnier, Faucher (2009). *IEEE TIE* 56(11):4700–4709. [doi:10.1109/TIE.2009.2023630](https://doi.org/10.1109/TIE.2009.2023630).
- Corne vd. (2018). *MSSP* 107:168–182. [doi:10.1016/j.ymssp.2017.12.010](https://doi.org/10.1016/j.ymssp.2017.12.010).
- Zhang, Zhang, Wang, Habetler (2020). *IEEE Access* 8:29857–29881 · `Açık`.

---

## (d) Stator sarımlar arası kısa devre

### Mekanizma
- Sarım yalıtımı bozulur ve büyük bir dolaşım akımının aktığı kısa devreli bir halka oluşur.
- Yerel ısınma hasarı hızla yayar. Bu nedenle tespit **erken** yapılmalıdır (Riera-Guasp 2015).
- Arızalı faz etkin sarım kaybeder ve makine asimetrik hale gelir:
  - **Negatif bileşen akımı** ortaya çıkar.
  - Mevcut harmoniklerin genlikleri değişir.

### İmza
- **Frekans kümesi:** f_st = f_s·[k ± n(1−s)/p], k = 1, 3; n = 1, 2, …, 2p−1. *Kısmen doğrulandı.*
  - Bu ifadenin kökeni eksenel akı analizidir (Penman 1994). Akım için birincil kaynak (Thomson 2001) ücretli olduğundan kontrol edilemedi.
  - Stavrou 2001'e göre akımda en güvenilir gösterge, dönme frekansının alt yan bandı f_s − f_r'dir.
- **Negatif bileşen akımı:** I₂ = (I_a + a²·I_b + a·I_c)/3, a = e^(j2π/3) (Kliman 1996; Bouzid 2013).
- **Park vektörü:** i_D = √(2/3)·i_a − (1/√6)·(i_b + i_c) ve i_Q = (1/√2)·(i_b − i_c).
  - Sağlam motorda i_D–i_Q deseni bir **çemberdir**; arızada **elipse** dönüşür.
  - Elipsliğin büyüklüğü arıza şiddetini, eksenin yönü arızalı fazı gösterir (Cardoso 1999, TM).
- **EPVA:** |i_D + j·i_Q| modülünün spektrumunda **2f_s** çizgisi belirir (Cruz & Cardoso 2001).

### Tuzaklar
- Kafesli rotorlu motorda **yeni** akım frekansı oluşmaz; yalnızca mevcut bileşenler büyür (Joksimović & Penman 2000). Bu yüzden sağlam durumun kaydına (baseline) ya da trende ihtiyaç vardır.
- **Besleme gerilimi dengesizliği** ve doğal asimetri de negatif bileşen ve EPVA'da 2f_s çizgisi üretir.
  - Gerilimleri de ölçün ya da bileşen empedansı yaklaşımını kullanın (Kliman 1996; Lee 2003; Bouzid 2013).
- Kapalı çevrim sürücüler için bkz. (g).
- Thomson & Culbert Böl. 12, sarım kısa devresinde MCSA'nın ne kadar işe yaradığını eleştirel olarak tartışır.

### Temel makaleler
1. **Penman, Sedding, Lloyd, Fink (1994).** Detection and location of interturn short circuits in the stator windings of operating motors. *IEEE TEC* 9(4):652–658.
   - [doi:10.1109/60.368345](https://doi.org/10.1109/60.368345) · `Ücretli` · **İ**
2. **Thomson (2001).** On-line MCSA to diagnose shorted turns in low voltage stator windings of 3-phase induction motors prior to failure. *IEEE IEMDC 2001*, 891–898.
   - [doi:10.1109/IEMDC.2001.939425](https://doi.org/10.1109/IEMDC.2001.939425) · `Ücretli` · **O**
3. **Joksimović & Penman (2000).** The detection of inter-turn short circuits in the stator windings of operating motors. *IEEE TIE* 47(5):1078–1084.
   - [doi:10.1109/41.873216](https://doi.org/10.1109/41.873216) · `Ücretli` · **İ**
   - "Yeni frekans oluşmaz" sonucu.
4. **Cardoso, Cruz, Fonseca (1999).** Inter-turn stator winding fault diagnosis in three-phase induction motors, by Park's vector approach. *IEEE TEC* 14(3):595–598.
   - [doi:10.1109/60.790920](https://doi.org/10.1109/60.790920) · [Ücretsiz PDF](https://estudogeral.uc.pt/bitstream/10316/12916/1/Inter-turn%20stator%20winding%20fault%20diagnosis.pdf) · **B**
5. **Cruz & Cardoso (2001).** *IEEE TIA* 37(5):1227–1233.
   - [doi:10.1109/28.952496](https://doi.org/10.1109/28.952496) · `Ücretli` · **O**
   - EPVA'daki 2f_s çizgisi; 5 MW'a kadar motorlar.
6. **Kliman, Premerlani, Koegl, Hoeweler (1996).** A new approach to on-line turn fault detection in AC motors. *IEEE IAS 1996*, 687–693.
   - [doi:10.1109/IAS.1996.557113](https://doi.org/10.1109/IAS.1996.557113) · `Ücretli` · **O**
   - Gerilim dengesizliğine göre düzeltilmiş negatif bileşen yöntemi. 648 sarımdan 1'indeki kısa devreyi 2 periyotta tespit ediyor.

**Ek kaynaklar**
- Stavrou, Sedding, Penman (2001). *IEEE TEC* 16(1):32–37. [doi:10.1109/60.911400](https://doi.org/10.1109/60.911400).
- Lee, Tallam, Habetler (2003). *IEEE TPEL* 18(3):865–872. [doi:10.1109/TPEL.2003.810848](https://doi.org/10.1109/TPEL.2003.810848). Bileşen empedans matrisi.
- Tallam, Habetler, Harley (2002). *IEEE TIA* 38(3):632–637. [doi:10.1109/TIA.2002.1003411](https://doi.org/10.1109/TIA.2002.1003411). **Simulink'e hazır durum uzayı modeli.**
- Tallam vd. (2007). A survey of methods for detection of stator-related faults in induction machines. *IEEE TIA* 43(4):920–933. [doi:10.1109/TIA.2007.900448](https://doi.org/10.1109/TIA.2007.900448) · **B–O**.
- Grubic, Aller, Lu, Habetler (2008). *IEEE TIE* 55(12):4127–4136. [doi:10.1109/TIE.2008.2004665](https://doi.org/10.1109/TIE.2008.2004665) · **B**.
- Gandhi, Corrigan, Parsa (2011). *IEEE TIE* 58(5):1564–1575. [doi:10.1109/TIE.2010.2089937](https://doi.org/10.1109/TIE.2010.2089937). Asenkron ve PM makineler.
- Siddique, Yadava, Singh (2005). *IEEE TEC* 20(1):106–114. [doi:10.1109/TEC.2004.837304](https://doi.org/10.1109/TEC.2004.837304) · **B**.
- Bouzid & Champenois (2013). *IEEE TIE* 60(9):4093–4102. [doi:10.1109/TIE.2012.2235392](https://doi.org/10.1109/TIE.2012.2235392).

---

## (e) MCSA ile görülebilen mekanik ve yük tarafı arızaları

### Mekanizma
- Yük tarafındaki arızalar karakteristik bir frekansta tork ve hız salınımı yaratır. Bu salınım akımı faz modülasyonuna uğratır ve f_s çevresinde yan bantlar oluşturur (Blodt 2006).
- Hizasızlık ve dengesizlik ayrıca dinamik eksantriklik ve radyal kuvvet ekler.

### İmza
- **Yük tork salınımı:** f_s ± k·f_osc (Blodt 2006).
- **Dengesizlik ve hizasızlık:** f_s ± k·f_r (Kral 2004; Obaid 2003).
- **Dişli kutusu:** f_s ± k·f_r,giriş, f_s ± k·f_r,çıkış ve f_s ± k·f_mesh; burada f_mesh = Z·f_r ve Z diş sayısıdır (Kia 2009).
- **Pompa kavitasyonu:** kapalı formda bir çizgi yerine, elektriksel olarak kestirilen torkun spektrumu kullanılır (Stopa 2014).

### Tuzaklar
- Bu çizgiler eksantriklik çizgileri f_s ± f_r ile çakışır.
- 2s·f_s yakınındaki düşük frekanslı salınımlar kırık çubuğu taklit eder (Kim 2016; Thomson & Culbert Böl. 7–8).
- İmzalar düşük hızda küçülür. Yine de Obaid 2003, VFD altında 150 d/d'de tespit yapabilmiştir.

### Temel makaleler
1. **Blodt, Chabert, Regnier, Faucher (2006).** Mechanical load fault detection in induction motors by stator current time-frequency analysis. *IEEE TIA* 42(6):1454–1463.
   - [doi:10.1109/TIA.2006.882631](https://doi.org/10.1109/TIA.2006.882631) · **O**
2. **Kia, Henao, Capolino (2009).** Analytical and experimental study of gearbox mechanical effect on the induction machine stator current signature. *IEEE TIA* 45(4):1405–1415.
   - [doi:10.1109/TIA.2009.2023503](https://doi.org/10.1109/TIA.2009.2023503) · **O**
3. **Kia, Henao, Capolino (2015).** *IEEE TIE* 62(3):1866–1878.
   - [doi:10.1109/TIE.2014.2360068](https://doi.org/10.1109/TIE.2014.2360068) · **İ**
   - Dişli yüzey hasarı ve stator akımı uzay vektörü.
4. **Obaid, Habetler, Tallam (2003).** Detecting load unbalance and shaft misalignment using stator current in inverter-driven induction motors. *IEEE IEMDC 2003*.
   - [doi:10.1109/IEMDC.2003.1210643](https://doi.org/10.1109/IEMDC.2003.1210643) · **B–O**
5. **Kral, Habetler, Harley (2004).** *IEEE TIA* 40(4):1101–1106.
   - [doi:10.1109/TIA.2004.830762](https://doi.org/10.1109/TIA.2004.830762) · **O**
6. **Bravo-Imaz vd. (2014).** Motor current signature analysis for gearbox health monitoring… *PHM Society European Conf.* 2(1).
   - [doi:10.36001/phme.2014.v2i1.1486](https://doi.org/10.36001/phme.2014.v2i1.1486) · `Açık` · **B**

**Ek kaynaklar**
- Verucchi vd. (2016). *MSSP* 80:570–581. [doi:10.1016/j.ymssp.2016.04.035](https://doi.org/10.1016/j.ymssp.2016.04.035). Esnek kaplinde hizasızlık.
- Stopa, Cardoso Filho, Martinez (2014). *IEEE TIA* 50(1):120–126. [doi:10.1109/TIA.2013.2267709](https://doi.org/10.1109/TIA.2013.2267709). Kavitasyon.
- Gelman, Mondal, Wright (2026). *Technologies* 14(4):214. [doi:10.3390/technologies14040214](https://doi.org/10.3390/technologies14040214) · `Açık`. Konveyör kayışı gevşekliği.

---

## (f) PMSM, BLDC, senkron makineler ve DFIG

### Mekanizma
- PMSM'de kayma sıfırdır: f_r = f_s/p.
- Rotorla dönen asimetriler akıyı f_r frekansında modüle eder. Örnekler: kısmi demanyetizasyon, kırık mıknatıs, dinamik ya da karma eksantriklik.
- **Düzgün** demanyetizasyon alanı simetrik bırakır. Yalnızca zıt EMK'yı düşürür, dolayısıyla aynı tork için daha fazla akım çekilir.
- PM makinede sarım kısa devresi mıknatısların zıt EMK'sı tarafından beslenir; motor dursa bile tehlikelidir.

### İmza
- **Rotor arızaları:** f = f_s·(1 ± k/p) = f_s ± k·f_r, k = 1, 2, 3, … (TM: Pietrzak & Wolkiewicz 2023 denklem 1).
  - Bazı yazarlar yalnızca tek mertebeleri kullanır: f_s·[1 ± (2k−1)/p].
- **Düzgün demanyetizasyon:** yeni çizgi oluşmaz; yalnızca tek harmonikler (2k−1)f_s değişir. Akı ya da zıt EMK kestirimiyle tespit edilir (Le Roux 2007).
- **PMSM sarım kısa devresi:** f_s'de negatif bileşen, büyüyen 3f_s (Pietrzak & Wolkiewicz 2022, TM); i_q'da 2. harmonik (Kim 2011).
- **DFIG eksantrikliği:** statorda f_s ± k·f_r, rotorda s·f_s ± k·f_r (Delfa-Baena 2025, TM).

### Tuzak
- Kırık mıknatıs ile statik eksantriklik çok benzer desenler verir (Göktaş, Zafarani & Akın 2016).
- Servo ve elektrikli araç motorlarının çoğu durağan olmayan koşullarda çalışır; zaman–frekans yöntemleri gerekir.

### Temel makaleler
1. **Le Roux, Harley, Habetler (2007).** Detecting rotor faults in low power permanent magnet synchronous machines. *IEEE TPEL* 22(1):322–328.
   - [doi:10.1109/TPEL.2006.886620](https://doi.org/10.1109/TPEL.2006.886620) · **O**
2. **Ebrahimi, Faiz, Roshtkhari (2009).** Static-, dynamic-, and mixed-eccentricity fault diagnoses in permanent-magnet synchronous motors. *IEEE TIE* 56(11):4727–4739.
   - [doi:10.1109/TIE.2009.2029577](https://doi.org/10.1109/TIE.2009.2029577) · **İ**
3. **Ruiz, Rosero, Espinosa, Romeral (2009).** Detection of demagnetization faults in PMSMs under nonstationary conditions. *IEEE Trans. Magn.* 45(7):2961–2969.
   - [doi:10.1109/TMAG.2009.2015942](https://doi.org/10.1109/TMAG.2009.2015942) · **İ**
4. **Rajagopalan, Aller, Restrepo, Habetler, Harley (2006).** Detection of rotor faults in brushless DC motors operating under nonstationary conditions. *IEEE TIA* 42(6):1464–1477.
   - [doi:10.1109/TIA.2006.882613](https://doi.org/10.1109/TIA.2006.882613) · **İ**
5. **Faiz & Nejadi-Koti (2016).** Demagnetization fault indexes in permanent magnet synchronous motors—an overview. *IEEE Trans. Magn.* 52(4):1–11.
   - [doi:10.1109/TMAG.2015.2480379](https://doi.org/10.1109/TMAG.2015.2480379) · **B–O**
6. **Pietrzak & Wolkiewicz (2023).** Demagnetization fault diagnosis of PMSMs based on stator current signal processing and machine learning algorithms. *Sensors* 23(4):1757.
   - [doi:10.3390/s23041757](https://doi.org/10.3390/s23041757) · `Açık` · **B–O**

**Ek kaynaklar**
- Choi vd. (2018). Fault diagnosis techniques for permanent magnet AC machine and drives—a review of current state of the art. *IEEE TTE* 4(2):444–463. [doi:10.1109/TTE.2018.2819627](https://doi.org/10.1109/TTE.2018.2819627) · **B**.
- Rosero, Cusido, Garcia, Ortega, Romeral (2006). *IECON 2006*, 964–969. [doi:10.1109/IECON.2006.347599](https://doi.org/10.1109/IECON.2006.347599). PMSM'de rulman ve eksantriklik.
- Göktaş, Zafarani, Akın (2016). *IEEE TEC* 31(2):578–587. [doi:10.1109/TEC.2015.2512602](https://doi.org/10.1109/TEC.2015.2512602).
- Kim (2011). *IEEE TIE* 58(6):2565–2568. [doi:10.1109/TIE.2010.2060463](https://doi.org/10.1109/TIE.2010.2060463).
- Pietrzak & Wolkiewicz (2022). *Sensors* 22(24):9668. [doi:10.3390/s22249668](https://doi.org/10.3390/s22249668) · `Açık`.
- Melecio, Djurović, Schofield (2019). *J. Eng. (IET)* 2019(17):4127–4132. [doi:10.1049/joe.2018.8048](https://doi.org/10.1049/joe.2018.8048) · `Açık`. FEM ile demanyetizasyon imzaları.
- Chen vd. (2019). *Appl. Sci.* 9(10):2116 · `Açık`. PMSM arızaları derlemesi.
- **DFIG, rotoru sargılı ve senkron makineler:**
  - Stefani vd. (2008). *IEEE TIA* 44(6):1711–1721. [doi:10.1109/TIA.2008.2006322](https://doi.org/10.1109/TIA.2008.2006322).
  - Gritli vd. (2013). *IEEE TIE* 60(9):4012–4024. [doi:10.1109/TIE.2012.2236992](https://doi.org/10.1109/TIE.2012.2236992).
  - Neti & Nandi (2009). *IEEE TIA* 45(3):911–920. [doi:10.1109/TIA.2009.2018905](https://doi.org/10.1109/TIA.2009.2018905).
  - Delfa-Baena vd. (2025). *Sensors* 25(24):7451. [doi:10.3390/s25247451](https://doi.org/10.3390/s25247451) · `Açık`.

---

## (g) Besleme ve sürücü etkileri

- **Kapalı çevrim, alan yönlendirmeli kontrol (FOC).**
  - Akım denetleyicileri akımdaki arıza bileşenlerini bastırır.
  - Bellini 2000'e göre i_d spektrumundaki 2f_s (stator arızası) ve 2s·f_s (rotor arızası) çizgileri denetleyici parametrelerinden büyük ölçüde bağımsızdır.
- **Kapalı çevrim sürücü, akım kaynağı gibi davranır.** Bu yüzden gerilimleri de izleyin (Tallam 2003).
  - DFOC'ta denetleyici çıkışlarında DC'de ve 2f_s'de değişim görülür (Wolkiewicz 2016).
  - DTC'de v_q/i_q spektrumlarına bakın (Göktaş & Arkan 2018).
  - Hangi değişkenin en yararlı olduğunu hız döngüsünün bant genişliği belirler (Cruz & Cardoso 2006).
- **PWM besleme.**
  - Spektrum genişler (Ruzimov 2025).
  - Düşük mertebeli inverter harmonikleri de kendi arıza yan bantlarını taşır; kırık çubuk çift harmonikleri artırır (Akın 2008).
- **Gerilim dengesizliği** tıpkı sarım arızası gibi negatif bileşen akımı üretir.
  - Dengesizliği ölçün (Laadjal 2023) ya da dengesizlikten etkilenmeyen göstergeler kullanın (Lee 2003; Kliman 1996; Bouzid 2013).
  - Gerilim dalgalanmaları ve salınımlı yükler de (1±2s)f_s çizgilerini taklit eder (Antonino-Daviu 2006).
- **Zamanla değişen hız ya da yük** arıza çizgilerini bulanıklaştırır. Çözümler:
  - denetim sinyalleriyle demodülasyon (Stefani 2009)
  - kalkış geçici rejiminin dalgacık analizi (Antonino-Daviu 2006)
  - kayma–frekans düzlemi (Puche-Panadero 2020)
  - inverter beslemeli geçici rejim için karşılaştırmalı zaman–frekans analizi (Fernández-Cavero 2017)

**Temel makaleler**
1. **Bellini, Filippetti, Franceschini, Tassoni (2000).** Closed-loop control impact on the diagnosis of induction motors faults. *IEEE TIA* 36(5):1318–1329.
   - [doi:10.1109/28.871280](https://doi.org/10.1109/28.871280) · **O**
2. **Akın, Orguner, Toliyat, Rayner (2008).** Low order PWM inverter harmonics contributions to the inverter-fed induction machine fault diagnosis. *IEEE TIE* 55(2):610–619.
   - [doi:10.1109/TIE.2007.911954](https://doi.org/10.1109/TIE.2007.911954) · **O**
3. **Tallam, Habetler, Harley (2003).** Stator winding turn-fault detection for closed-loop induction motor drives. *IEEE TIA* 39(3):720–724.
   - [doi:10.1109/TIA.2003.811784](https://doi.org/10.1109/TIA.2003.811784) · **O**
4. **Stefani, Bellini, Filippetti (2009).** Diagnosis of induction machines' rotor faults in time-varying conditions. *IEEE TIE* 56(11):4548–4556.
   - [doi:10.1109/TIE.2009.2016517](https://doi.org/10.1109/TIE.2009.2016517) · **İ**
5. **Antonino-Daviu, Riera-Guasp, Folch, Palomares (2006).** *IEEE TIA* 42(4):990–996.
   - [doi:10.1109/TIA.2006.876082](https://doi.org/10.1109/TIA.2006.876082) · [Ücretsiz kopya](http://hdl.handle.net/10251/98700) · **O**
6. **Riera-Guasp, Antonino-Daviu, Capolino (2015).** *IEEE TIE* 62(3):1746–1759.
   - [doi:10.1109/TIE.2014.2375853](https://doi.org/10.1109/TIE.2014.2375853) · [Ücretsiz kopya](http://hdl.handle.net/10251/97806) · **B–O**

**Ek kaynaklar**
- Cruz & Cardoso (2006). *IAS 2006*. [doi:10.1109/IAS.2006.256869](https://doi.org/10.1109/IAS.2006.256869).
- Wolkiewicz vd. (2016). *IEEE TIE* 63(4):2517–2528. [doi:10.1109/TIE.2016.2520902](https://doi.org/10.1109/TIE.2016.2520902).
- Fernández-Cavero vd. (2017). *IEEE Access* 5:8048–8063. [doi:10.1109/ACCESS.2017.2702643](https://doi.org/10.1109/ACCESS.2017.2702643) · `Açık`.
- Puche-Panadero vd. (2020). Fault diagnosis in the slip–frequency plane… *Sensors* 20(12):3398. [doi:10.3390/s20123398](https://doi.org/10.3390/s20123398) · `Açık`.
- Ruzimov vd. (2025). *Sensors* 25(22):7045. [doi:10.3390/s25227045](https://doi.org/10.3390/s25227045) · `Açık`. İnverterle beslenen motorda negatif bileşen analiziyle kırık çubuk.
- Laadjal vd. (2023). *Sensors* 23(18):7989. [doi:10.3390/s23187989](https://doi.org/10.3390/s23187989) · `Açık`.

---

## Doğrulanamayan ya da sınırlı ayrıntılar

- dB tablosunun Thomson & Fenger 2001'e atfı. Tablonun kendisi Penrose 2006'da doğrulandı.
- Kırık çubuk sayısı tahmin formülü ve k/p = 1, 5, 7, … kümesi.
- Sarımlar arası kısa devre frekans formülü (kısmen doğrulandı).
- Cameron 1986'nın son sayfası.
