import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import math

def calcular_hd(N_val, fs_val=5000, fp_val=2000):
    n = np.arange(0, N_val)
    deslo = math.ceil((N_val - 1) / 2)
    wc = 0.6 * np.pi
    m = n - deslo

    hd = np.zeros(N_val)
    for i, val_m in enumerate(m):
        if val_m == 0:
            hd[i] = wc / np.pi
        else:
            hd[i] = np.sin(np.pi * val_m) / (np.pi * val_m) - np.sin(wc * val_m) / (np.pi * val_m)
    return n, hd

# Parâmetros
Ns = [10, 100, 1000]
fs_global = 5000
fp_global = 2000

# Criar figura com 3 linhas e 2 colunas
fig, axs = plt.subplots(len(Ns), 2, figsize=(12, 9))
fig.suptitle('Respostas ao Impulso e em Frequência para diferentes N', fontsize=16)

for i, N_val in enumerate(Ns):
    n, hd = calcular_hd(N_val, fs_global, fp_global)
    w, h = signal.freqz(hd, 1)

    # Resposta ao impulso
    axs[i, 0].stem(n, hd, basefmt=" ", linefmt="b-", markerfmt="bo")
    axs[i, 0].set_title(f'Resposta ao Impulso (N = {N_val})')
    axs[i, 0].set_xlabel('n')
    axs[i, 0].set_ylabel('Amplitude')
    axs[i, 0].grid(True, linestyle='--', alpha=0.6)

    # Resposta em frequência
    axs[i, 1].plot(w / np.pi, abs(h), label='|H(jω)|')
    axs[i, 1].axvline(x=(0.6), color='r', linestyle='--', label='Frequência de corte')
    axs[i, 1].set_title(f'Resposta em Frequência (N = {N_val})')
    axs[i, 1].set_xlabel('Frequência Normalizada (ω/π)')
    axs[i, 1].set_ylabel('Magnitude')
    axs[i, 1].grid(True, linestyle='--', alpha=0.6)
    axs[i, 1].legend()

plt.tight_layout(rect=[0, 0, 1, 0.96])  # Ajusta para não sobrepor o título
plt.show()
