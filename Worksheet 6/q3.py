import pandas as pd
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'], 'Age': [25, 30, 35, 40]}
df = pd.DataFrame(data)
print(df['Name'])

df['Country'] = ['USA', 'USA', 'USA', 'Canada']
print(df)
