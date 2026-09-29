function [f, XdB] = genlik_spektrumu_dB(x, Fs)
%GENLIK_SPEKTRUMU_DB Tek tarafli genlik spektrumu (dB, en buyuk bilesene gore).
%   [f, XdB] = genlik_spektrumu_dB(x, Fs)
%   x  : zaman sinyali (vektor), Fs : ornekleme frekansi [Hz]
%   f  : frekans ekseni [Hz],  XdB : 20*log10(|X|/max|X|) -> temel bilesen 0 dB olur.
%   Hann penceresi kullanir; Signal Processing Toolbox gerektirmez.

    x = x(:) - mean(x);
    N = numel(x);
    w = 0.5 - 0.5*cos(2*pi*(0:N-1).'/(N-1));   % Hann penceresi
    X = abs(fft(x .* w)) / sum(w);              % pencere kazanci duzeltmesi
    X = X(1:floor(N/2)+1);
    X(2:end-1) = 2*X(2:end-1);                  % tek tarafli spektrum
    f = (0:numel(X)-1).' * Fs / N;
    XdB = 20*log10(X / max(X) + eps);
end
