import pandas as pd
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'], 'Age': [25, 30, 35, 40]}
df = pd.DataFrame(data)
filtered_df = df[df['Age'] > 30]
print(filtered_df)
df.set_index('Name', inplace=True)
print(df)