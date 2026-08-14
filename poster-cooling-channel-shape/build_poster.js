// A0 portrait research poster — LUT template look (black band + logo, orange FF6600, Arial)
// Content: ICEM 2026 + ECCE 2026 papers on cooling channel shape in hollow hairpin windings
const pptxgen = require("pptxgenjs");

const pres = new pptxgen();
pres.defineLayout({ name: "A0P", width: 33.11, height: 46.81 });
pres.layout = "A0P";

// ---------- constants ----------
const ORANGE = "FF6600";      // LUT brand orange (template accent1)
const ORANGE_DEEP = "E85D00"; // deepened orange for stat numbers / chart series
const INK = "1A1A1A";
const GRAY = "595959";
const TINT = "FFF1E8";        // light orange tint for tiles
const FONT = "Arial";

const W = 33.11, H = 46.81;
const ML = 2.23;                       // left/right margin
const CW = W - 2 * ML;                 // 28.65 content width
const COLW = 8.75, GAP = 1.2;
const COLX = [ML, ML + COLW + GAP, ML + 2 * (COLW + GAP)]; // 2.23, 12.18, 22.13
const TOP = 10.55;                     // content top
const RULE_Y = 42.44;                  // footer rule
const BOTTOM = 42.05;                  // content must end above this

const FIGDIR = __dirname + "/figs/";
const ASPECT = { // width/height of extracted figures
  icem_fig1_topologies: 2141 / 979,
  icem_fig3_currentdensity: 2036 / 1168,
  icem_fig5_tempmaps: 4321 / 1154,
  ecce_fig1_machine: 2072 / 920,
  ecce_fig2_shapes: 2137 / 367,
  ecce_fig8_pareto: 2113 / 1155,
  ecce_fig9_tempmaps: 4321 / 1093,
};

const slide = pres.addSlide();
slide.background = { color: "FFFFFF" };

// ---------- header ----------
slide.addShape(pres.ShapeType.rect, { x: 0, y: 0, w: W, h: 3.6, fill: { color: "000000" }, line: { type: "none" } });
slide.addImage({ path: FIGDIR + "lut_logo_white.png", x: ML, y: 1.02, h: 1.56, w: 1.56 * (1301 / 452) });

slide.addText("IMPACT OF COOLING CHANNEL SHAPE ON THE PERFORMANCE OF HOLLOW HAIRPIN WINDINGS", {
  x: ML, y: 3.98, w: CW, h: 2.45, margin: 0, fontFace: FONT, fontSize: 78, bold: true,
  color: ORANGE, align: "left", valign: "top", lineSpacingMultiple: 1.03,
});
slide.addText("Electromagnetic–thermal analysis and multi-objective shape optimization of direct oil-cooled hairpin windings for traction motors", {
  x: ML, y: 6.55, w: CW, h: 1.32, margin: 0, fontFace: FONT, fontSize: 40, bold: true,
  color: "111111", align: "left", valign: "top", lineSpacingMultiple: 1.08,
});

slide.addText("RESEARCH TEAM", {
  x: ML, y: 8.14, w: 12, h: 0.45, margin: 0, fontFace: FONT, fontSize: 24, bold: true, color: ORANGE, charSpacing: 2,
});
slide.addText([
  { text: "Hüseyin Tayyer Canseven¹ · Pratik Bisale¹ · Ilya Petrov¹ · Lassi Aarniovuori¹ · Juho Montonen² · Juha Pyrhönen¹", options: { fontSize: 26, color: INK, breakLine: true, paraSpaceAfter: 6 } },
  { text: "¹ Department of Electrical Engineering, LUT University, Finland      ² Danfoss Editron, Lappeenranta, Finland", options: { fontSize: 22, color: GRAY } },
], { x: ML, y: 8.66, w: CW - 8.9, h: 1.25, margin: 0, fontFace: FONT, valign: "top" });
slide.addText("Based on the authors' ICEM 2026\nand ECCE 2026 conference papers", {
  x: W - ML - 8.6, y: 8.14, w: 8.6, h: 1.1, margin: 0, fontFace: FONT, fontSize: 21, italic: true,
  color: GRAY, align: "right", valign: "top", lineSpacingMultiple: 1.12,
});

// ---------- flow helpers ----------
function makeCol(i) { return { x: COLX[i], y: TOP, name: "col" + (i + 1) }; }

