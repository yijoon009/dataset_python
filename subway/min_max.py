import pandas as pd

df = pd.read_csv('near_subway1.csv')

max = df.max()
print(max)


print("-------------------------------")
min = df.min(skipna=True)
print(min)

 

#%% second
import os
print(os.curdir)