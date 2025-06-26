import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt

fs=15000
wce=2000
## para 40db com fs=15k e 1990 e 2010 foi ordem 3350 com 1980 a 2020 ainda 1676
# foi aumentada a frequencia de 2050 a 1950 pois a ordem estava muito alta

numtaps = 671
wc = (2/fs)*1950
wd = (2/fs)*2050
beta = 3.395321

# print(wc - (2/fs)*wce, wd - (2/fs)*wce )

print(wc, wd)

# Filtro com janela de Kaiser
b = signal.firwin(numtaps, [wc, wd], window=('kaiser', beta), pass_zero='bandstop')

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