function head(col, txt, opts = {}) {
  if (col.y > TOP) col.y += opts.before ?? 0.45;
  const cpl = Math.floor(COLW / (0.60 * 33 / 72)); // bold caps-ish estimate ≈ 32
  const lines = Math.ceil(txt.length / cpl);
  const h = lines * 0.52 + 0.12;
  slide.addText(txt, {
    x: col.x, y: col.y, w: COLW, h, margin: 0, fontFace: FONT,
    fontSize: 33, bold: true, color: "000000", valign: "top", lineSpacingMultiple: 1.05,
  });
  col.y += h + 0.2;
}

const CHARS_PER_IN = (pt) => 1 / (0.52 * pt / 72); // rough Arial estimate
function bullets(col, items, opts = {}) {
  const size = opts.size ?? 25;
  const runs = items.map((t, i) => ({
    text: t,
    options: {
      bullet: { code: "2022", indent: 18 }, breakLine: true,
      paraSpaceAfter: i === items.length - 1 ? 0 : 10,
    },
  }));
  const cpl = Math.floor((COLW - 0.35) * CHARS_PER_IN(size));
  let lines = 0;
  items.forEach((t) => (lines += Math.ceil(t.length / cpl)));
  const h = lines * (size / 72) * 1.14 + items.length * (10 / 72) + 0.08;
  slide.addText(runs, {
    x: col.x, y: col.y, w: COLW, h, margin: 0, fontFace: FONT, fontSize: size,
    color: INK, valign: "top", lineSpacingMultiple: 1.12,
  });
  col.y += h;
}

function fig(col, key, caption, opts = {}) {
  col.y += opts.before ?? 0.38;
  const w = COLW * (opts.wFrac ?? 1);
  const h = w / ASPECT[key];
  slide.addImage({ path: FIGDIR + key + ".png", x: col.x + (COLW - w) / 2, y: col.y, w, h });
  col.y += h + 0.12;
  if (caption) {
    const cpl = Math.floor(COLW * CHARS_PER_IN(19.5));
    const cl = Math.ceil(caption.length / cpl);
    const ch = cl * (19.5 / 72) * 1.15 + 0.06;
    slide.addText(caption, {
      x: col.x, y: col.y, w: COLW, h: ch, margin: 0, fontFace: FONT, fontSize: 19.5,
      italic: true, color: GRAY, valign: "top", lineSpacingMultiple: 1.1,
    });
    col.y += ch;
  }
}

function statTile(col, big, label, opts = {}) {
  col.y += opts.before ?? 0.42;
  const h = opts.h ?? 1.8;
  slide.addShape(pres.ShapeType.roundRect, {
    x: col.x, y: col.y, w: COLW, h, rectRadius: 0.09, fill: { color: TINT }, line: { type: "none" },
  });
  slide.addText(big, {
    x: col.x + 0.35, y: col.y, w: opts.bigW ?? 3.1, h, margin: 0, fontFace: FONT,
    fontSize: opts.bigSize ?? 56, bold: true, color: ORANGE_DEEP, align: "left", valign: "middle",
  });
  slide.addText(label, {
    x: col.x + (opts.bigW ?? 3.1) + 0.45, y: col.y + 0.14, w: COLW - (opts.bigW ?? 3.1) - 0.9, h: h - 0.28,
    margin: 0, fontFace: FONT, fontSize: 20, color: "3B3B3B", valign: "middle", lineSpacingMultiple: 1.08,
  });
  col.y += h;
}

function noteTile(col, txt, opts = {}) {
  col.y += opts.before ?? 0.4;
  const h = opts.h ?? 1.6;
  slide.addShape(pres.ShapeType.roundRect, {
    x: col.x, y: col.y, w: COLW, h, rectRadius: 0.09, fill: { color: TINT }, line: { type: "none" },
  });
  slide.addText(txt, {
    x: col.x + 0.4, y: col.y + 0.12, w: COLW - 0.8, h: h - 0.24, margin: 0, fontFace: FONT,
    fontSize: 25.5, bold: true, italic: true, color: "2B2B2B", valign: "middle", lineSpacingMultiple: 1.1,
  });
  col.y += h;
}

const noB = { type: "none" };
function tbl(col, rows, colW, opts = {}) {
  col.y += opts.before ?? 0.32;
  const rowH = opts.rowH ?? 0.56;
  slide.addTable(rows, {
    x: col.x, y: col.y, w: COLW, colW, rowH,
    fontFace: FONT, fontSize: opts.size ?? 21.5, color: INK, valign: "middle",
    border: [noB, noB, { pt: 0.75, color: "CCCCCC" }, noB],
    margin: [0.04, 0.08, 0.04, 0.08],
  });
  col.y += rows.length * rowH + 0.15;
}

