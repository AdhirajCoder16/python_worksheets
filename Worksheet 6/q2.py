import pandas as pd
S1 = pd.Series([100, 200, 300, 400, 500])
print(S1)

print(S1.iloc[1])
print(S1.iloc[3])

S2 = pd.Series([10, 20, 30, 40, 50])
print(S1 + S2)