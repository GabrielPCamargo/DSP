# y[n]=1/3x[n]+1/3x[n-1]+1/3x[n-2]
# y[n]=0.8y[n-1]+0.2x[n]

import scipy.signal as signal
import numpy as np
import matplotlib.pyplot as plt

# Sistema 1: FIR
b1 = [1/3, 1/3, 1/3]
a1 = [1, 0, 0]

system1 = signal.dlti(b1, a1, dt=1)
t1, y1 = signal.dimpulse(system1, n=10)

plt.figure(figsize=(10, 4))
plt.stem(t1, np.squeeze(y1), basefmt=" ")
plt.xlabel('n')
plt.ylabel('Amplitude')
plt.title('Resposta ao Impulso - FIR')
plt.xticks(np.arange(t1.min(), t1.max() + 1, 1))  # <<< aqui
plt.grid()
plt.show()


# Sistema 2: IIR
b2 = [0.2]
a2 = [1, -0.8]

system2 = signal.dlti(b2, a2, dt=1)
t2, y2 = signal.dimpulse(system2, n=20)

plt.figure(figsize=(10, 4))
plt.stem(t2, np.squeeze(y2), basefmt=" ")
plt.xlabel('n')
plt.ylabel('Amplitude')
plt.title('Resposta ao Impulso - IIR')
plt.xticks(np.arange(t2.min(), t2.max() + 1, 1))  # <<< aqui
plt.grid()
plt.show()
