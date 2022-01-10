import pandas as pd
from pyarrow import csv
import datetime

#%% first cell
# 전체데이터 가져오기
total_df = csv.read_csv('filled_empty_time_long.csv').to_pandas()
# # 컬럼명 변경
# total_df.columns = ['base_ymd', 'time', 'dong_cd', 'total_local']
total_df_sp = total_df.copy()

# 자치구코드 가져오기
# gu_cd = total_df_sp['gu_cd']
# gu_cd.drop_duplicates(inplace=True)
# gu_cd.to_csv('gu_cd.csv', mode='w', index=False, header=True)
# print(gu_cd)
gu_cd = pd.read_csv('gu_cd.csv')

tmp_df = pd.DataFrame()

dt_index = pd.date_range(start='20180101', end='20201231')

for i in range(len(gu_cd)):
    start_time = datetime.datetime.now()
    gu_df = total_df_sp[total_df_sp['gu_cd'] == gu_cd['gu_cd'][i]]
    # print(dong_df)
    for date in dt_index:
        searchDate = int(str(date)[0:10].replace('-', ''))
        # if dong_df[dong_df['base_ymd'].str.contains(searchDate)].empty:
        if gu_df.loc[gu_df['base_ymd'] == searchDate].empty:
            for time in range(24):
                new_data = {'base_ymd': searchDate, 'time': time, 'gu_cd': gu_cd['gu_cd'][i], 'total_long': -1}
                tmp_df = tmp_df.append(new_data, ignore_index=True)
                # print(tmp_df)
                # print(searchDate, dong_cd['dong_cd'][i])
    end_time = datetime.datetime.now()
    elapsed_time = end_time - start_time
    print(" 시작시간 : {0}, 종료시간 : {1}, 걸린시간 : {2}".format(start_time, end_time, elapsed_time))
    print('----------총: ', i, ' 개 출력 완료----------')

total_df_sp = pd.concat([total_df_sp, tmp_df])
total_df_sp.to_csv('filled_empty_date_long.csv', mode='w', index=False, header=True)
