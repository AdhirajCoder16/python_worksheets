import pandas as pd

df = pd.read_csv('employees.csv')


avg_salary = df.groupby('Department')['Salary'].mean()
print(avg_salary)


min_max_salary = df.groupby('Department')['Salary'].agg(['min', 'max'])
print(min_max_salary)
