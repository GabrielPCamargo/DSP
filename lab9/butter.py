import scipy.io.wavfile
import scipy.signal
import matplotlib.pyplot as plt
import numpy as np
import sounddevice as sd
from scipy.io.wavfile import write

# Carrega o áudio
filename = 'chorus.wav'
fs, wave = scipy.io.wavfile.read(filename)

print('Data:', wave)
print('Sampling rate:', fs)
print('Audio length:', wave.shape[0]/fs, 'seconds')
print('Lowest amplitude:', wave.min())
print('Highest amplitude:', wave.max())

# Usa um canal se for estéreo
if wave.ndim > 1:
    wave = wave[:, 0]

# FFT do sinal original
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

# Filtro Butterworth
fc = 940  # frequência de corte em Hz
wc = fc / (fs / 2)  # frequência normalizada

b, a = scipy.signal.butter(7, wc, 'low')

# Resposta em frequência
w, h = scipy.signal.freqz(b, a)

plt.figure()
plt.plot(w / np.pi * (fs / 2), abs(h))
plt.xlabel('Frequência (Hz)')
plt.ylabel('|H(freq)|')
plt.title('Resposta em frequência - Butterworth')
plt.grid()
plt.show()

# Aplica o filtro com filtfilt para evitar defasagem
filtrado = scipy.signal.filtfilt(b, a, wave)

# Sinal filtrado no tempo
plt.figure()
plt.plot(filtrado)
plt.title('Sinal Filtrado (Butterworth)')
plt.xlabel('Amostra')
plt.ylabel('Amplitude')
plt.grid()
plt.show()

# FFT do sinal filtrado
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
plt.title('FFT do Sinal Filtrado')
plt.grid()
plt.show()

# Reproduz original
wave_play = wave.astype(np.float32) / np.max(np.abs(wave))
print("Tocando áudio original...")
sd.play(wave_play, samplerate=fs)
sd.wait()

# Reproduz filtrado
filtrado_play = filtrado.astype(np.float32) / np.max(np.abs(filtrado))
print("Tocando áudio filtrado (Butterworth)...")
sd.play(filtrado_play, samplerate=fs)
sd.wait()

# Salva como WAV (int16)
filtrado_int16 = np.int16(filtrado_play * 32767)
output_filename = 'chorus_filtrado_butterworth.wav'
write(output_filename, fs, filtrado_int16)
print(f"Áudio filtrado salvo como '{output_filename}'")
