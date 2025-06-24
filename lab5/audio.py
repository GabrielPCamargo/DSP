import scipy.io.wavfile
import scipy.signal
import matplotlib.pyplot as plt
import sounddevice as sd
import numpy as np
import scipy.signal as signal
from scipy.signal import tf2zpk


filename = './chorus.wav'
fs, wave = scipy.io.wavfile.read(filename)

# Converte para float e normaliza
wave = wave.astype(np.float32)
wave /= np.max(np.abs(wave))

# Usa apenas um canal se for estéreo
if wave.ndim > 1:
    wave = wave[:, 0]

# Escuta o som original
print("Tocando original...")
# sd.play(wave, fs)
# sd.wait()

# Cria filtro Chebyshev de segunda espécie (Cheby2)



# # Sistema 1
# z1, p1, _ = tf2zpk(b1, a1)

# # Sistema 2 (exemplo diferente — você pode ajustar)
# z2, p2, _ = tf2zpk(b2, a2)

# # Plot
# plt.figure(figsize=(6,6))
# ax = plt.subplot(1,1,1)

# # Círculo unitário
# uc = plt.Circle((0,0), radius=1, fill=False, linestyle='--', color='gray')
# ax.add_patch(uc)

# # Sistema 1
# plt.plot(np.real(z1), np.imag(z1), 'go', label='Zeros filtro 1', markersize=7)
# plt.plot(np.real(p1), np.imag(p1), 'rx', label='Polos filtro 1', markersize=7)

# # Sistema 2
# plt.plot(np.real(z2), np.imag(z2), 'bo', label='Zeros filtro 2', markersize=7)
# plt.plot(np.real(p2), np.imag(p2), 'mx', label='Polos filtro 2', markersize=7)

# # Configurações do gráfico
# plt.axhline(0, color='black', lw=1)
# plt.axvline(0, color='black', lw=1)
# plt.grid(True)
# plt.xlabel('Re(z)')
# plt.ylabel('Im(z)')
# plt.title('Polos no plano z')
# plt.legend()
# plt.axis('equal')
# plt.xlim([-1.5, 1.5])
# plt.ylim([-1.5, 1.5])
# plt.show()

b1, a1 = scipy.signal.cheby2(7, 10, 0.8, output='ba')
saida1 = scipy.signal.lfilter(b1, a1, wave)

# Filtro 2 (exemplo diferente)
b2, a2 = scipy.signal.cheby2(7, 10, 0.5, output='ba')
saida2 = scipy.signal.lfilter(b2, a2, wave)

# Tempo para o eixo x
tempo = np.linspace(0, len(wave) / fs, num=len(wave))

# Filtra o sinal
plt.figure(figsize=(12, 8))

plt.subplot(3, 1, 1)
plt.plot(tempo, wave)
plt.title("Áudio Original")
plt.xlabel("Tempo [s]")
plt.ylabel("Amplitude")
plt.grid()

plt.subplot(3, 1, 2)
plt.plot(tempo, saida1)
plt.title("Filtro cheby2 - janela 0.8)")
plt.xlabel("Tempo [s]")
plt.ylabel("Amplitude")
plt.grid()

plt.subplot(3, 1, 3)
plt.plot(tempo, saida2)
plt.title("Filtro cheby2 - janela 0.5)")
plt.xlabel("Tempo [s]")
plt.ylabel("Amplitude")
plt.grid()

plt.tight_layout()
plt.show()


# Escuta o sinal filtrado
print("Tocando sinal filtrado...")
# sd.play(saida, fs)
# sd.wait()


