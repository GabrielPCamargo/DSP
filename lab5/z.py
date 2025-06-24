import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import tf2zpk

# Sistema 1
b1 = [1]
a1 = [1, -1.845, 0.850586]
z1, p1, _ = tf2zpk(b1, a1)

# Sistema 2 (exemplo diferente — você pode ajustar)
b2 = [1]  # Dois zeros
a2 = [1, -1.85, 0.85]  # Dois polos diferentes
z2, p2, _ = tf2zpk(b2, a2)

# Plot
plt.figure(figsize=(6,6))
ax = plt.subplot(1,1,1)

# Círculo unitário
uc = plt.Circle((0,0), radius=1, fill=False, linestyle='--', color='gray')
ax.add_patch(uc)

# Sistema 1
plt.plot(np.real(p1), np.imag(p1), 'rx', label='Polos H(z)', markersize=7)

# Sistema 2
plt.plot(np.real(p2), np.imag(p2), 'mx', label='Polos Hap(z)', markersize=7)

# Configurações do gráfico
plt.axhline(0, color='black', lw=1)
plt.axvline(0, color='black', lw=1)
plt.grid(True)
plt.xlabel('Re(z)')
plt.ylabel('Im(z)')
plt.title('Polos no plano z')
plt.legend()
plt.axis('equal')
plt.xlim([-1.5, 1.5])
plt.ylim([-1.5, 1.5])
plt.show()


# system2 = signal.dlti(b, a, dt=1)
# t2, y2 = signal.dimpulse(system2, n=100)

# plt.figure(figsize=(10, 4))
# plt.stem(t2, np.squeeze(y2), basefmt=" ")
# plt.xlabel('n')
# plt.ylabel('Amplitude')
# plt.title('Resposta ao Impulso - IIR')
# plt.grid()
# plt.show()
