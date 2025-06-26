import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt
numtaps = 401
wc = 0.2
wd = 0.5
b1= signal.firwin(numtaps, [wc, wd],window='boxcar', pass_zero='bandpass')
b2= signal.firwin(numtaps, [wc, wd],window='hamming', pass_zero='bandpass')
b3= signal.firwin(numtaps, [wc, wd],window='blackman', pass_zero='bandpass')

w1, h1 = signal.freqz(b1)
w2, h2 = signal.freqz(b2)
w3, h3 = signal.freqz(b3)
plt.title('Resposta em Frequência - Filtro FIR Digital ')
plt.plot(w1/np.pi, 20*np.log10(np.abs(h1)), 'b', label='Boxcar')
plt.plot(w2/np.pi, 20*np.log10(np.abs(h2)), 'r', label='Hamming')
plt.plot(w3/np.pi, 20*np.log10(np.abs(h3)), 'g', label='Blackman')
plt.ylabel('Módulo da Amplitude em (dB)')
plt.xlabel('Frequencia (rad/sample ou rd/amostra)')
plt.grid()
plt.legend()
plt.show()