// ================= COLUMN 1 =================
const c1 = makeCol(0);

head(c1, "Motivation", { before: 0 });
bullets(c1, [
  "Electrified traction pushes motors to higher speeds and frequencies — hairpin windings are the standard thanks to high slot fill and automated manufacturing.",
  "Skin and proximity effects concentrate AC losses in the conductors nearest the slot opening: severe local hot spots limit the continuous power rating.",
  "Water jackets remove heat only after it has crossed slot insulation and stator core — a long, high-resistance thermal path.",
]);

head(c1, "Direct oil cooling through hollow conductors");
bullets(c1, [
  "Dielectric oil flows through a channel inside each hairpin conductor: heat is extracted directly at the source, hot spots are suppressed and the critical end-winding region is cooled too.",
  "Direct liquid cooling can sustain up to 277 % higher continuous current than a water jacket at the same winding temperature limit.",
]);
fig(c1, "ecce_fig1_machine", "Reference machine: 300 kW hairpin-winding PMSM, modeled as a 1/6 periodic sector. Every conductor carries an internal cooling channel.", { wFrac: 0.94 });

head(c1, "Reference machine & fair comparison");
tbl(c1, [
  [{ text: "Rated power / speed", options: { bold: true } }, { text: "300 kW / 2000 rpm" }],
  [{ text: "Stator slots × layers", options: { bold: true } }, { text: "48 × 4 hollow conductors" }],
  [{ text: "Conductor cross-section", options: { bold: true } }, { text: "6 mm × 4 mm" }],
  [{ text: "Rated current / frequency", options: { bold: true } }, { text: "350 A rms / 266.7 Hz" }],
  [{ text: "Coolant (dielectric oil)", options: { bold: true } }, { text: "65 °C inlet, 10 L/min total" }],
  [{ text: "Flow regime", options: { bold: true } }, { text: "Laminar (Re ≤ 113)" }],
], [4.5, 4.25]);
bullets(c1, [
  "Fair-comparison rule: every channel keeps the same flow area (2 mm²) → same mean oil velocity and same copper removed — the pure shape effect is isolated.",
]);
fig(c1, "icem_fig1_topologies", "Compared slot topologies: solid baseline, round channel Ø 1.6 mm, and rectangular channel 1 mm × 2 mm.", { wFrac: 0.95 });

noteTile(c1, "Can the internal channel be shaped freely for cooling — without an electromagnetic penalty?", { h: 1.65 });

console.log("col1 end:", c1.y.toFixed(2), "target <", BOTTOM);

// ================= COLUMN 2 =================
const c2 = makeCol(1);

head(c2, "Electromagnetic analysis", { before: 0 });
bullets(c2, [
  "2D FEA of all three topologies at the rated worst case: 350 A rms, 266.7 Hz.",
  "High-frequency current crowds at the conductor periphery — the centre acts as a low-current “dead zone”, exactly where the cooling channel sits.",
]);
fig(c2, "icem_fig3_currentdensity", "Current density at rated frequency: solid, round and rectangular conductors (left → right). The channel region carries almost no current.", { wFrac: 0.78 });

c2.y += 0.45;
slide.addText("High-frequency AC losses per layer (W)", {
  x: c2.x, y: c2.y, w: COLW, h: 0.42, margin: 0, fontFace: FONT, fontSize: 23, bold: true, color: INK,
});
c2.y += 0.48;
slide.addChart(pres.ChartType.bar, [
  { name: "Solid", labels: ["Layer 1", "Layer 2", "Layer 3", "Layer 4"], values: [2002.0, 800.2, 273.5, 32.5] },
  { name: "Round channel", labels: ["Layer 1", "Layer 2", "Layer 3", "Layer 4"], values: [1988.3, 794.1, 271.7, 32.8] },
  { name: "Rectangular channel", labels: ["Layer 1", "Layer 2", "Layer 3", "Layer 4"], values: [1992.7, 796.7, 272.3, 32.4] },
], {
  x: c2.x, y: c2.y, w: COLW, h: 3.85,
  barDir: "col", barGrouping: "clustered", barGapWidthPct: 70, barOverlapPct: -6,
  chartColors: ["2A78D6", "199E70", "E85D00"],
  showLegend: true, legendPos: "t", legendFontSize: 18, legendColor: "333333", legendFontFace: FONT,
  catAxisLabelColor: "333333", catAxisLabelFontSize: 18, catAxisLabelFontFace: FONT,
  valAxisLabelColor: "333333", valAxisLabelFontSize: 16, valAxisLabelFontFace: FONT,
  valAxisMinVal: 0, valAxisMaxVal: 2500, valAxisMajorUnit: 500, valAxisLabelFormatCode: "#,##0",
  valGridLine: { color: "E3E3E3", size: 0.75 }, catGridLine: { style: "none" },
  catAxisLineColor: "BFBFBF", valAxisLineColor: "BFBFBF",
  showTitle: false, showValue: false,
});
c2.y += 3.85 + 0.1;
slide.addText("Layer 1 lies next to the airgap and dominates the loss — yet its AC losses are shape-independent.", {
  x: c2.x, y: c2.y, w: COLW, h: 0.64, margin: 0, fontFace: FONT, fontSize: 19.5, italic: true, color: GRAY, lineSpacingMultiple: 1.1,
});
c2.y += 0.64;

