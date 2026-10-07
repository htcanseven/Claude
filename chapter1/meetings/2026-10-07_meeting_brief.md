# Book proposal: meeting brief, 7 October 2026

*High-Speed Electrical Machines and Drives* · Hüseyin Canseven, Ilya Petrov, Juha Pyrhönen

*Internal note for the three of us. It records contributors' answers, so it is not for circulation. Updated at mid-morning with the letters from Wróbel, Peltoniemi, Aarniovuori and Belahcen and the invitations sent to Sopanen and Hinkkanen. Anything else that has arrived by email is not in it, so correct the tables in the meeting.*

## Where we are

- **Chapter 1** is written and is now in the house style throughout: all nine figures are redrawn, and every table and caption uses one style. It is 24 pages. Five items remain to be folded in before the version that goes to Wiley.
- **The annotated table of contents** has 14 chapters and 454 pages: 414 of chapters plus 40 of front and back matter, against a target of 450 and a ceiling of 500. It cannot go to anyone new until Chapter 9 has an owner, because every copy still names Paavo Rasilo.
- **Contributors.**
  - In writing: Juha Saari (Chapter 2), Anouar Belahcen (Chapter 8, and Chapter 9 if his letter is the draft he was sent), Rafał Wróbel (Chapter 10), Pasi Peltoniemi (Chapter 11) and Lassi Aarniovuori (§11.2 and §13.4).
  - Paavo Rasilo declined Chapter 9 on 20 September.
  - Jussi Sopanen agreed in principle and was invited on 3 September; his letter has not come back.
  - Marko Hinkkanen was invited on 4 September, for the control side of the drive chapter, three days before it became Chapter 12. He has not replied.
  - Tiainen and Jaatinen-Värri, Pippuri-Mäkeläinen and Ikäheimo have been invited, with no answer recorded.
- **Letters of support:** five of ten are back: Saari, Aarniovuori, Wróbel, Peltoniemi and Belahcen. Wróbel's must be fixed before it goes to Wiley.
- **Not yet started for the package:** the partial Chapter 7, the biographies, the competing-titles analysis and Wiley's proposal form.
- **Wiley:** Juha's question of 15 September, whether he should send the first letter to Wiley, is still unanswered.

## Decisions needed today

1. **Who owns Chapter 9.** Paavo Rasilo declined on 20 September and suggested Anouar Belahcen and Floran Martin. Anouar was offered "one or two chapters" on the losses. The draft letter he was sent says he will contribute "the loss chapters of the book, on AC winding losses and conductor design and on the core, rotor and aerodynamic losses", and he has now signed it. If he signed it unchanged, Chapter 9 is already his in writing, and the decision is only to confirm it, with Floran as his co-author if he wants one. Check the signed copy's wording first. The table of contents must then name him for Chapter 9 before his letter and the table of contents go to Wiley together. Until then, no table of contents goes out.
2. **Authored book or edited volume.** Juha's revision of the table of contents reads "Editors", and Juha has described the book that way to contributors since 9 September. Everything else still says "authors": the byline, the confidentiality notice and its copyright line, the invitations and the letters. Contributors own 11 of the 14 chapters, so "edited" is the honest description. It does change the Wiley contract, the contributor agreements and royalties, and how reviewers read the book. Decide, then change every document at once.
3. **Wiley: who writes, and what we ask.** First, answer Juha's question; recommended: Juha writes, given his history with Wiley. The questions to put to them:
   - Does the book print in colour or greyscale?
   - Do they accept AI-generated images? The house style assumes not.
   - What is the trim size? Every figure's width can be changed in one place.
   - What is the page ceiling? The plan stands at 454 of 500.
   - Is there a companion site for the Python notebooks?
   - Do they prefer an authored or an edited volume?
