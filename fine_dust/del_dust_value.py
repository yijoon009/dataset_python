import pandas as pd

df = pd.read_csv('final_dust_data.csv', low_memory=False)
df_sp = df.copy()
df_sp.drop(['dust_value'], axis=1, inplace=True)

df_sp.to_csv('final_dust_data_wo_dust_value.csv', mode='w', index=False, header=True)

# total_df = total_df.drop(['dust_value'], axis=1, inplace=True)

# total_df.to_csv('final_dust_data.csv', mode='w', index=True, header=True, na_rep='-1')