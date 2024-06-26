//Frequency components of a signal
//----------------------------------
// build a square wave signal sampled at 1000hz  containing at frequency 1Hz
// and 50% duty cycle

clear;
sample_rate=1000;
frequency=1;
t = 0:1/sample_rate:1;
N=size(t,'*'); //number of samples

//s=sin(2*%pi*frequency*t);
s = squarewave(2*%pi*frequency*t,50)

y=fft(s);

//s is real so the fft response is conjugate symmetric and we retain only the first N/2 points
f=sample_rate*(0:(N/2))/N; //associated frequency vector
n=size(f,'*')
y_mag = abs(y(1:n));
clf();
plot(f,y_mag);
