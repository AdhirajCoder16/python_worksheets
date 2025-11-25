import numpy as np
from scipy.fftpack import fft2

a = np.random.rand(3, 3)
result = fft2(a)
print(result)