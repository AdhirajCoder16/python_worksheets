import numpy as np

# Create 2D array with values 1 to 9
arr2D = np.arange(1, 10).reshape(3, 3)
print("Original 2D Array:")
print(arr2D)
result = arr2D * 5
print("\n2D Array after multiplying by 5:")
print(result)