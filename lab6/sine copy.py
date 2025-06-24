import numpy as np
import matplotlib.pyplot as plt

Ts = 1/600  # Período de amostragem
Fs = 1.0/Ts  # Frequência de amostragem
t = np.arange(0, 0.5, Ts)  # Vetor de tempo (3000 Hz)
t1 = np.arange(0, 0.5 + 1/241, 1/241)  # Vetor de tempo (61 Hz)
t2 = np.arange(0, 0.5 + 1/41, 1/41)  # Vetor de tempo (60 Hz)
freq_sinal = 30

# Sinal com fase ajustada para evitar zeros na amostragem a 60 Hz
seno_discreto = np.sin(2 * np.pi * freq_sinal * t)
seno_discreto1 = np.sin(2 * np.pi * freq_sinal * t1)
seno_discreto2 = np.sin(2 * np.pi * freq_sinal * t2)  # Adiciona fase de π/2

plt.figure(figsize=(10, 8))

plt.subplot(4, 1, 1)
plt.plot(t, seno_discreto, 'k-')
plt.xlabel('Tempo (s)')
plt.ylabel('Sinal analógico')
plt.title('Seno com diferentes períodos de amostragem')

plt.subplot(4, 1, 2)
plt.stem(t, seno_discreto, '--')
plt.xlabel('Tempo (s)')
plt.ylabel('Ts=1/600s')

plt.subplot(4, 1, 3)
plt.stem(t1, seno_discreto1, '--')
plt.xlabel('Tempo (s)')
plt.ylabel('Ts=1/241s')

plt.subplot(4, 1, 4)
plt.stem(t2, seno_discreto2, '--')
plt.xlabel('Tempo (s)')
plt.ylabel('Ts=1/41s')

plt.tight_layout()  # Ajusta o espaçamento entre subplots
plt.show()