import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def model(y, t):
    theta, omega = y
    dtheta = omega
    domega = -0.2 * omega - 9.81 * np.sin(theta)
    return [dtheta, domega]
t = np.linspace(0, 20, 200)
y0 = [1, 0]
solution = odeint(model, y0, t)
plt.plot(t, solution[:, 0])
plt.xlabel('Time (s)')
plt.ylabel('Displacement (rad)')
plt.show()
max_disp = np.max(solution[:, 0])
time_max = t[np.argmax(solution[:, 0])]
print(max_disp, time_max)