import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
dados = np.array([7, 14, 11, 43, 
38,61,75,38,12,18,18,17,19,32,42,57,44,114,35,11,13,10])
conv = np.empty(len(dados) + 1)


for i in range(len(dados) + 1):
    if i == 0:
        conv[i] = dados[i]*0.5
    elif i == len(dados):
        conv[i] = dados[i-1]*0.5
    else:
        conv[i] = dados[i]*0.5 + dados[i-1]*0.5

plt.plot(dados)
plt.plot(conv)
plt.show()