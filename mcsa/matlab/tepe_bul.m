function A = tepe_bul(f, XdB, f0, tol)
%TEPE_BUL f0 +/- tol [Hz] araligindaki en yuksek spektral genligi [dB] dondurur.
%   A = tepe_bul(f, XdB, f0, tol)

    idx = (f >= f0 - tol) & (f <= f0 + tol);
    A = max(XdB(idx));
end
