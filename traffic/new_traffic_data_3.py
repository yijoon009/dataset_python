import csv
import pandas as pd

total_df = pd.read_csv('h_new_traffic_data_2.csv', low_memory=False)

# 사본 복사
total_df_sp = total_df.copy()

hap = total_df_sp[['data_0','data_1','data_2','data_3','data_4','data_5','data_6','data_7','data_8','data_9','data_10','data_11','data_12','data_13','data_14','data_15','data_16','data_17','data_18','data_19','data_20','data_21','data_22','data_23']]
avg_new = hap.mean(axis=1)
# print(avg_new)

total_df_sp['avg_data'] = avg_new
total_df_sp.to_csv('h_new_traffic_data_4_nan.csv', mode="w", index=False, header=True)


# total_df_sp.to_csv('h_new_traffic_data_4.csv', mode="w", index=False, header=True, na_rep="-1")
# print(total_df_sp)

