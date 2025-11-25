import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize_scalar
def f(x):
    return x**4 - 3*x**2 + 2
res = minimize_scalar(f, bounds=(-2, 3), method='bounded')
x = np.linspace(-2, 3, 500)
y = f(x)
plt.plot(x, y)
plt.scatter(res.x, res.fun, color='red')
plt.show()
print(res.x, res.fun)