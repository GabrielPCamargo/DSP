import scipy.io.wavfile
import scipy.signal
import matplotlib.pyplot as plt  
import sounddevice as sd
from scipy import signal
import numpy as np  

# coloque o caminho de onde está seu arquivo
filename='./../lab1/vogais.wav'

(fs, wave) = scipy.io.wavfile.read(filename) 

n = len(wave)                       # tamanho do sinal signal
Ts = 1.0/fs                      # sampling interval
t = np.arange(0,n)  
t=t/fs
ff1 = 3000 
ff2= 3100                          # frequency of the signal
ruido = 100*np.sin(2 * np.pi * ff1 * t) + 200*np.sin(2 * np.pi * ff2 * t)
plt.plot(ruido[1:1000])

sinal_ruidoso=wave +ruido

plt.plot(sinal_ruidoso)

# visualizando 

n = len(sinal_ruidoso)                       # tamanho do sinal signal
k = np.arange(n)
T = n/fs
frq = k/T # two sides frequency range
freq = frq[range(int(n/2))]           # one side frequency range

Y = np.fft.fft(wave)/n              # fft computing and normalization
Y = Y[range(int(n/2))]

Y2 = np.fft.fft(sinal_ruidoso)/n              # fft computing and normalization
Y2 = Y2[range(int(n/2))]

plt.show()

plt.subplot(3,1,1)
plt.plot(freq, abs(Y))
plt.xlabel('freq (Hz)')
plt.ylabel('|Y(freq)|')


plt.subplot(3,1,2)
plt.plot(freq, abs(Y2), 'r-')
plt.xlabel('freq (Hz)')
plt.ylabel('|Y(freq)|')


fc=3000# frequência de Corte
w=fc/(fs/2) # conversão do Sinal 
b,a = signal.butter(2, w, 'low')
filtered = signal.filtfilt(b, a, sinal_ruidoso) 

Y3 = np.fft.fft(filtered)/n              # fft computing and normalization
Y3 = Y3[range(int(n/2))]

plt.subplot(3,1,3)
plt.plot(freq, abs(Y3), 'r-')
plt.xlabel('freq (Hz)')
plt.ylabel('|Y3(freq)|')
plt.show()  

print("Tocando áudio original...")
sd.play(wave, fs)
sd.wait()

print("Tocando áudio com ruído...")
sd.play(sinal_ruidoso, fs)
sd.wait()

print("Tocando áudio filtrado...")
sd.play(filtered, fs)
sd.wait()