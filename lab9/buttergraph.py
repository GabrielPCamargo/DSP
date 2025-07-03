import scipy.io.wavfile
import scipy.signal
import matplotlib.pyplot as plt
import numpy as np
import sounddevice as sd

filename = 'chorus.wav'
fs, wave = scipy.io.wavfile.read(filename)

print('Sampling rate:', fs)
print('Audio length:', wave.shape[0]/fs, 'seconds')
print('Lowest amplitude:', wave.min())
print('Highest amplitude:', wave.max())

# Se for estéreo, converte para mono
if wave.ndim > 1:
    wave = wave.mean(axis=1)

# FFT original
n = len(wave)
T = n / fs
freq = np.fft.fftfreq(n, d=1/fs)[:n // 2]
Y = np.fft.fft(wave) / n
Y = Y[:n // 2]

# Filtro
wc = (2 / fs) * 940
b, a = scipy.signal.cheby1(7, 0.2, wc, 'low')
filtrado = scipy.signal.filtfilt(b, a, wave)

# FFT filtrado
Yf = np.fft.fft(filtrado) / n
Yf = Yf[:n // 2]

# Plot original (tempo e FFT)
plt.figure(figsize=(12, 6))

plt.subplot(2, 2, 1)
plt.plot(np.arange(n) / fs, wave)
plt.title('Sinal Original no Tempo')
plt.xlabel('Tempo (s)')
plt.ylabel('Amplitude')
plt.grid()

plt.subplot(2, 2, 2)
plt.plot(freq, np.abs(Y))
plt.title('FFT do Sinal Original')
plt.xlabel('Frequência (Hz)')
plt.ylabel('|Y(freq)|')
plt.grid()

# Plot filtrado (tempo e FFT)
plt.subplot(2, 2, 3)
plt.plot(np.arange(n) / fs, filtrado)
plt.title('Sinal Filtrado no Tempo')
plt.xlabel('Tempo (s)')
plt.ylabel('Amplitude')
plt.grid()

plt.subplot(2, 2, 4)
plt.plot(freq, np.abs(Yf))
plt.title('FFT do Sinal Filtrado')
plt.xlabel('Frequência (Hz)')
plt.ylabel('|Y(freq)|')
plt.grid()

plt.tight_layout()
plt.show()

# Tocar áudios
# print("Reproduzindo áudio original...")
# sd.play(wave.astype(np.float32) / np.max(np.abs(wave)), samplerate=fs)
# sd.wait()

# print("Reproduzindo áudio filtrado...")
# sd.play(filtrado.astype(np.float32) / np.max(np.abs(filtrado)), samplerate=fs)
# sd.wait()


from scipy.io.wavfile import write

# Normaliza para evitar distorção (clipping)
filtrado_norm = filtrado / np.max(np.abs(filtrado))

# Converte para int16 (formato WAV)
filtrado_int16 = np.int16(filtrado_norm * 32767)

# Salva o arquivo
output_filename = 'chorus_filtrado_cheby1.wav'
write(output_filename, fs, filtrado_int16)