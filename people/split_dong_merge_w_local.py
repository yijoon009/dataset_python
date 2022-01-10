import pandas as pd
from pyarrow import csv
import os

# 전체 데이터 가져오기
total_df = csv.read_csv('sorted_long.csv').to_pandas()
# 행정동 코드 가져오기
dong_cd = csv.read_csv('dong_cd.csv').to_pandas()

for i in range(len(dong_cd)):
    # start = time.time()
    # 같은 행정동만 묶여있는 데이터프레임
    dong_df = total_df[total_df['dong_cd'] == dong_cd['dong_cd'][i]]
    # dong_df.columns = ['index', 'base_ymd','time','dong_cd','total_local']
    # dong_df.reset_index(drop=True, inplace=True)

    # 행정동 코드
    hjd_cd = str(dong_cd['dong_cd'][i])[:-2]

    # 기존에 있던 행정동별 내국인 파일
    # file = './local/{}_local.csv'.format(hjd_cd)

    # 기존에 내국인, 단기 합친 파일
    file = './l_t/{}_l_t.csv'.format(hjd_cd)

    # 해당하는 파일이 있는지 확인
    if os.path.exists(file):
        # print("존재")
        local_df = csv.read_csv(file).to_pandas()
        # print(local_df)
        # print(dong_df)
        local_df2 = pd.merge(local_df, dong_df)
        local_df2.to_csv('./l_t_lon/{}_l_t_l.csv'.format(hjd_cd), mode='w', index=True, header=True)
        # print(local_df2)

    # dong_df.to_csv('./local/{}_local.csv'.format(str(dong_cd['dong_cd'][i])[:-2]), mode='w', index=True, header=True)
    print('----------총: ', i, ' 개 출력 완료----------')
    # print(type(dong_df))