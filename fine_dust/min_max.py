import pandas as pd

df = pd.read_csv('final_dust_data_wo_dust_value.csv', low_memory=False)

max = df.max()
print(max)

print("-------------------------------")
min = df.min(skipna=True)
print(min)