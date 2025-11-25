import numpy as np
from scipy import signal

t = np.linspace(0, 1, 500)
x = np.sin(2 * np.pi * 7 * t) + np.random.randn(500)
b, a = signal.butter(3, 0.05)
filtered = signal.filtfilt(b, a, x)
print(filtered)