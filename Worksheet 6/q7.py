import pandas as pd

df1 = pd.DataFrame({
    'Name': ['John', 'Jane', 'Emily'],
    'Department': ['Sales', 'Marketing', 'HR']
})

df2 = pd.DataFrame({
    'Name': ['John', 'Jane', 'Emily'],
    'Experience (Years)': [5, 7, 3]
})

merged_df = pd.merge(df1, df2, on='Name')
print(merged_df)
sorted_df = merged_df.sort_values(by='Experience (Years)', ascending=False)
print(sorted_df)