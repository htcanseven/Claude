# Letter of support — Pasi Peltoniemi (returned signed, 22 September 2026)

*Text as returned, from `incoming/letters/Support_Letter_Peltoniemi_signed_2026-09-22.pdf`.
It supersedes the draft in `letters/Support_Letter_Peltoniemi.md`.*

*He takes the drive chapter, which he calls "the chapter on power-electronic constraints and
converter–machine interaction in high-speed electrical drives". He kept the draft's argument,
that the switch decides the pole number, and rewrote the description of the chapter himself.*

*He draws one boundary worth mirroring in the Chapter 11 abstract. Insulation, bearing
currents, EMC and filtering are treated "through the converter-generated electrical stresses
that drive these phenomena, rather than attempting a complete treatment of the underlying
insulation, bearing or EMC physics". Wiley's reviewers will read the letter beside the table
of contents, so the two should describe the same chapter.*

*Signed. It has no date, no letterhead and no Re: line; it opens straight with "Dear
Editors". Usable as it stands.*

---

Dear Editors,

The plan for this book, and the part I would take in it, was discussed with the authors before the proposal was written. I write to support it and to confirm that I intend to contribute.

My field is power electronics and electric drives. The argument this book makes about the converter is one I would make myself, and it is not the argument usually made. A machine is normally specified first and its converter procured afterwards, as though the drive were a component to be selected once the difficult work is done. At high speed that order fails. The fundamental frequency follows from the speed and the pole number, and the switching frequency a device family can sustain then fixes how many pulses fall within a period. When that number becomes small, the current is no longer what the machine designer assumed it would be, and no amount of control effort recovers it. In practice the switch therefore decides the pole number, which is a decision taken very early and, in my experience, usually without anyone consulting the power electronics.

The literature does not help with this. Books on power electronics assume a well-behaved load, and books on electrical machines assume a supply near enough to sinusoidal. At high speed neither assumption survives. The harmonics that remain at a low pulse ratio are deposited in a rotor; the faster switching that would raise the pulse ratio instead stresses insulation dimensioned under mains-frequency assumptions and drives common-mode currents through the bearings; and the filters that would relieve that bring losses and volume of their own. These are not separate topics. They are one design problem, and I know of no book that presents them as one.

The timing is also right. Silicon carbide and gallium nitride have moved the boundary of what can be built, and the design practice has not caught up with the devices. Machines that were not feasible a few years ago are feasible now, while machines that were perfectly satisfactory now meet rates of voltage rise they were never insulated for. A book that states converter capability as a design constraint and follows its consequences into the machine would be useful now in a way it would not have been ten years ago.

Subject to the publishing contract, I intend to take responsibility for the chapter on power-electronic constraints and converter–machine interaction in high-speed electrical drives. The chapter will formulate the converter interface quantitatively and examine how machine speed and pole number, converter topology, DC-link voltage, switching frequency and modulation determine the voltage and current waveforms supplied to the machine. Particular attention will be given to operation at low switching-to-fundamental-frequency ratios and to the resulting current distortion, harmonic content, common-mode voltage and voltage-rate-of-change stresses.

The role of silicon, silicon-carbide and gallium-nitride technologies will be considered primarily through the operating boundaries they impose or enable, including achievable switching frequency, switching losses and switching-transition speed. These constraints will be combined with converter switching models and representative machine models to establish feasible operating regions for high-speed drives and to demonstrate how converter and machine parameters must be selected together.

Consequences for machine insulation, bearing currents, electromagnetic compatibility and filtering will be discussed through the converter-generated electrical stresses that drive these phenomena, rather than attempting a complete treatment of the underlying insulation, bearing or EMC physics. Representative high-speed-machine examples will be used to demonstrate the resulting converter–machine design trade-offs.

I have worked on power electronic converters, their control and their interaction with electrical machines for 20 years, including different projects, and would bring these works to the book.

Yours sincerely,

[signature]

Prof. Pasi Peltoniemi
Department of Electrical Engineering, LUT University
