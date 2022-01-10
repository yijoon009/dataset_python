import pandas as pd
from pyarrow import csv
import time

# 전체데이터 가져오기
total_df = csv.read_csv('filled_empty_time_temp.csv').to_pandas()
# # 컬럼명 변경
# total_df.columns = ['base_ymd', 'time', 'dong_cd', 'total_local']
total_df_sp = total_df.copy()

# 행정동코드 가져오기
dong_cd = pd.read_csv('dong_cd.csv')

tmp_df = pd.DataFrame()

dt_index = pd.date_range(start='20180101', end='20201231')

for i in range(len(dong_cd)):
    start = time.time()
    dong_df = total_df_sp[total_df_sp['dong_cd'] == dong_cd['dong_cd'][i]]
    # print(dong_df)
    for date in dt_index:
        searchDate = int(str(date)[0:10].replace('-', ''))
        # if dong_df[dong_df['base_ymd'].str.contains(searchDate)].empty:
        if dong_df.loc[dong_df['base_ymd'] == searchDate].empty:
            for time in range(24):
                new_data = {'base_ymd': date, 'time': time, 'dong_cd': dong_cd['dong_cd'][i], 'total_temp': -1}
                tmp_df = tmp_df.append(new_data, ignore_index=True)
                # print(tmp_df)
                # print(searchDate, dong_cd['dong_cd'][i])
    print('----------총: ', i, ' 개 출력 완료----------')
    end = time.time()
    print('경과 시간: ', end - start, '초')

total_df_sp = pd.concat([total_df_sp, tmp_df])
total_df_sp.to_csv('filled_empty_date_temp.csv', mode='w', index=False, header=True)
