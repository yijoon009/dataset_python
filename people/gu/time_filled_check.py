from pyarrow import csv
import pandas as pd

df = csv.read_csv('filled_empty_time_long.csv').to_pandas()
# df.columns = ['base_ymd', 'time', 'dong_cd', 'total_local']

cnt_df = df.groupby(['base_ymd', 'gu_cd'])
total_count = pd.DataFrame(cnt_df.size())
total_count.to_csv('to_check.csv', mode='w', header=True)

cnt_df = pd.read_csv('to_check.csv')
cnt_df.columns = ['base_ymd', 'gu_cd', 'cnt']

df_not24 = cnt_df.loc[cnt_df['cnt'] != 24]
print(df_not24)