import pandas as pd
from pyarrow import csv

# df = csv.read_csv('filled_empty_date_local.csv').to_pandas()
df = csv.read_csv('filled_empty_date_temp.csv').to_pandas()
df_sp = df.copy()

print(df_sp)
print("========================")
df_sp.sort_values(by=['base_ymd', 'time'], axis=0, inplace=True)
print(df_sp)
df_sp.to_csv('sorted_temp.csv', mode='w', index=False, header=True)
