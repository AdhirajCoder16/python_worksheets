import numpy as np

arr = np.random.randint(20, 41, size=10)
print("Original Array:", arr)
greater_than_30 = arr[arr > 30]
print("Elements greater than 30:", greater_than_30)
