import pandas as pd
from pyarrow import csv
import time

# 전체데이터 가져오기
total_df = csv.read_csv('total_long.csv').to_pandas()
# 컬럼명 변경
total_df.columns = ['base_ymd', 'time', 'dong_cd', 'total_long']
total_df_sp = total_df.copy()

# 기준일, 행정동코드별로 몇개있는지 확인
cnt_df = total_df.groupby(['base_ymd', 'dong_cd'])
total_count = pd.DataFrame(cnt_df.size())
total_count.to_csv('find_empty_time_long.csv', mode='w', header=True)

cnt_df = pd.read_csv('find_empty_time_long.csv')
cnt_df.columns = ['base_ymd', 'dong_cd', 'cnt']

# 24개(24시간)가 아닌것만 가져오기
df_not24 = cnt_df.loc[cnt_df['cnt'] != 24]
# print(df_not24)

count = 0
for idx, row in df_not24.iterrows():
    # 시간이 빈 해당 행정동만 뽑아오기
    condition1 = total_df_sp.dong_cd == row.dong_cd
    df_check = total_df_sp.loc[condition1]
    # print(df_check)
    start = time.time()
    for i in range(0, 24):
        # 0시 ~ 23시까지 있는지 확인
        condition2 = (df_check.base_ymd == row.base_ymd) & (df_check.time == i)
        if df_check.loc[condition2].empty:
            # 해당 시간이 없을때 전체데이터에 추가(나중에 sort)
            new_data = {'base_ymd': row.base_ymd, 'time': i, 'dong_cd': row.dong_cd, 'total_long': -1}
            # print(new_data)
            total_df_sp = total_df_sp.append(new_data, ignore_index=True)
    count+=1
    print('----------총: ', count, ' 개 출력 완료----------')
    end = time.time()
    print('경과 시간: ',end-start,'초')
total_df_sp.to_csv('filled_empty_time_long.csv', mode='w', index=False, header=True)


# df_check = total_df_sp.loc[:, ['base_ymd', 'time', 'dong_cd']]

# for idx, row in df_not24.iterrows():
#     start = time.time()
#     for i in range(0, 24):
#         condition = (df_check.base_ymd == row.base_ymd) & (df_check.dong_cd == row.dong_cd) & (df_check.time == i)
#         if df_check.loc[condition].empty:
#             new_data = {'base_ymd': row.base_ymd, 'time': i, 'dong_cd': row.dong_cd, 'total_local': -1}
#             total_df_sp = total_df_sp.append(new_data, ignore_index=True)
#             # print(row.base_ymd, row.dong_cd, i)
#     print('----------idx: ', idx, ' 출력 완료----------')
#     end = time.time()
#     print('경과 시간: ',end-start,'초')
# total_df_sp.to_csv('filled_empty_time_temp.csv', mode='w', index=False, header=True)
