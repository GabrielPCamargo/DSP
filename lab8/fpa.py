import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import math

fs=5000
fp=2000

N=100

n = np.arange(0,N)

deslo=math.ceil(N-1)/2
wc=(2*fp/fs)*np.pi
m=n-deslo

hd=np.sin(np.pi*m)/(np.pi*m) - np.sin(0.6*np.pi*m)/(np.pi*m)
plt.stem(hd)
plt.show()

w,h=signal.freqz(hd,1)
plt.plot(w/np.pi,abs(h))
plt.show()