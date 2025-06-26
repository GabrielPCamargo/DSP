import scipy.io.wavfile
import scipy.signal
import matplotlib.pyplot as plt
import numpy as np
import sounddevice as sd

filename = 'chorus.wav'
fs, wave = scipy.io.wavfile.read(filename)

print('Data:', wave)
print('Sampling rate:', fs)
print('Audio length:', wave.shape[0]/fs, 'seconds')
print('Lowest amplitude:', wave.min())
print('Highest amplitude:', wave.max())

# FFT
n = len(wave)
k = np.arange(n)
T = n / fs
frq = k / T
freq = frq[range(n // 2)]

Y = np.fft.fft(wave) / n
Y = Y[range(n // 2)]

plt.figure()
plt.plot(freq, abs(Y))
plt.xlabel('Frequency (Hz)')
plt.ylabel('|Y(freq)|')
plt.title('FFT of Original Signal')
plt.grid()
plt.show()

wc = (2 / fs) * 940
b, a = scipy.signal.cheby2(7, 40, wc, 'low', analog=False)
w, h = scipy.signal.freqz(b, a)

plt.figure()
plt.plot(w / np.pi * (fs / 2), abs(h))
plt.xlabel('Frequência (Hz)')
plt.ylabel('|H(freq)|')
plt.title('Resposta em frequência cheby2')
plt.grid()
plt.show()

filtrado = scipy.signal.filtfilt(b, a, wave)

plt.figure()
plt.plot(filtrado)
plt.title('Filtered Signal')
plt.xlabel('Sample')
plt.ylabel('Amplitude')
plt.grid()
plt.show()

n = len(filtrado)
k = np.arange(n)
T = n / fs
frq = k / T
freq = frq[range(n // 2)]

Y = np.fft.fft(filtrado) / n
Y = Y[range(n // 2)]

plt.figure()
plt.plot(freq, abs(Y))
plt.xlabel('Frequency (Hz)')
plt.ylabel('|Y(freq)|')
plt.title('FFT of Original Signal')
plt.grid()
plt.show()

if wave.dtype != np.float32:
    wave_play = wave.astype(np.float32) / np.max(np.abs(wave))
else:
    wave_play = wave

sd.play(wave_play, samplerate=fs)
sd.wait()


# Play filtered audio
filtrado_play = filtrado.astype(np.float32) / np.max(np.abs(filtrado))
print("Playing filtered audio...")
sd.play(filtrado_play, samplerate=fs)
sd.wait()