statTile(c2, "< 0.25 %", "AC-loss difference between round and rectangular channels in the critical airgap-side layer — and only +2.4 % total loss for hollow vs solid conductors.", { bigW: 3.3 });

head(c2, "Thermal & hydraulic modelling");
bullets(c2, [
  "Equal area ⇒ equal mean velocity: the shapes differ only in wetted perimeter P and hydraulic diameter Dₕ = 4A/P.",
  "Laminar flow ⇒ h = Nu·k / Dₕ — a larger wetted perimeter directly buys heat-transfer surface.",
]);
tbl(c2, [
  [{ text: "", options: { bold: true } }, { text: "Round", options: { bold: true, align: "center" } }, { text: "Rectangular", options: { bold: true, align: "center", color: ORANGE_DEEP } }],
  [{ text: "Wetted perimeter", options: { bold: true } }, { text: "5 mm", options: { align: "center" } }, { text: "6 mm  (+20 %)", options: { align: "center", bold: true, color: ORANGE_DEEP } }],
  [{ text: "Hydraulic diameter Dₕ", options: { bold: true } }, { text: "1.60 mm", options: { align: "center" } }, { text: "1.33 mm", options: { align: "center" } }],
  [{ text: "Nusselt number Nu", options: { bold: true } }, { text: "4.36", options: { align: "center" } }, { text: "4.12", options: { align: "center" } }],
  [{ text: "Heat-transfer coeff. h", options: { bold: true } }, { text: "≈ 350 W/(m²K)", options: { align: "center" } }, { text: "≈ 400 W/(m²K)", options: { align: "center", bold: true, color: ORANGE_DEEP } }],
], [3.65, 2.35, 2.75]);

head(c2, "Steady-state thermal FEA");
fig(c2, "icem_fig5_tempmaps", "Temperature field at rated load — (a) round vs (b) rectangular channels. 2D FE slot model with layer-resolved losses and convection boundaries; the hot spot sits in Layer 1 next to the airgap.", { before: 0.05 });
statTile(c2, "−10 °C", "peak winding temperature: 172 °C (round) → 162 °C (rectangular) at the same 10 L/min oil flow — from the channel shape alone.", { bigW: 3.3 });

console.log("col2 end:", c2.y.toFixed(2), "target <", BOTTOM);

// ================= COLUMN 3 =================
const c3 = makeCol(2);

head(c3, "Channel-shape optimization", { before: 0 });
bullets(c3, [
  "Enlarging the channel adds wetted surface but removes copper (higher DC loss); shrinking it raises the pressure drop steeply — peak temperature and pumping power genuinely compete.",
  "Surrogate-based optimization: 128 thermal-FE samples per shape → surrogate model → multi-objective GA → Pareto front, with pumping power in closed form.",
  "Manufacturability constraints: wall thickness ≥ 0.75 mm, channel opening ≥ 0.75 mm.",
]);
fig(c3, "ecce_fig2_shapes", "Candidate shapes within the same conductor: circular, rectangular, elliptical.");
fig(c3, "ecce_fig8_pareto", "Pareto fronts (log pumping-power scale); stars mark minimum-temperature designs. The rectangular channel dominates the entire trade-off range.", { wFrac: 0.92 });

