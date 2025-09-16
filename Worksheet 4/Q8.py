import numpy as np

A = np.array([[1, 2],
              [3, 4]])

B = np.array([[5, 6],
              [7, 8]])

print("Matrix A:\n", A)
print("Matrix B:\n", B)
matmul = np.dot(A, B)   
print("\nMatrix Multiplication (A x B):\n", matmul)
transpose_A = A.T
print("\nTranspose of Matrix A:\n", transpose_A)
