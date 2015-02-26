//Frequency components of a signal
//----------------------------------
// build a signal sampled at 1000hz  containing a pure frequency
// at 10Hz
sample_rate=1000;
frequency=10;
t = 0:1/sample_rate:1;
N=size(t,'*'); //number of samples

s=sin(2*%pi*frequency*t);

y=fft(s);

//s is real so the fft response is conjugate symmetric and we retain only the first N/2 points
f=sample_rate*(0:(N/2))/N; //associated frequency vector
n=size(f,'*')
clf()
plot(f,abs(y(1:n)))
