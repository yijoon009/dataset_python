import pandas as pd
from pyarrow import csv

# 전체 데이터 가져오기
total_df = csv.read_csv('sorted_local.csv').to_pandas()
# 자치구 코드 가져오기
gu_cd = csv.read_csv('gu_cd.csv').to_pandas()

for i in range(len(gu_cd)):
    # start = time.time()
    gu_df = total_df[total_df['gu_cd'] == gu_cd['gu_cd'][i]]
    # dong_df.columns = ['index', 'base_ymd','time','dong_cd','total_local']
    gu_df.reset_index(drop=True, inplace=True)
    gu_df.to_csv('./local/{}_local.csv'.format(gu_cd['gu_cd'][i]), mode='w', index=False, header=True)
    print('----------총: ', i, ' 개 출력 완료----------')
    # print(type(dong_df))