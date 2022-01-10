import pandas as pd

df = pd.read_csv('./l_t_l_idx/11110515_l_t_l.csv')

max = df.max()
print(max)
print("-------------------------------")
min = df.min(skipna=True)
print(min)
