import pandas as pd


df = pd.read_csv('employees.csv')
print(df)


filtered_df = df[df['Salary'] > 55000]
print(filtered_df[['Name', 'Department']])
