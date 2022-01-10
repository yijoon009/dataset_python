import pandas as pd
from pyarrow import csv
import time

# 전체데이터 가져오기
total_df = csv.read_csv('total_local_wo_nan.csv').to_pandas()
# 컬럼명 변경
total_df.columns = ['base_ymd', 'time', 'dong_cd', 'total_local']
total_df_sp = total_df.copy()

# 행정동 코드 가져오기
dong_df = total_df_sp['dong_cd']
dong_df = dong_df.drop_duplicates(inplace=False)
# print(dong_df)
dt_idx = pd.date_range(start='20191015', end='20191027')

tmp_df = pd.DataFrame()

count = 0
# 행정동 하나마다
for dong in dong_df:
    start = time.time()
    # 날짜 추가
    for date in dt_idx:
        date = str(date)[0:10].replace('-', '')
        # 각 시간도
        for i in range(24):
            new_data = {'base_ymd': date, 'time': i, 'dong_cd': dong, 'total_local': -1}
            tmp_df = tmp_df.append(new_data, ignore_index=True)
    # print(tmp_df)
    count += 1
    print('----------총: ', count, ' 개 출력 완료----------')
    end = time.time()
    print('경과 시간: ', end - start, '초')
# print(tmp_df)
total_df_sp = pd.concat([total_df_sp, tmp_df])
total_df_sp.to_csv('filled_empty_date_local.csv', mode='w', index=False, header=True)
