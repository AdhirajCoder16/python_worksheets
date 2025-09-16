import numpy as np

A = np.array([[2, 1, 3],
              [0, 5, 6],
              [7, 8, 9]], dtype=float)


det_A = np.linalg.det(A)
print("Determinant of A:", det_A)

if abs(det_A) > 1e-12:
    inv_A = np.linalg.inv(A)
    print("\nInverse of A:")
    print(np.round(inv_A, 6))  
else:
    print("\nMatrix A is singular, no inverse exists.")
eigvals, eigvecs = np.linalg.eig(A)
print("\nEigenvalues of A:")
print(np.round(eigvals, 6))

print("\nEigenvectors of A (columns correspond to eigenvalues):")
print(np.round(eigvecs, 6))