4. **Submission date.** Fix the month. It sets the reply-by dates in every pending email, and fills the "[month]" left in the timeline we gave Juha Saari.
5. **The rest of the package, and who prepares it.** Section 7 of the table of contents promises three pieces that do not exist yet:
   - a partial Chapter 7, showing the inverted sizing procedure on one running machine;
   - the biographies;
   - a competing-titles analysis.

   Wiley's proposal form is needed too, and it normally asks for suggested reviewers. Assign each piece, or drop the Chapter 7 promise.
6. **Running-machine data.**
   - **Industrial:** the 2 MW solid-rotor machine of Chong Di's dissertation was built and tested, but the results are unpublished. Decide what may appear, and whether anyone outside LUT must agree.
   - **Mobile:** nine chapters rest on Voltcar, and the consortium's permission to publish has not yet been obtained. Jenni's draft letter says she will obtain it. A late refusal would cost the mobile half of the book, so this should be settled before submission.

## Chapter 1 and the figures

- **To look at together:** the new Figure 1.2 and Figure 1.4.
  - Figure 1.2(b) is now drawn the same way as (a). It shows the motor's upper half cut open, the radial and axial AMBs, the impeller on the motor shaft, and an empty floor where the oil system was.
  - Figure 1.4 draws the rotor to scale above the four mode shapes.
  - Juha's points of 15 September: the oil cooler he found missing is now drawn. He also asked for a photorealistic AI picture of the geared drive, which the house style excludes because the copyright in AI images is unsettled.
- **Figure 1.4 needs its data.** The curves were traced from the old picture. Who holds the MATLAB model? Export the four mode shapes, and confirm the labels: three "radial AMB" and "active part". The rotor's proportions resemble the 2 MW machine's; if it is that rotor, the caption could say so.
- **Still to fold in, as one revision before submission:**
  - §1.1.2 on specific speed, from Ahti's draft 2 of 6 October. Two things are open:
    - our corrections: the Table 1 densities were taken at 0 °C against 15 °C, and equations (1) and (3) need fixing;
    - his answer on the turbine convention for the volume flow.

    This is Juha's thread with Ahti: where does it stand?
  - The missing §1.2 heading: the chapter runs from §1.1.2 straight into §1.2.1.
  - "mechanical rpm value" in §1.1, to read r/min.
  - The pulse-ratio wording, against Juha's "nine or eleven".
  - Figure 1.5: do the illustrative loss values stay? The caption says they are illustrative.
- **Copies already out.** Wrobel, Saari, Ahti and Jonna hold the earlier Chapter 1, whose Figure 1.5 was AI-generated. Resend once with the corrected table of contents, or leave it until submission?
- **House style for the whole book.** Approve House_Style.docx. Its MATLAB version has not been tested: can someone in the group try it on one figure?

## The table of contents

- **Merge Juha's revision** with the changes made since. His revision rewrites the register of every abstract, makes the text 26 % longer, and uses "Editors". The later changes:
  - Chapter 1 at 28 pages with §1.1.2;
  - §2.2 retitled;
  - Chapter 13 with Ahti as point of contact;
  - totals of 414 and 454 pages.
- **Then four fixes:**
  - Chapter 9's owner, in three places;
  - "Upheat Solutions" for Juha Saari;
  - Chapter 14's title, which says "traction" although the chapter also has aerospace and e-turbocharger sections;
  - no Status column in the contributors' copy.

## What the returned letters change

- **Wróbel** takes Chapter 10 entire, but his letter cannot go to Wiley as it stands. Its letterhead still reads "Email: [insert preferred professional email]", and it is not signed. He also now writes as an independent researcher and engineering consultant, not as Newcastle University. Ask how he wants to be listed, including whether with diacritics, Rafał Wróbel.
- **Peltoniemi** describes his chapter as "power-electronic constraints and converter–machine interaction in high-speed electrical drives". He treats insulation, bearing currents and EMC through the converter-generated stresses, not their full physics. The Chapter 11 abstract should say the same, because Wiley's reviewers read the letters beside the table of contents.
- **Aarniovuori** takes §11.2 and §13.4, as offered, and adds service on IEC and CENELEC standardisation committees. That makes him a candidate for §13.5, qualification against the standards, too.
- **Most letters name neither the book nor us** (Saari, Aarniovuori, Peltoniemi), and three are undated. Rather than send them back, bundle the letters behind a cover sheet that gives the title and the editors and lists them.

