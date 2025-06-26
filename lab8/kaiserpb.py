import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt

numtaps = 116
wc = 0.3
wd = 0.5
beta = 2.78298  # valor típico para janela Kaiser com boa atenuação

# Filtro com janela de Kaiser
b = signal.firwin(numtaps, [wc, wd], window=('kaiser', beta), pass_zero='bandpass')

# Resposta em frequência
w, h = signal.freqz(b)

# Plot
plt.title('Resposta em Frequência - Janela Kaiser')
plt.plot(w/np.pi, 20*np.log10(np.abs(h)), label=f'Kaiser (beta={beta})')
plt.ylabel('Ganho (dB)')
plt.xlabel('Frequência (rad/sample)')
plt.grid()
plt.legend()
plt.show()
