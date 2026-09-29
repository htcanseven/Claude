# 1. Temeller: MCSA'yı Anlamak İçin Okuma Listesi

[← Ana yol haritası](README.md)

Bu dosya, yol haritasının **Aşama 1**'i (konuyu derinlemesine anlamak) için ayrıntılı kaynak listesidir.
Kaynaklar Eylül 2026'da DOI/URL üzerinden doğrulandı. Doğrulanamayan ayrıntılar *(doğrulanmadı)* diye işaretlendi.

**Gösterim.**
- **Erişim:** `Açık` yayıncıda ücretsizdir. `Ücretsiz kopya` yazarın ya da kurumun deposunda ücretsiz bir sürüm olduğunu gösterir. `Ücretli` abonelik ister; bunlara üniversite kütüphanesi üzerinden erişebilirsiniz.
- **Seviye:** **B** başlangıç, **O** orta, **İ** ileri.

> **İpucu:** Ücretli makalelerin çoğuna üniversitenizin IEEE Xplore / ScienceDirect aboneliği ile erişebilirsiniz.
> Ücretsiz sürüm aramak için [Unpaywall](https://unpaywall.org/) tarayıcı eklentisi işe yarar. HAL ve RiuNet (UPV Valencia) depoları da yararlıdır.
> Bazı kurum depoları dosyayı "erişim kısıtlı" tutar. Örneğin IRIS UNIMORE'deki Bellini/Filippetti kopyaları kapalı, RiuNet'teki bazı kopyalar ambargoludur. Bu dosyada "Ücretsiz kopya" diye işaretlenenlerin açık olduğu kontrol edildi.

---

## 1.1 Kısaltma notu: "MSCA" değil, "MCSA"

"MSCA" elektrik makinesi teşhisi literatüründe yerleşik bir kısaltma değildir. Büyük olasılıkla **MCSA — Motor Current Signature Analysis (Motor Akım İmza Analizi)** kastediliyor.
Veri tabanlarında "MSCA" araması çoğunlukla *Marie Skłodowska-Curie Actions* sonuçlarını getirir. Aramalarınızda **MCSA** kullanın.

| Kısaltma | Açılım | Kısa açıklama | Dayanak kaynak |
|---|---|---|---|
| MCSA / CSA | (Motor) Current Signature Analysis | Stator akımının spektrumunda arıza frekanslarını aramak | Kliman & Stein 1992; Thomson & Fenger 2001 |
| ESA | Electrical Signature Analysis | Akıma ek olarak gerilim ve güç de analiz edilir | ISO 20958:2013 |
| MSCSA | Motor **Square** Current Signature Analysis | Akımın **karesinin** spektrumu. Yalnızca akım sensörüyle anlık güce benzer bilgi verir | Pires vd. 2013 |
| IPSA | Instantaneous Power Signature Analysis | Anlık gücün spektrumu | Legowski vd. 1996 |
| PVA / EPVA | (Extended) Park's Vector Approach | Park vektörünün deseni ya da modülünün spektrumu | Cardoso vd. 1999; Cruz & Cardoso 2001 |
| MCA | Motor Circuit Analysis | Motor dururken yapılan çevrimdışı test. ESA ise motor çalışırken yapılır | ABB/Samotics rehberi (§1.7) |

**MSCSA kaynakları.** MSCSA, MCSA'nın niş bir varyantıdır. Tezinizde "ilgili yöntemler" başlığı altında anmaya değer.
- Pires, V.F., Kadivonga, M., Martins, J.F., Pires, A.J. (2013). Motor square current signature analysis for induction motor rotor diagnosis. *Measurement* 46(2):942–948.
  - [doi:10.1016/j.measurement.2012.10.008](https://doi.org/10.1016/j.measurement.2012.10.008) · `Ücretli` · **O**
  - MSCSA'nın ilk önerildiği makale; kırık çubuk ve eksantriklik üzerinde test edilmiş.
- Pires, Foito, Martins, Pires (2015). Detection of stator winding fault in induction motors using a motor square current signature analysis (MSCSA). *IEEE POWERENG 2015*, 507–512.
  - [doi:10.1109/POWERENG.2015.7266369](https://doi.org/10.1109/POWERENG.2015.7266369) · `Ücretli` · **O**
- Pires, Martins, Pires, Rodrigues (2016). Induction motor broken bar fault detection based on MCSA, MSCSA and PCA: a comparative study. *CPE-POWERENG 2016*, 298–303.
  - [doi:10.1109/CPE.2016.7544203](https://doi.org/10.1109/CPE.2016.7544203) · `Ücretli` · **O**
  - MCSA ile MSCSA'yı doğrudan karşılaştırıyor.
- Pires vd. (2026). A new MSCSA technique for induction motor diagnosis based on the Park transform approach (MSCSA-APT). *Electronics* 15(15):3323.
  - [doi:10.3390/electronics15153323](https://doi.org/10.3390/electronics15153323) · `Açık` · **O**
- Singh, G., Naikan, V.N.A. (2018). Detection of half broken rotor bar fault in VFD driven induction motor drive using motor square current MUSIC analysis. *MSSP* 110:333–348.
  - [doi:10.1016/j.ymssp.2018.03.001](https://doi.org/10.1016/j.ymssp.2018.03.001) · `Ücretli` · **İ**

---

## 1.2 Motivasyon: Motorlar nereden arızalanır?

| Anket | Kapsam | Rulman | Stator | Rotor | Diğer |
|---|---|---|---|---|---|
| IEEE-IAS Motor Reliability Working Group (1985) | 1.141 motor, >200 hp | %44 | %26 | %8 | %22 |
| EPRI, Albrecht vd. (1986) | 6.312 motor, >100 hp, santraller | %41 | %36 | %9 | %14 |
| Thorsen & Dalva (1995) | ≥11 kW OG/YG kafesli motorlar; offshore ve petrokimya | %42 | %13 | %8 | %38 |
| Tavner & Hasson, MOD anketi (1999) | ≤750 kW AG motorlar | %95 | %2 | %1 | %2 |
| *Karşılaştırma:* araştırmaların ilgisi (26 yılda 80 IEEE/IEE dergi makalesi; Tavner 2008) | — | %21 | %35 | %44 | — |

**Kaynaklardaki farklılık.** IEEE 1985 anketinin yüzdeleri ikincil kaynaklarda iki farklı biçimde aktarılıyor: 44/26/8/22 ve 41/37/10/12.
Tezinizde birincil makaleyi ve gerçekten okuduğunuz ikincil kaynağı birlikte gösterin.

**Kaynaklar**
- IEEE Motor Reliability Working Group (1985). Report of large motor reliability survey of industrial and commercial installations, Part I. *IEEE Trans. Ind. Appl.* IA-21(4):853–864.
  - [doi:10.1109/TIA.1985.349532](https://doi.org/10.1109/TIA.1985.349532)
  - Part II: aynı sayı, s. 865–872, [doi:10.1109/TIA.1985.349533](https://doi.org/10.1109/TIA.1985.349533)
  - Part 3: IA-23(1):153–158, 1987, [doi:10.1109/TIA.1987.4504880](https://doi.org/10.1109/TIA.1987.4504880)
- Albrecht, P.F., Appiarius, J.C., McCoy, R.M., Owen, E.L., Sharma, D.K. (1986). Assessment of the reliability of motors in utility applications—Updated. *IEEE Trans. Energy Convers.* EC-1(1):39–46.
  - [doi:10.1109/TEC.1986.4765668](https://doi.org/10.1109/TEC.1986.4765668)
- Thorsen, O.V., Dalva, M. (1995). *IEEE Trans. Ind. Appl.* 31(5):1186–1196.
  - [doi:10.1109/28.464536](https://doi.org/10.1109/28.464536)
- Tavner, P.J. (2008). Review of condition monitoring of rotating electrical machines. *IET Electr. Power Appl.* 2(4):215–247.
  - [doi:10.1049/iet-epa:20070280](https://doi.org/10.1049/iet-epa:20070280) · `Ücretli`
  - Tavner'in tablosu ücretsiz olarak Jung vd. 2025'te de yer alıyor: *Data in Brief* 62:111954, [doi:10.1016/j.dib.2025.111954](https://doi.org/10.1016/j.dib.2025.111954), Tablo 1.
- Ücretsiz ikincil kaynak: McJunkin, Agarwal, Lybeck (2016). *Online Monitoring of Induction Motors*. INL/EXT-15-36681, ABD Enerji Bakanlığı / INL.
  - [PDF](https://inldigitallibrary.inl.gov/content/uploads/50/2026/04/6760053.pdf) (bkz. Tablo 1)
- Eleştirel okuma: H. Penrose, ["Large Electric Motor Reliability: What Did the Studies Really Say?"](https://www.reliabilityconnect.com/large-electric-motor-reliability-what-did-the-studies-really-say-2/) (2018, ücretsiz).

**Çıkarım**
- En sık arıza rulmanlardadır: büyük motorlarda %40–45, küçük AG motorlarda çok daha fazla.
- Stator sargıları ikinci sıradadır (%13–37). Rotor arızaları ise %8–10 düzeyindedir, ama araştırmaların en çok ilgilendiği arıza türüdür.
- MCSA'nın en güçlü olduğu alanlar **rotor kafesi arızaları** ve **eksantrikliktir**.
- Rulman arızasını akımdan tespit etmek daha zordur (Culbert & Letal 2015, §1.7).

---

## 1.3 Önerilen okuma sırası: klasik eğitici makaleler ve derlemeler

Aşağıdaki sırayla okuyun. İlk ikisi, konuya giriş için en iyi kaynaklardır.

1. **Thomson, W.T., Gilmore, R.J. (2003).** Motor current signature analysis to detect faults in induction motor drives – fundamentals, data interpretation, and industrial case histories. *Proc. 32nd Turbomachinery Symposium*, Texas A&M.
   - [OAKTrust (ücretsiz PDF)](https://hdl.handle.net/1969.1/163283) · `Açık` · **B**
   - **Başlamak için en iyi ücretsiz kaynak.** Kırık çubuk, eksantriklik, AG sargılarında kısa devre ve bazı mekanik arızaları temelden ve saha örnekleriyle anlatır.
   - Site bir tarayıcı doğrulaması yapar; bağlantıyı normal bir tarayıcıda açın.
2. **Thomson, W.T., Fenger, M. (2001).** Current signature analysis to detect induction motor faults. *IEEE Ind. Appl. Mag.* 7(4):26–34.
   - [doi:10.1109/2943.930988](https://doi.org/10.1109/2943.930988) · `Ücretli` · **B**
   - Endüstrideki standart giriş makalesi: spektrum nasıl okunur, gerçek motorlardan vaka örnekleri.
3. **Kliman, G.B., Stein, J. (1992).** Methods of motor current signature analysis. *Electric Machines & Power Systems* 20(5):463–474.
   - [doi:10.1080/07313569208909609](https://doi.org/10.1080/07313569208909609) · `Ücretli` · **B**
   - MCSA'nın tarihçesi ve birinci dereceden teorisi. Motoru bir ivmeölçer gibi bir "sensör" olarak ele alır.
4. **Benbouzid, M.E.H. (2000).** A review of induction motors signature analysis as a medium for faults detection. *IEEE TIE* 47(5):984–993.
   - [doi:10.1109/41.873206](https://doi.org/10.1109/41.873206) · `Ücretli` · **B/O**
   - MCSA merkezli klasik derleme.
   - Yanında okuyun: **Benbouzid & Kliman (2003).** What stator current processing-based technique to use for induction motor rotor faults diagnosis? *IEEE TEC* 18(2):238–244, [doi:10.1109/TEC.2003.811741](https://doi.org/10.1109/TEC.2003.811741). [HAL'da ücretsiz](https://hal.science/hal-01052444).
   - Kaynakça derlemesi: Benbouzid (1999). *IEEE TEC* 14(4):1065–1074, [doi:10.1109/60.815029](https://doi.org/10.1109/60.815029). [HAL'da ücretsiz](https://hal.science/hal-01052297).
5. **Nandi, S., Toliyat, H.A., Li, X. (2005).** Condition monitoring and fault diagnosis of electrical motors—a review. *IEEE TEC* 20(4):719–729.
   - [doi:10.1109/TEC.2005.847955](https://doi.org/10.1109/TEC.2005.847955) · `Ücretli` · **B/O**
   - Alanın en çok atıf alan derlemesi. Stator, rotor, eksantriklik ve rulman arızalarının akım, akı ve titreşim imzalarını kapsar.
6. **Bellini, A., Filippetti, F., Tassoni, C., Capolino, G.-A. (2008).** Advances in diagnostic techniques for induction machines. *IEEE TIE* 55(12):4109–4126.
   - [doi:10.1109/TIE.2008.2007527](https://doi.org/10.1109/TIE.2008.2007527) · `Ücretli` (kurum deposundaki kopya erişime kapalı) · **O**
   - Sinyal tabanlı, model tabanlı ve yapay zekâ tabanlı teşhisin geniş bir güncellemesi; sürücüyle beslenen makineleri de kapsar.
7. **Henao, H. vd. (2014).** Trends in fault diagnosis for electrical machines: a review of diagnostic techniques. *IEEE Ind. Electron. Mag.* 8(2):31–42.
   - [doi:10.1109/MIE.2013.2287651](https://doi.org/10.1109/MIE.2013.2287651) · [Ücretsiz kopya (RiuNet)](http://hdl.handle.net/10251/98423) · **O**
   - Alanın okunması kolay, dergi üslubunda bir haritası.
8. **Riera-Guasp, M., Antonino-Daviu, J.A., Capolino, G.-A. (2015).** Advances in electrical machine, power electronic, and drive condition monitoring and fault detection: state of the art. *IEEE TIE* 62(3):1746–1759.
   - [doi:10.1109/TIE.2014.2375853](https://doi.org/10.1109/TIE.2014.2375853) · [Ücretsiz kopya (RiuNet)](http://hdl.handle.net/10251/97806) · **O/İ**
   - Durağan olmayan (transient) analiz ve sürücü düzeyindeki bakış açısı.
9. **Jung, J.-H., Lee, J.-J., Kwon, B.-H. (2006).** Online diagnosis of induction motors using MCSA. *IEEE TIE* 53(6):1842–1852.
   - [doi:10.1109/TIE.2006.885131](https://doi.org/10.1109/TIE.2006.885131) · `Ücretli` · **O**
   - Donanımda doğrulanmış eksiksiz bir çevrimiçi MCSA işleme zinciri. **İleride MATLAB'da yeniden üretmek için iyi bir şablon.**
10. **Mehrjou, M.R., Mariun, N., Marhaban, M.H., Misron, N. (2011).** Rotor fault condition monitoring techniques for squirrel-cage induction machine—a review. *MSSP* 25(8):2827–2848.
    - [doi:10.1016/j.ymssp.2011.05.007](https://doi.org/10.1016/j.ymssp.2011.05.007) · `Ücretli` · **O**
    - Kırık çubuk ve uç halka arızaları için sinyaller ve işleme teknikleri.
11. **Gangsar, P., Tiwari, R. (2020).** Signal based condition monitoring techniques for fault detection and diagnosis of induction motors: a state-of-the-art review. *MSSP* 144:106908.
    - [doi:10.1016/j.ymssp.2020.106908](https://doi.org/10.1016/j.ymssp.2020.106908) · `Ücretli` · **O/İ**
    - Akım, titreşim ve diğer sinyaller ile makine öğrenmesi; elektriksel ve mekanik arızalar birlikte.
12. **Tavner, P.J. (2008).** Review of condition monitoring of rotating electrical machines. *IET EPA* 2(4):215–247 (bkz. §1.2). · `Ücretli` · **O**
13. **Zhang, P., Du, Y., Habetler, T.G., Lu, B. (2011).** A survey of condition monitoring and protection methods for medium-voltage induction motors. *IEEE TIA* 47(1):34–46.
    - [doi:10.1109/TIA.2010.2090839](https://doi.org/10.1109/TIA.2010.2090839) · `Ücretli` · **O**
    - Orta gerilim motorları açısından bakış.

---

## 1.4 Formüllerin kaynağı olan temel teknik makaleler

Arıza frekansı formüllerinin ilk türetildiği makaleler bunlardır. [Arıza imzaları dosyası](02-ariza-turleri-ve-imzalari.md) bu makaleleri ayrıntılı işler.

- **Kliman, Koegl, Stein, Endicott, Madden (1988).** *IEEE TEC* 3(4):873–879.
  - [doi:10.1109/60.9364](https://doi.org/10.1109/60.9364) · **O**
  - Çalışan motorda kırık çubuğun (1±2s)f yan bantları.
- **Schoen, Habetler, Kamran, Bartheld (1995).** *IEEE TIA* 31(6):1274–1279.
  - [doi:10.1109/28.475697](https://doi.org/10.1109/28.475697) · **O**
  - Rulman hasarı frekanslarının stator akımındaki izi.
- **Dorrell, Thomson, Roach (1997).** *IEEE TIA* 33(1):24–34.
  - [doi:10.1109/28.567073](https://doi.org/10.1109/28.567073) · **İ**
  - Statik, dinamik ve karma eksantrikliğin akı, akım ve titreşim imzaları.
- **Cardoso, Cruz, Fonseca (1999).** *IEEE TEC* 14(3):595–598.
  - [doi:10.1109/60.790920](https://doi.org/10.1109/60.790920) · **O**
  - Sarımlar arası kısa devre için Park vektörü yaklaşımı.
  - Devamı (EPVA): **Cruz & Cardoso (2001)**, *IEEE TIA* 37(5):1227–1233, [doi:10.1109/28.952496](https://doi.org/10.1109/28.952496).
- **Bellini, Filippetti, Franceschini, Tassoni, Kliman (2001).** *IEEE TIA* 37(5):1248–1255.
  - [doi:10.1109/28.952499](https://doi.org/10.1109/28.952499) · `Ücretli` · **O**
  - Yan bant genliği ile kırık çubuk sayısı arasındaki ilişki.
- **Blödt, Granjon, Raison, Rostaing (2008).** *IEEE TIE* 55(4):1813–1822.
  - [doi:10.1109/TIE.2008.917108](https://doi.org/10.1109/TIE.2008.917108) · [HAL'da ücretsiz](https://hal.science/hal-00270747/document) · **İ**
  - Rulman hasarı iki mekanizmayla etki eder: tork salınımı ve eksantriklik. Sonuçta akımda faz ve genlik modülasyonu oluşur.

---

## 1.5 Güncel derlemeler (2018–2026)

Açık erişimliler başta olmak üzere:

| # | Kaynak | Erişim | Seviye | Neden okumalı? |
|---|---|---|---|---|
| 1 | Halder, Bhat, Zychma, Sowa (2022). Broken rotor bar fault diagnosis techniques based on MCSA for induction motor—a review. *Energies* 15(22):8569. [doi:10.3390/en15228569](https://doi.org/10.3390/en15228569) | Açık | B/O | Doğrudan MCSA ve kırık çubuk odaklı derleme |
| 2 | Kumar, Andriollo, Cirrincione, Cirrincione, Tortella (2022). *Energies* 15(23):8938. [doi:10.3390/en15238938](https://doi.org/10.3390/en15238938) | Açık | O | Arıza istatistiklerinden başlar; klasik ve yapay zekâ yöntemlerini MCSA vurgusuyla anlatır |
| 3 | Garcia-Calva, Morinigo-Sotelo, Fernandez-Cavero, Romero-Troncoso (2022). Early detection of faults in induction motors—a review. *Energies* 15(21):7855. [doi:10.3390/en15217855](https://doi.org/10.3390/en15217855) | Açık | O | Başlangıç (erken) aşamadaki arızalar |
| 4 | Antonino-Daviu (2020). Electrical monitoring under transient conditions. *Appl. Sci.* 10(17):6137. [doi:10.3390/app10176137](https://doi.org/10.3390/app10176137) | Açık | O | Kalkış akımı ve geçici rejim analizi |
| 5 | Frosini (2020). Novel diagnostic techniques for rotating electrical machines—a review. *Energies* 13(19):5066. [doi:10.3390/en13195066](https://doi.org/10.3390/en13195066) | Açık | O | Bileşen bileşen saha uygulamaları ve yeni yöntemler |
| 6 | Kudelina, Asad, Vaimann, Rassõlkin, Kallaste, Van Khang (2021). *Energies* 14(22):7459. [doi:10.3390/en14227459](https://doi.org/10.3390/en14227459) | Açık | B | Kısa genel bakış |
| 7 | Khan, Asad, Kudelina, Vaimann, Kallaste (2023). Bearing faults detection methods for electrical machines—state of the art. *Energies* 16(1):296. [doi:10.3390/en16010296](https://doi.org/10.3390/en16010296) | Açık | O | En sık arıza sınıfı olan rulmanlar |
| 8 | Liu, Zhang, He, Huang (2021). Review of modeling and diagnostic techniques for eccentricity fault. *Energies* 14(14):4296. [doi:10.3390/en14144296](https://doi.org/10.3390/en14144296) | Açık | O/İ | Eksantrikliğin **modellenmesi**; Simulink aşamasında işe yarar |
| 9 | Gultekin, Bazzi (2023). Review of FDD techniques for AC motor drives. *Energies* 16(15):5602. [doi:10.3390/en16155602](https://doi.org/10.3390/en16155602) | Açık | O | Makine, güç elektroniği, DA bara ve sensör arızaları |
| 10 | Gonzalez-Jimenez, del-Olmo, Poza, Garramiola, Madina (2021). Data-driven fault diagnosis for electric drives. *Sensors* 21(12):4024. [doi:10.3390/s21124024](https://doi.org/10.3390/s21124024) | Açık | O | Uygulamaya dönük makine öğrenmesi iş akışı |
| 11 | Zhang, Zhang, Wang, Habetler (2020). Deep learning algorithms for bearing fault diagnostics. *IEEE Access* 8:29857–29881. [doi:10.1109/ACCESS.2020.2972859](https://doi.org/10.1109/ACCESS.2020.2972859) | Açık | O/İ | Rulman arızalarında derin öğrenme, akım tabanlı yaklaşımlar dahil |
| 12 | Orlowska-Kowalska vd. (2022). FD and FTC of PMSM drives. *IEEE Access* 10:59979–60024. [doi:10.1109/ACCESS.2022.3180153](https://doi.org/10.1109/ACCESS.2022.3180153) | Açık | İ | PMSM sürücülerinde arıza teşhisi ve arızaya dayanıklı kontrol |
| 13 | Chen, Liang, Li, Liang, Wang (2019). Faults and diagnosis methods of PMSM. *Appl. Sci.* 9(10):2116. [doi:10.3390/app9102116](https://doi.org/10.3390/app9102116) | Açık | O | PMSM arıza harmonikleri ve yöntemleri |
| 14 | Zachariades, Xavier (2025). AI techniques in fault diagnosis of electric machines. *Sensors* 25(16):5128. [doi:10.3390/s25165128](https://doi.org/10.3390/s25165128) | Açık | O | Güncel yapay zekâ manzarası |
| 15 | Gherghina, Bizon, Iana, Vasilică (2025). Synchronous motors fault detection review. *Machines* 13(9):815. [doi:10.3390/machines13090815](https://doi.org/10.3390/machines13090815) | Açık | O | 2021–2025 dönemini kapsayan sistematik (PRISMA) derleme |
| 16 | Zamudio-Ramírez vd. (2022). Magnetic flux analysis… *IEEE TII* 18(5):2895–2908. [doi:10.1109/TII.2021.3070581](https://doi.org/10.1109/TII.2021.3070581) | [Ücretsiz kopya](http://hdl.handle.net/10251/201880) | O | Akımı tamamlayan kaçak akı analizi |
| 17 | **Niu, Dong, Chen (2023). Motor fault diagnostics based on current signatures: a review.** *IEEE TIM* 72:1–19. [doi:10.1109/TIM.2023.3285999](https://doi.org/10.1109/TIM.2023.3285999) | Ücretli | O | **Konunuza en doğrudan uyan güncel derleme** (yalnızca akım imzaları) |
| 18 | Hassan, Amer, Abdelsalam, Williams (2018). BRB detection techniques based on fault signature analysis – a review. *IET EPA* 12:895–907. [doi:10.1049/iet-epa.2018.0054](https://doi.org/10.1049/iet-epa.2018.0054) | Ücretli | O | Kırık çubuk yöntemlerinin imzaya göre sınıflandırılması |
| 19 | **Bonet-Jara, Quijano-Lopez, Morinigo-Sotelo, Pons-Llinares (2021). Sensorless speed estimation for the diagnosis of induction motors via MCSA. Review and commercial devices analysis.** *Sensors* 21(15):5037. [doi:10.3390/s21155037](https://doi.org/10.3390/s21155037) | Açık | B–O | **Başlangıç için çok değerli:** arıza formülleri, dB kriterleri, kayma hatasının yol açtığı yanlış alarmlar, 79 endüstriyel motorda ticari cihaz analizi |

---

## 1.6 Kitaplar

- **Thomson, W.T., Culbert, I. (2017).** *Current Signature Analysis for Condition Monitoring of Cage Induction Motors: Industrial Application and Case Histories.* Wiley-IEEE Press.
  - [doi:10.1002/9781119175476](https://doi.org/10.1002/9781119175476) · **B→O**
  - **MCSA uygulamasının temel kitabı.** Özellikle Bölüm 1 (MCSA'ya giriş) ve Bölüm 4 (kafes sargısı arızaları) önemli.
- **Toliyat, H.A., Nandi, S., Choi, S., Meshgin-Kelk, H. (2012).** *Electric Machines: Modeling, Condition Monitoring, and Fault Diagnosis.* CRC Press.
  - [doi:10.1201/b13008](https://doi.org/10.1201/b13008) · **O/İ**
  - **Modelleme aşaması için en önemli kitap.** Sargı fonksiyonu (WFA), manyetik eşdeğer devre (MEC), sonlu elemanlar (FEM), MCSA ve DSP üzerinde MCSA uygulaması bölümlerini içerir.
- **Tavner, P., Crabtree, C., Kazemtabrizi, B., Ran, L. (2026).** *Condition Monitoring of Rotating Electrical Machines*, 4. baskı, IET.
  - [doi:10.1049/PBPO288E](https://doi.org/10.1049/PBPO288E) · **O**
  - Önceki baskılar: 3. baskı 2020, [doi:10.1049/PBPO145E](https://doi.org/10.1049/PBPO145E); 2. baskı 2008, [doi:10.1049/PBPO056E](https://doi.org/10.1049/PBPO056E).
  - Güvenilirlik, arıza modları ve tüm izleme tekniklerini kapsayan geniş bir başvuru kitabı.
- **Faiz, J., Ghorbanian, V., Joksimović, G. (2017).** *Fault Diagnosis of Induction Motors.* IET.
  - [doi:10.1049/PBPO108E](https://doi.org/10.1049/PBPO108E) · **İ**
  - Araştırma düzeyinde bir monografi; arızalı makine modellemeye başlayınca işe yarar.
- **Saad, N., Irfan, M., Ibrahim, R. (2018).** *Condition Monitoring and Faults Diagnosis of Induction Motors: Electrical Signature Analysis.* CRC Press.
  - [doi:10.1201/9781351172561](https://doi.org/10.1201/9781351172561) · **B/O**
- **Karmakar, S., Chattopadhyay, S., Mitra, M., Sengupta, S. (2016).** *Induction Motor Fault Diagnosis.* Springer.
  - [doi:10.1007/978-981-10-0624-1](https://doi.org/10.1007/978-981-10-0624-1) · **B/O**
- **Trigeassou, J.-C. (ed.) (2011).** *Electrical Machines Diagnosis.* ISTE/Wiley.
  - [doi:10.1002/9781118601662](https://doi.org/10.1002/9781118601662) · **İ**
  - Model tabanlı ve sinyal tabanlı teşhis.
- **Isermann, R. (2006).** *Fault-Diagnosis Systems.* Springer.
  - [doi:10.1007/3-540-30368-5](https://doi.org/10.1007/3-540-30368-5) · **O/İ**
  - Genel arıza teşhisi teorisi: gözlemciler, parite denklemleri, parametre kestirimi.
  - Tamamlayıcı cilt: *Fault-Diagnosis Applications* (2011), [doi:10.1007/978-3-642-12767-0](https://doi.org/10.1007/978-3-642-12767-0).

**Ücretsiz kitap bölümleri**
- Bonaldi, E.L. vd. (2012). Predictive maintenance by electrical signature analysis to induction motors. *Induction Motors – Modelling and Control* (InTech).
  - [doi:10.5772/48045](https://doi.org/10.5772/48045) · [Ücretsiz PDF](https://cdn.intechopen.com/pdfs/40906/InTech-Predictive_maintenance_by_electrical_signature_analysis_to_induction_motors.pdf) · **B**
  - 34 sayfalık iyi bir giriş.
- Blödt, M., Granjon, P., Raison, B., Regnier, J. (2010). Mechanical fault detection in induction motor drives through stator current monitoring – theory and application examples. *Fault Detection* (InTech).
  - [doi:10.5772/9072](https://doi.org/10.5772/9072) · [IntechOpen](https://www.intechopen.com/chapters/10363) · [HAL](https://hal.science/hal-00485734) · **O**
- Villalobos-Pina, F.J. vd. (2024). Electric fault diagnosis in induction machines using MCSA. *Time Series Analysis – Recent Advances…* (IntechOpen).
  - [doi:10.5772/intechopen.1004002](https://doi.org/10.5772/intechopen.1004002) · [IntechOpen](https://www.intechopen.com/chapters/1171032) · **B**

Türkçe kitaplar ve tezler için [05 numaralı dosyaya](05-veri-setleri-turkce-kaynaklar-egitimler.md) bakın.

---

## 1.7 Standartlar ve endüstriyel rehberler

**Standartlar**
- **ISO 20958:2013.** *Condition monitoring and diagnostics of machine systems — Electrical signature analysis of three-phase induction motors.*
  - [iso.org](https://www.iso.org/standard/39839.html) · `Ücretli` · [içindekiler dahil ücretsiz önizleme](https://cdn.standards.iteh.ai/samples/39839/45986d17766f42b09e8d24078c747a0b/ISO-20958-2013.pdf)
  - Sabit gerilim ve frekanslı şebekeden beslenen motorlar için stator akımı, gerilim ve güç analizini kapsar. Ek A'da Park vektörü yaklaşımı var.
- **IEEE Std 1415-2006.** *IEEE Guide for Induction Machinery Maintenance Testing and Failure Analysis.*
  - [IEEE SA](https://standards.ieee.org/standard/1415-2006.html) · `Ücretli`
  - 2021'den beri "Inactive-Reserved" durumunda; revizyon projesi (P1415) açık.
- Destekleyici standartlar (ikisi de ücretli):
  - [ISO 17359:2018](https://www.iso.org/standard/71194.html): durum izleme programının kurulması.
  - [ISO 13379-1:2012](https://www.iso.org/standard/39836.html): verilerin yorumlanması ve teşhis.

**Endüstriyel rehberler (ücretsiz)**
- **Culbert, I., Letal, J. (2015).** Signature analysis for on-line motor diagnostics. *IEEE PPIC 2015*.
  - [doi:10.1109/PPIC.2015.7165866](https://doi.org/10.1109/PPIC.2015.7165866) · [Ücretsiz PDF (Iris Power)](https://irispower.com/wp-content/uploads/2018/06/2015-PCIC-Signature-Analysis-For-On-Line-Motor-Diagnostics.pdf) · **O**
  - Pratik eşikler (PDF'ten doğrulandı):
    - (1−2s)f yan bandı temel bileşenin **45 dB ya da daha az** altındaysa kafes sargısı arızasından şüphelenilir. Fark küçüldükçe hasar büyür.
    - Eksantriklik için en yüksek rotor oluk harmoniği ile dönme hızı yan bantları arasındaki ortalama fark **15–25 dB** ise incelenmesi gereken bir sorun vardır.
  - Trend izlemek için ölçümler **aynı yük seviyesinde** alınmalıdır.
- **ABB Motion Services / Samotics.** *Electrical Signature Analysis Explained.*
  - [Ücretsiz PDF](https://search.abb.com/library/Download.aspx?DocumentID=4MWA000076&LanguageCode=en&DocumentPartId=&Action=Launch&DocumentRevisionId=D) · **B**
  - Veri toplama, FFT, model tabanlı ve veri tabanlı analiz, ESA ile MCA farkı. 20 sayfa.
- **PdMA.** *Advanced Spectral Analysis – Current Signature Analysis.*
  - [Ücretsiz PDF](https://pdma.com/wp-content/uploads/2021/01/Advanced_Spectral_Analysis.pdf) · **B/O**
- **SKF (2016).** *Predictive Motor Maintenance: a primer on static, dynamic, and online motor testing.*
  - [Ücretsiz PDF](https://cdn.skfmediahub.skf.com/api/public/0901d196805b2d0b/pdf_preview_medium/0901d196805b2d0b_pdf_preview_medium.pdf) · **B**

---

## 1.8 Literatürü takip etmek

**Anahtar araştırmacılar ve gruplar**

| Grup | Odak |
|---|---|
| W.T. Thomson; I. Culbert (Iris Power) | Endüstriyel MCSA uygulaması |
| G.B. Kliman (GE) | MCSA'nın kökeni |
| T.G. Habetler (Georgia Tech) | Rulmanlar, OG motorlar, derin öğrenme |
| M.E.H. Benbouzid (Brest) | Derlemeler, sinyal işleme |
| H.A. Toliyat, S. Nandi | Modelleme, derlemeler |
| Filippetti, Bellini, Tassoni, Franceschini (Bologna/Modena) | Elektriksel imza analizi, sürücüler |
| G.-A. Capolino, H. Henao (Amiens) | SDEMPED topluluğu |
| J.A. Antonino-Daviu, M. Riera-Guasp (UPV Valencia) | Geçici rejim analizi, akı, **hızlı arızalı motor modelleri** |
| R. Romero-Troncoso (UAQ); D. Morinigo-Sotelo (Valladolid) | Erken arıza, inverterle beslenen motorlar |
| A.J.M. Cardoso, S.M.A. Cruz (Coimbra) | Park vektörü yöntemleri |
| M. Blödt, P. Granjon | Akım üzerinden mekanik arızalar |
| P. Tavner (Durham) | Güvenilirlik, durum izleme |
| J. Faiz, G. Joksimović | Arıza modelleme |
| M. Arkan, T. Göktaş (İnönü); diğer Türk araştırmacılar | Bkz. [05 numaralı dosya](05-veri-setleri-turkce-kaynaklar-egitimler.md) |

**Dergiler**
- Temel dergiler: IEEE TIE, IEEE TIA, IEEE TEC, IEEE TII, IEEE TIM; *IEEE Industrial Electronics Magazine*, *IEEE Industry Applications Magazine*; IET Electric Power Applications; MSSP; *Measurement*; *Electric Power Components and Systems*.
- Açık erişim: IEEE Access; MDPI *Energies*, *Sensors*, *Machines*, *Applied Sciences*, *Electronics*; veri setleri için *Data in Brief*.

**Konferanslar**
- **IEEE SDEMPED:** alanın kendi sempozyumu, iki yılda bir düzenlenir.
- ICEM, IEEE IEMDC, IEEE ECCE, IEEE IAS Annual Meeting, IECON.
- Uygulayıcılara yönelik: IEEE PCIC, IEEE PPIC, Texas A&M Turbomachinery Symposium.

**Arama dizeleri**
- **IEEE Xplore (Command Search):**
  ```
  ("All Metadata":"motor current signature analysis" OR "All Metadata":MCSA OR "All Metadata":"current signature analysis" OR "All Metadata":"electrical signature analysis") AND ("All Metadata":"induction motor*" OR "All Metadata":"induction machine*") AND ("All Metadata":fault*)
  ```
  Yalnızca derlemeler için sonuna ekleyin: `AND ("Document Title":review OR "Document Title":survey OR "Document Title":"state of the art")`
- **Scopus:**
  ```
  TITLE-ABS-KEY(("motor current signature analysis" OR mcsa OR "current signature analysis" OR "electrical signature analysis" OR "stator current") AND ("induction motor*" OR "induction machine*" OR "electric* machine*" OR pmsm) AND (fault* OR diagnos* OR "condition monitoring")) AND PUBYEAR > 2017
  ```
- **Arıza türüne göre ek terimler:**
  - `"broken rotor bar*"`
  - `"inter-turn" OR "stator winding fault"`
  - `eccentricity`
  - `"bearing fault*"`
  - `"inverter-fed" OR VFD`
  - `"startup transient" OR wavelet`
  - `MSCSA OR "square current" OR "instantaneous power" OR "Park's vector"`
- **Atıf zinciri:** Thomson & Fenger 2001, Benbouzid 2000 ve Nandi 2005 için Google Scholar'daki "Cited by" listelerini tarayın.
