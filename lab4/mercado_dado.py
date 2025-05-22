import scipy.signal as signal
import numpy as np
import matplotlib.pyplot as plt

# Dados
dados = np.array([46.5, 47.5, 47.5, 47, 46.125, 45.25, 45.75, 45.875, 45.625, 44.75, 
                  44.375, 44.75, 44.75, 46.5, 46.5, 47.625, 47.75, 48.125, 48.875, 48, 
                  49.75, 49.875, 45, 46, 46, 45.5, 44.625, 43.75, 44.25, 44.375, 
                  44.125, 43.25, 42.875, 43.25, 43.25, 45, 45, 46.125, 46.25, 
                  46.625, 47.375, 46.5, 48.25, 48.375])

# Filtro FIR
b_fir = [1/3, 1/3, 1/3]
a_fir = [1]

saida_fir = signal.lfilter(b_fir, a_fir, dados)

# Filtro IIR
b_iir = [0.2]
a_iir = [1, -0.8]

saida_iir = signal.lfilter(b_iir, a_iir, dados)

# Plotando
plt.figure(figsize=(12, 6))

plt.plot(dados, label='Dados Originais', marker='o')
plt.plot(saida_fir, label='Filtro FIR (Média Móvel)', linestyle='--')
plt.plot(saida_iir, label='Filtro IIR (Recursivo)', linestyle='-.')

plt.xlabel('Amostras')
plt.ylabel('Valor')
plt.title('Aplicação de Filtros FIR e IIR aos Dados')
plt.legend()
plt.grid()
plt.tight_layout()
plt.show()
