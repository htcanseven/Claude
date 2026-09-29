%% MCSA - Ilk Adim: Sentetik stator akiminda kirik rotor cubugu yan bantlari
% Amac: Simulink modeline gecmeden once MCSA'nin temel mantigini gormek.
%   1) Saglam ve "kirik cubuklu" iki stator akimi sentezlenir.
%   2) Hann pencereli FFT ile genlik spektrumu hesaplanir (dB, temel bilesene gore).
%   3) (1 -/+ 2s)f_s yan bantlari aranir ve isaretlenir.
%   4) Kayit suresi kisa tutulursa yan bantlarin neden kayboldugu gosterilir.
%
% Sadece temel MATLAB fonksiyonlari kullanir (ek toolbox gerekmez); GNU Octave ile de
% calisir. Yardimci fonksiyonlar ayni klasordedir: genlik_spektrumu_dB.m, tepe_bul.m

clear; close all; clc;

%% 1) Motor ve olcum parametreleri (ornek degerler)
fs_hat = 50;      % Sebeke (besleme) frekansi f_s [Hz]
s      = 0.01;    % Kayma (slip); hafif yuklu bir motor icin tipik
Fs     = 5000;    % Ornekleme frekansi [Hz]
T      = 20;      % Kayit suresi [s]  ->  frekans cozunurlugu = 1/T = 0.05 Hz
I1     = 10;      % Temel bilesen genligi [A]

% Kirik cubuk yan bandinin temel bilesene gore bagil genligi [dB].
% Saglam motorlarda bu fark genellikle cok buyuktur (yan bant -50 dB'in altinda);
% fark kuculdukce ariza siddeti artar. Pratik esikler icin yol haritasina bakin.
Asb_dB = -40;

t = (0:1/Fs:T-1/Fs).';
N = numel(t);

%% 2) Sentetik sinyaller
f_lsb = (1 - 2*s)*fs_hat;   % alt yan bant  (1-2s)f_s : rotor asimetrisinin dogrudan izi
f_usb = (1 + 2*s)*fs_hat;   % ust yan bant  (1+2s)f_s : hiz dalgalanmasindan dogar
Asb   = I1*10^(Asb_dB/20);

rng(1);                                   % tekrarlanabilir gurultu
gurultu  = 0.002*I1*randn(N,1);           % olcum gurultusu
i_saglam = I1*sin(2*pi*fs_hat*t) + gurultu;
i_ariza  = I1*sin(2*pi*fs_hat*t) ...
         + Asb*sin(2*pi*f_lsb*t + 0.3) ...
         + 0.8*Asb*sin(2*pi*f_usb*t - 0.7) ...
         + gurultu;

%% 3) Spektrum hesabi (tek tarafli, Hann pencereli, dB rel. temel bilesen)
[f, X_saglam] = genlik_spektrumu_dB(i_saglam, Fs);
[~, X_ariza ] = genlik_spektrumu_dB(i_ariza,  Fs);

%% 4) Yan bantlarin tespiti
tol = 0.2;  % arama penceresi [Hz]
yb_saglam = [tepe_bul(f, X_saglam, f_lsb, tol), tepe_bul(f, X_saglam, f_usb, tol)];
yb_ariza  = [tepe_bul(f, X_ariza,  f_lsb, tol), tepe_bul(f, X_ariza,  f_usb, tol)];

fprintf('Frekans cozunurlugu  : %.3f Hz (T = %g s)\n', Fs/N, T);
fprintf('Beklenen yan bantlar : %.2f Hz ve %.2f Hz\n', f_lsb, f_usb);
fprintf('Saglam motor         : LSB = %6.1f dB, USB = %6.1f dB\n', yb_saglam);
fprintf('Kirik cubuklu motor  : LSB = %6.1f dB, USB = %6.1f dB\n', yb_ariza);

%% 5) Cizim
figure('Name', 'MCSA - kirik rotor cubugu');
subplot(2,1,1);
plot(f, X_saglam, 'Color', [0.6 0.6 0.6]); hold on;
plot(f, X_ariza, 'b');
plot([f_lsb f_usb], yb_ariza + 3, 'rv', 'MarkerFaceColor', 'r');
xlim([45 55]); ylim([-110 5]); grid on;
xlabel('Frekans [Hz]'); ylabel('Genlik [dB, temel bilesene gore]');
legend('Saglam', 'Kirik cubuk', '(1 \pm 2s)f_s', 'Location', 'northwest');
title(sprintf('T = %g s (\\Deltaf = %.2f Hz): yan bantlar net', T, Fs/N));

%% 6) Cozunurluk deneyi: ayni sinyalin sadece 1 saniyesi analiz edilirse?
N1 = round(1*Fs);
[f1, X1] = genlik_spektrumu_dB(i_ariza(1:N1), Fs);
yb_kisa  = [tepe_bul(f1, X1, f_lsb, 0.5), tepe_bul(f1, X1, f_usb, 0.5)];
fprintf('T = 1 s ile          : LSB konumunda %6.1f dB (temel bilesenin sizintisi!)\n', yb_kisa(1));

subplot(2,1,2);
plot(f1, X1, 'b-o', 'MarkerSize', 3); hold on;
plot([f_lsb f_usb], [3 3], 'rv', 'MarkerFaceColor', 'r');
xlim([45 55]); ylim([-110 5]); grid on;
xlabel('Frekans [Hz]'); ylabel('Genlik [dB]');
title(sprintf('T = 1 s (\\Deltaf = %.0f Hz): yan bantlar kayboldu', Fs/N1));

% --- Kendi deneyleriniz ---
% * s = 0.03 yapin (tam yuk): yan bantlar 50 Hz'den uzaklasir, kisa kayit bile yetebilir.
% * s = 0.002 yapin (bosta calisma): T = 20 s bile zorlanir -> Hilbert/MUSIC yontemleri
%   neden gelistirilmis, yol haritasinin sinyal isleme bolumunde okuyun.
% * Pencereyi kaldirin (w = ones(N,1)) ve sizintinin nasil arttigini gorun.
% * Asb_dB'yi -60 dB'ye indirin: gurultu tabaniyla yarisan baslangic asamasi ariza.
