import pandas as pd
import openpyxl

df = pd.read_excel('traffic_data_without_avg_data.xlsx')

# -1 작업 후 에러부분 '-1'로 변경
# df.to_excel('hello_fin.xlsx', index=False, na_rep='-1')
df.to_csv('final_traffic_data.csv', mode="w", header=True, index=False, na_rep='-1')