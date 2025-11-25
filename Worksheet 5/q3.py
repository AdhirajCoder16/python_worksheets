import numpy as np
from scipy import linalg

a = np.array([[1, 2], [3, 4]])
det = linalg.det(a)
inv = linalg.inv(a)
eig = linalg.eigvals(a)
print(det)
print(inv)
print(eig)