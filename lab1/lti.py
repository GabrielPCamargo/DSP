import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
x = np.array([1.0, 0.0, 2.0, 0.0, 0.0, -1])
h = np.array([3.0, 2.0, 1.0])
y=signal.convolve(x, h)
f,a = plt.subplots(ncols=3, figsize=(20,5))
a[0].stem(x)
a[1].stem(h)
a[2].stem(y)
plt.show()