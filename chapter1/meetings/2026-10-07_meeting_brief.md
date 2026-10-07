# Book proposal: meeting brief, 7 October 2026

*High-Speed Electrical Machines and Drives* · Hüseyin Canseven, Ilya Petrov, Juha Pyrhönen

*Internal note for the three of us. It records contributors' answers, so it is not for circulation. It reflects what is filed in the project as of this morning; anything that has arrived by email since then is not in it, so correct the tables in the meeting.*

## Where we are

- **Chapter 1** is written and is now in the house style throughout: all nine figures are redrawn, and every table and caption uses one style. It is 24 pages. Five items remain to be folded in before the version that goes to Wiley.
- **The annotated table of contents** has 14 chapters and 454 pages: 414 of chapters plus 40 of front and back matter, against a target of 450 and a ceiling of 500. It cannot go to anyone new until Chapter 9 has an owner, because every copy still names Paavo Rasilo.
- **Contributors.**
  - Juha Saari has accepted Chapter 2.
  - Paavo Rasilo declined Chapter 9 on 20 September.
  - Jussi Sopanen and Pasi Peltoniemi agreed in principle.
  - Rafal Wrobel is interested and has the whole of Chapter 10 on offer.
  - Belahcen, Tiainen and Jaatinen-Värri, and Pippuri-Mäkeläinen have been invited, with no answer recorded yet.
  - Hinkkanen's invitation is not recorded as sent, and Aarniovuori has not been approached.
- **Letters of support:** one of ten is back (Juha Saari's).
- **Not yet started for the package:** the partial Chapter 7, the biographies, the competing-titles analysis and Wiley's proposal form.
- **Wiley:** Juha's question of 15 September, whether he should send the first letter to Wiley, is still unanswered.

## Decisions needed today

1. **Who owns Chapter 9.** Paavo Rasilo declined on 20 September and suggested Anouar Belahcen and Floran Martin. Recommended: offer Chapter 9 to Anouar alongside Chapter 8, with Floran as his co-author. Anouar's draft letter already argues Chapter 9's case: loss models fitted at mains frequency do not extrapolate, and the damage from cutting and stacking depends on frequency. So the letter becomes correct as written. The alternative is Floran as owner, introduced with Paavo's name; we asked Paavo whether we may use it. Until this is settled, no table of contents goes out.
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

## Status by chapter

| Ch. | Subject | Owner | Status | Support letter |
|---|---|---|---|---|
| 1 | Introduction | editors; §1.1.2 A. Jaatinen-Värri | written; house style done; five items to fold in | — |
| 2 | Applications | J. Saari, Upheat Solutions | accepted; waiting for the detailed section structure | received 21 Sep |
| 3 | Topologies | editors; J. Ikäheimo for §3.2–3.3 | Ikäheimo agreed through Juha; ABB clearance for photographs still to ask | drafted |
| 4–6 | Rotor mechanics, rotordynamics, bearings | J. Sopanen | agreed in principle; he names the bearing specialist | drafted |
| 7 | Sizing | editors | partial chapter promised in the package | — |
| 8 | Winding losses | A. Belahcen | invited; no answer recorded | drafted; it argues Chapter 9's case |
| 9 | Core, rotor and aerodynamic losses | open | Rasilo declined 20 Sep | — |
| 10 | Thermal | R. Wrobel, Newcastle | interested; whole chapter offered; answer pending | drafted |
| 11 | Converter | P. Peltoniemi | agreed in principle; Aarniovuori (§11.2) not yet approached | drafted |
| 12 | Control | M. Hinkkanen | invitation not recorded as sent; an introduction from Juha or Anouar would help | drafted; needs fixing |
| 13 | Industrial case studies | J. Tiainen and A. Jaatinen-Värri | invited with Chapter 1 and the table of contents; no answer recorded | drafted (Ahti) |
| 14 | Mobile case studies | J. Pippuri-Mäkeläinen, VTT | invited; no answer recorded; Voltcar permission pending | drafted |

## Letters of support

- **Back:** Juha Saari's, signed. It still needs a date, and the book's title or our names, because Wiley's reviewers receive the letters as a bundle. We asked him for both.
- **To fix before they go out:**
  - Hinkkanen's still offers "the control sections of the chapter on the drive", where he would now own Chapter 12, and needs the pulse-ratio wording.
  - Belahcen's depends on decision 1.
- **Chasing:** once the submission month is fixed, give everyone a reply-by date.

## Actions

| Action | Who | By |
|---|---|---|
| Answer Juha's question; write to Wiley | | |
| Offer Chapter 9 | | |
| Merge and correct the table of contents | | |
| Talk to Lassi Aarniovuori | | |
| Introduce and invite Marko Hinkkanen | | |
| Export the Figure 1.4 mode shapes | | |
| Partial Chapter 7, or drop it | | |
| Biographies, competing titles, Wiley's form | | |
| Voltcar permission, with Jenni | | |
| What may be published of the 2 MW machine | | |
| Close §1.1.2 with Ahti | | |
