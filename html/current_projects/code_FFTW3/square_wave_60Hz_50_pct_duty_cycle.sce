//Frequency components of a signal
//----------------------------------
// build a square wave signal sampled at 10000hz  containing at frequency 60Hz
// and 50% duty cycle, 95% duty cycle, and 99% duty cycle

clear;
sample_rate=10000;
frequency=60;
t = 0:1/sample_rate:1;
N=size(t,'*'); //number of samples

// Generate squarewaves
s_50 = squarewave(2*%pi*frequency*t,50);
s_95 = squarewave(2*%pi*frequency*t,95);
s_99 = squarewave(2*%pi*frequency*t,99); 

// Perform FFTs
y_50=fft(s_50);
y_95=fft(s_95);
y_99=fft(s_99);

// Setup plotting vectors
//squarewaves are real so the fft response is conjugate symmetric and we retain only the first N/2 points
f=sample_rate*(0:(N/2))/N; //associated frequency vector
n=size(f,'*')
y_mag_50 = abs(y_50(1:n));
y_mag_95 = abs(y_95(1:n));
y_mag_99 = abs(y_99(1:n));
clf();

// Generate plots


// Time domain plots
a=get("current_axes");
a.data_bounds=[0,0;1,2];
xtitle('f(t)', 'Time [s]', 'Amplitude [Arb Units]');

h=0;
scf(h);
xset('window',h);
plot(t, s_50(1:N), 'g-');
plot(t, s_95(1:N), 'r-');
plot(t, s_99(1:N), 'b-');
hl = legend(['50% Duty Cycle'; '95% Duty Cycle'; '99% Duty Cycle']);

// Frequency domain plots
h=1;
scf(h);
xset('window',h);
a=get('current_axes');
a.data_bounds=[0,0;1000,1000];
xtitle('FFT(f(t))', 'Freq [Hz]', 'Amplitude [Arb Units - Linear]');

plot (f, abs(y_mag_50(1:n)), 'g-');
plot (f, abs(y_mag_95(1:n)), 'r-');
plot (f, abs(y_mag_99(1:n)), 'b-');
hl = legend(['50% Duty Cycle'; '95% Duty Cycle'; '99% Duty Cycle']);


