import pandas as pd

df = pd.read_csv('h_new_traffic_data_4_nan.csv')

max = df.max()
print(max)

print("-------------------------------")
min = df.min(skipna=True)
print(min)