tbl(c3, [
  [{ text: "Shape", options: { bold: true } }, { text: "Optimal channel", options: { bold: true, align: "center" } }, { text: "Peak T", options: { bold: true, align: "center" } }, { text: "Pump power", options: { bold: true, align: "center" } }],
  [{ text: "Circular" }, { text: "Ø 0.75 mm", options: { align: "center" } }, { text: "127.4 °C", options: { align: "center" } }, { text: "34.8 W", options: { align: "center" } }],
  [{ text: "Elliptical" }, { text: "4.5 × 0.75 mm", options: { align: "center" } }, { text: "89.3 °C", options: { align: "center" } }, { text: "2.98 W", options: { align: "center" } }],
  [{ text: "Rectangular", options: { bold: true, color: ORANGE_DEEP } }, { text: "4.5 × 0.75 mm", options: { align: "center", bold: true, color: ORANGE_DEEP } }, { text: "78.8 °C", options: { align: "center", bold: true, color: ORANGE_DEEP } }, { text: "1.92 W", options: { align: "center", bold: true, color: ORANGE_DEEP } }],
], [2.35, 2.9, 1.7, 1.8], { before: 0.42 });

statTile(c3, "18 ×", "less pumping power and −48.6 °C: the optimized rectangular channel (78.8 °C at 1.92 W) versus the optimized circular channel (127.4 °C at 34.8 W).", { bigW: 2.5 });

fig(c3, "ecce_fig9_tempmaps", "Temperature fields at each shape's minimum-temperature design: (a) circular, (b) rectangular, (c) elliptical. All optima are wide, shallow channels.");

head(c3, "Conclusions");
bullets(c3, [
  "The channel interior is electromagnetically “dead” — AC-loss penalty < 0.25 %: the channel can be shaped purely for cooling.",
  "Wetted perimeter within the fixed conductor envelope sets the thermal ranking: rectangle > ellipse ≫ circle.",
  "An equal-area swap from round to rectangular already buys −10 °C peak temperature.",
  "The optimized 4.5 × 0.75 mm rectangular channel reaches 78.8 °C at only 1.92 W pumping power.",
  "Next: manufacturing of the optimized hollow profiles and experimental validation on a motorette.",
]);

c3.y += 0.42;
slide.addText("This work was supported by the Academy of Finland Centre of Excellence in High-Speed Electromechanical Energy Conversion Systems and by Danfoss Editron.", {
  x: c3.x, y: c3.y, w: COLW, h: 0.95, margin: 0, fontFace: FONT, fontSize: 18.5, italic: true, color: GRAY, valign: "top", lineSpacingMultiple: 1.12,
});
c3.y += 0.95;

console.log("col3 end:", c3.y.toFixed(2), "target <", BOTTOM);

// ---------- footer ----------
slide.addShape(pres.ShapeType.line, { x: ML, y: RULE_Y, w: CW, h: 0, line: { color: ORANGE, width: 3 } });
slide.addText("RESEARCH TEAM\nCONTACT", {
  x: ML, y: 42.98, w: 5.6, h: 1.1, margin: 0, fontFace: FONT, fontSize: 23, bold: true, color: ORANGE,
  valign: "top", lineSpacingMultiple: 1.12, charSpacing: 1.5,
});
slide.addText("ICEM 2026 · ECCE 2026", {
  x: ML, y: 44.25, w: 5.6, h: 0.45, margin: 0, fontFace: FONT, fontSize: 18, italic: true, color: GRAY,
});

const contacts = [
  [["Hüseyin Tayyer Canseven", "huseyin.canseven@lut.fi"], ["Pratik Bisale", "pratik.bisale@lut.fi"]],
  [["Ilya Petrov", "ilya.petrov@lut.fi"], ["Lassi Aarniovuori", "lassi.aarniovuori@lut.fi"]],
  [["Juho Montonen", "juho.montonen@danfoss.com"], ["Juha Pyrhönen", "juha.pyrhonen@lut.fi"]],
];
contacts.forEach((pair, i) => {
  const runs = [];
  pair.forEach(([name, mail], j) => {
    runs.push({ text: name, options: { bold: true, fontSize: 19.5, color: INK, breakLine: true, paraSpaceAfter: 2 } });
    runs.push({ text: mail, options: { fontSize: 18.5, color: GRAY, breakLine: j === 0, paraSpaceAfter: j === 0 ? 10 : 0 } });
  });
  slide.addText(runs, {
    x: 8.87 + i * 7.33, y: 42.98, w: 7.0, h: 2.6, margin: 0, fontFace: FONT, valign: "top", lineSpacingMultiple: 1.08,
  });
});

pres.writeFile({ fileName: __dirname + "/Poster_CoolingChannelShape.pptx" }).then(() => console.log("WROTE pptx"));
