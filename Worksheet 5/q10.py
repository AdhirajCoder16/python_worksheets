import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
def func(t, a, b, c):
    return a * t ** 2 + b * t + c
time = np.array([0, 1, 2, 3, 4, 5])
velocity = np.array([2, 3.1, 7.9, 18.2, 34.3, 56.2])
params, _ = curve_fit(func, time, velocity)
plt.scatter(time, velocity)
plt.plot(time, func(time, *params))
plt.title('Curve fitting for velocity data')
plt.xlabel('Time (s)')
plt.ylabel('Velocity (m/s)')
plt.show()