import pandas as pd

df = pd.read_csv('total_local.csv', low_memory=False)
print(df.isnull().sum())
df.dropna(inplace=True)
print(df.isnull().sum())
df.to_csv('total_local_wo_nan.csv', mode='w', index=False, header=True)