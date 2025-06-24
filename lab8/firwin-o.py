import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt
numtaps = 1001
wc = 0.2
b1= signal.firwin(numtaps, [0.2, 0.6],window='boxcar', pass_zero='bandpass')
b2= signal.firwin(numtaps, [0.3, 1/3],window='hamming', pass_zero='bandpass')
b3= signal.firwin(numtaps, wc,window='blackman')

w1, h1 = signal.freqz(b1)
w2, h2 = signal.freqz(b2)
w3, h3 = signal.freqz(b3)
plt.title('Resposta em Frequência - Filtro FIR Digital ')
plt.plot(w1/np.pi, 20*np.log10(np.abs(h1)), 'b')
plt.plot(w2/np.pi, 20*np.log10(np.abs(h2)), 'r')
plt.plot(w3/np.pi, 20*np.log10(np.abs(h3)), 'g')
plt.ylabel('Módulo da Amplitude em (dB)')
plt.xlabel('Frequencia (rad/sample ou rd/amostra)')
plt.grid()
plt.show()