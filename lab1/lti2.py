import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
x = np.array([3.0, 11.0, 7.0, 0.0, -1, 4, 2])
h = np.array([2.0, 3.0, -5.0, 2.0, 1.0])
# Define the starting indices
n_x = np.arange(-3, -3 + len(x))  # x starts at -3
n_h = np.arange(0, len(h))        # h starts at 0
n_y = np.arange(n_x[0] + n_h[0], n_x[-1] + n_h[-1] + 1)  # Convolution result range

# Compute convolution
y = signal.convolve(x, h)

# Plot
f, a = plt.subplots(ncols=3, figsize=(20, 5))
a[0].stem(n_x, x)
a[0].set_title("x[n]")
a[1].stem(n_h, h)
a[1].set_title("h[n]")
a[2].stem(n_y, y)
a[2].set_title("y[n] = x[n] * h[n]")
plt.show()