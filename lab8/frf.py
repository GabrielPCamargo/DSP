import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import math

fs=5000
fp=2000

N=1000

n = np.arange(0,N)

deslo=math.ceil(N-1)/2
wc=(2*fp/fs)*np.pi
m=n-deslo

hd=np.sin(np.pi*m)/(np.pi*m) - np.sin(0.5*np.pi*m)/(np.pi*m) + np.sin(0.2*np.pi*m)/(np.pi*m)
plt.stem(hd)
plt.show()

plt.title('Resposta em Frequência N=' + str(N))
plt.ylabel('Amplitude')
plt.xlabel('Frequencia (rad/sample)')
w,h=signal.freqz(hd,1)
plt.plot(w/np.pi,abs(h))
plt.show()