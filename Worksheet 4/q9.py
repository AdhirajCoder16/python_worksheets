import numpy as np

# Create array
arr = np.random.randint(10, 61, size=15)
print("Original Array:", arr)
mean_val = np.mean(arr)
print("Mean:", mean_val)
median_val = np.median(arr)
print("Median:", median_val)
std_val = np.std(arr)
print("Standard Deviation:", std_val)
