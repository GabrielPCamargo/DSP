import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
dados = np.array([7, 14, 11, 43, 
38,61,75,38,12,18,18,17,19,32,42,57,44,114,35,11,13,10])
plt.plot(dados)
a = np.array([1])
b = np.array([0.5, 0.5])
y = signal.lfilter(b, a, dados)
plt.plot(y)
plt.show()