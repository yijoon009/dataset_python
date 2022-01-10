import pandas as pd
from pyarrow import csv

# 전체 데이터 가져오기
total_df = csv.read_csv('sorted_local.csv').to_pandas()
# 행정동 코드 가져오기
dong_cd = csv.read_csv('dong_cd.csv').to_pandas()

for i in range(len(dong_cd)):
    # start = time.time()
    dong_df = total_df[total_df['dong_cd'] == dong_cd['dong_cd'][i]]
    # dong_df.columns = ['index', 'base_ymd','time','dong_cd','total_local']
    dong_df.reset_index(drop=True, inplace=True)
    dong_df.to_csv('./local/{}_local.csv'.format(str(dong_cd['dong_cd'][i])[:-2]), mode='w', index=False, header=True)
    print('----------총: ', i, ' 개 출력 완료----------')
    # print(type(dong_df))