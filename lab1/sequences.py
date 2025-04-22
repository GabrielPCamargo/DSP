import numpy as np
import matplotlib.pyplot as plt
n_samples = 60
signal = np.zeros(n_samples)
t = np.arange(-30, 30, 1) 

### signal[0] = 1 impulso

# for i in range(30):   degrau
#     signal[30 + i] = 1

# for i in range(20):
#     signal[40 + i] = 1 degrau deslocamento de 10

for i in range(30):
    signal[30 + i] = i # Rampa

# Sinc  Filtro passa baixa ideal e a transformada de fourier de onda retângular
# x=np.linspace(-10, 10, 101)
# plt.plot(x, np.sinc(x))
# plt.title("Sinc Function")
# plt.ylabel("Amplitude")
# plt.xlabel("X")
# plt.show()


plt.stem(t, signal)
plt.show()