import numpy as np
from scipy import interpolate

x = np.linspace(0, 10, 10)
y = np.sin(x)
f = interpolate.interp1d(x, y)
xnew = np.linspace(0, 10, 50)
ynew = f(xnew)
print(ynew)