import numpy as np
import matplotlib.pyplot as plt

# Parâmetros
Ts = 1/100  # Período de amostragem (sinal contínuo)
Fs = 1.0/Ts  # Frequência de amostragem
t = np.arange(0, 2, Ts)  # Vetor de tempo para o sinal "contínuo"
t1 = np.arange(0, 2 + 1/10, 1/10)  # Vetor de tempo com Ts=1/10s
t2 = np.arange(0, 2 + 1/2, 1/2)   # Vetor de tempo com Ts=1/2s
freq_sinal = 1

# Sinais senoidais
seno_discreto = np.sin(2 * np.pi * freq_sinal * t)
seno_discreto1 = np.sin(2 * np.pi * freq_sinal * t1)
seno_discreto2 = np.sin(2 * np.pi * freq_sinal * t2)

# Criação dos gráficos
plt.figure(figsize=(10, 8))

plt.subplot(4, 1, 1)
plt.plot(t, seno_discreto, 'k-')
plt.xlabel('Tempo (s)')
plt.ylabel('Sinal Analógico')
plt.title('Seno com diferentes períodos de amostragem')

plt.subplot(4, 1, 2)
plt.stem(t, seno_discreto, '--')
plt.ylabel('Ts=1/100s')

plt.subplot(4, 1, 3)
plt.stem(t1, seno_discreto1, '--')
plt.ylabel('Ts=1/10s')

plt.subplot(4, 1, 4)
plt.stem(t2, seno_discreto2, '--')
plt.ylabel('Ts=1/2s')
plt.ylim(-1, 1)

plt.tight_layout()  # Ajusta o espaçamento entre os subplots
plt.show()