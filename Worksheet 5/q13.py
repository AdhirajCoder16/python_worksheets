import time
import matplotlib.pyplot as plt
sizes = [200, 400, 600, 800, 1000]
times = []
for size in sizes:
    text = 'a' * (size * 1024 * 1024)
    start = time.time()
    text = text.upper()
    end = time.time()
    times.append(end - start)
plt.plot(sizes, times)
plt.xlabel('File size (MB)')
plt.ylabel('Time (seconds)')
plt.show()