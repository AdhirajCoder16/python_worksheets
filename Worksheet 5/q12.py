import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import root_scalar
coeffs = [1, 0, -5, 6, 1]  # x^4 + 0x^3 -5x^2 + 6x + 1
def poly(x):
    return coeffs[0]*x**4 + coeffs[1]*x**3 + coeffs[2]*x**2 + coeffs[3]*x + coeffs[4]
roots = np.roots(coeffs)
x = np.linspace(-3, 3, 400)
plt.plot(x, poly(x))
plt.scatter(roots.real, np.zeros_like(roots), color='red')
plt.show()
print(roots)