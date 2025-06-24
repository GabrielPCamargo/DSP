import scipy.signal as signal
import numpy as np
import matplotlib.pyplot as plt

b = [0,5,0]  # Sem zeros nas bordas
a = [1, -1.3, 0.4]

# resposta em frequencia
w, h = signal.freqz(b, a)

amplitude = np.abs(h)
phase = np.angle(h, deg=True)

# Plot
plt.figure(figsize=(10, 6))

# Amplitude
plt.subplot(2, 1, 1)
plt.plot(w / np.pi, amplitude)
plt.title('Reposta em Frequência')
plt.ylabel('Amplitude')
plt.grid()

# Phase
plt.subplot(2, 1, 2)
plt.plot(w / np.pi, phase)
plt.ylabel('Fase (Graus)')
plt.xlabel('Frequência normalizada (×π rad/amostra)')
plt.grid()

# aplicação da função:
dados = np.array([7, 14, 11, 43, 38, 61, 75, 38, 12, 18, 18, 17, 
                  19, 32, 42, 57, 44, 114, 35, 11, 13, 10])

saida = signal.lfilter(b, a, dados)


plt.figure(figsize=(10, 5))
plt.plot(dados, label='Entrada')
plt.plot(saida, label='Saída filtrada')
plt.xlabel('Amostra')
plt.ylabel('Valor')
plt.legend()
plt.grid()
plt.show()

#Equação de diferenças 0.4y[n]-1,3y[n+1]+y[n+2]=5x[n+1]

#resposta ao impulso

system = signal.dlti(b, a, dt=1)
t, y = signal.dimpulse(system, n=30)

plt.stem(t, np.squeeze(y), basefmt=" ")
plt.xlabel('n')
plt.ylabel('Amplitude')
plt.title('Resposta ao Impulso')
plt.grid()
plt.show()
