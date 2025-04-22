import numpy as np
import matplotlib.pyplot as plt

Fs = 150                         # sampling rate
Ts = 1.0/Fs                      # sampling interval
t = np.arange(0,1,Ts)            # time vector
ff = 10 
y = np.sin(2 * np.pi * ff * t) + np.sin(2*np.pi * 15 * t)


plt.subplot(2,1,1)
plt.plot(t,y,'k-')
plt.xlabel('time')
plt.ylabel('amplitude')

plt.subplot(2,1,2)
n = len(y)                       # tamanho do sinal signal

k = np.arange(n)
T = n/Fs
frq = k/T # two sides frequency range
freq = frq[range(int(n/2))]           # one side frequency range

Y = np.fft.fft(y)/n              # fft computing and normalization
Y = Y[range(int(n/2))]

plt.plot(freq, abs(Y), 'r-')
plt.xlabel('freq (Hz)')
plt.ylabel('|Y(freq)|')

plt.show() 