## Status by chapter

| Ch. | Subject | Owner | Status | Support letter |
|---|---|---|---|---|
| 1 | Introduction | editors; §1.1.2 A. Jaatinen-Värri | written; house style done; five items to fold in | — |
| 2 | Applications | J. Saari, Upheat Solutions | accepted; waiting for the detailed section structure | received 21 Sep |
| 3 | Topologies | editors; J. Ikäheimo for §3.2–3.3 | Ikäheimo agreed through Juha; ABB clearance for photographs still to ask | drafted |
| 4–6 | Rotor mechanics, rotordynamics, bearings | J. Sopanen | agreed in principle; invited 3 Sep; he names the bearing specialist | awaited |
| 7 | Sizing | editors | partial chapter promised in the package | — |
| 8 | Winding losses | A. Belahcen | in writing | signed; covers Chapters 8 and 9 if unchanged |
| 9 | Core, rotor and aerodynamic losses | Belahcen, to confirm | Rasilo declined 20 Sep | see Chapter 8 |
| 10 | Thermal | R. Wróbel, independent consultant | accepted | received 21 Sep; unsigned, email line unfilled |
| 11 | Converter | P. Peltoniemi | accepted; Aarniovuori on §11.2 | received 22 Sep; Aarniovuori's scanned 7 Sep |
| 12 | Control | M. Hinkkanen | invited 4 Sep, for the control side of the drive chapter; no reply | after he says yes; draft needs fixing |
| 13 | Industrial case studies | J. Tiainen and A. Jaatinen-Värri | invited with Chapter 1 and the table of contents; no answer recorded | drafted (Ahti) |
| 14 | Mobile case studies | J. Pippuri-Mäkeläinen, VTT | invited; no answer recorded; Voltcar permission pending | drafted |

## Letters of support

- **Back, five:**
  - Saari, 21 Sep;
  - Aarniovuori, scanned 7 Sep;
  - Wróbel, 21 Sep;
  - Peltoniemi, 22 Sep;
  - Belahcen, by 7 Oct, not yet filed.

  The register is in `letters/received/README.md`.
- **Must be fixed:** Wróbel's, which needs a signature and the email line in its letterhead.
- **Awaited:**
  - Sopanen, who had the draft with his invitation on 3 Sep;
  - Ikäheimo;
  - Jaatinen-Värri, and a second letter from Tiainen if she will write one;
  - Pippuri-Mäkeläinen.
- **Not yet asked:** Hinkkanen, whose letter is the second step. His draft still offers "the control sections of the chapter on the drive" and needs the Chapter 12 offer and the pulse-ratio wording.
- **Chasing:** once the submission month is fixed, give everyone a reply-by date.

## Actions

| Action | Who | By |
|---|---|---|
| Answer Juha's question; write to Wiley | | |
| Offer Chapter 9 | | |
| Merge and correct the table of contents | | |
| Ask Rafał to sign, fill the email line, and say how to list him | | |
| File Anouar's signed letter; check its chapter paragraph | | |
| Follow up Marko Hinkkanen with the Chapter 12 offer | | |
| Chase Jussi Sopanen's letter and his co-authors | | |
| Export the Figure 1.4 mode shapes | | |
| Partial Chapter 7, or drop it | | |
| Biographies, competing titles, Wiley's form | | |
| Voltcar permission, with Jenni | | |
| What may be published of the 2 MW machine | | |
| Close §1.1.2 with Ahti | | |
