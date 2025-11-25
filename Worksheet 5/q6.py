import numpy as np
sales = np.random.randint(50, 200, (12, 4))
total_sales = np.sum(sales)
avg_sales = np.mean(sales)
max_sales = np.max(sales)
best_month = np.argmax(np.sum(sales, axis=1)) + 1
worst_month = np.argmin(np.sum(sales, axis=1)) + 1
print(total_sales)
print(avg_sales)
print(max_sales)
print(best_month)
print(worst_month)