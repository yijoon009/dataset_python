import pandas as pd
from pyarrow import csv
import os

# 전체 데이터 가져오기
total_df = csv.read_csv('sorted_long.csv').to_pandas()
# 자치구 코드 가져오기
gu_cd = csv.read_csv('gu_cd.csv').to_pandas()

for i in range(len(gu_cd)):
    # start = time.time()
    # 같은 자치구만 묶여있는 데이터프레임
    gu_df = total_df[total_df['gu_cd'] == gu_cd['gu_cd'][i]]
    # print(gu_df)
    # dong_df.columns = ['index', 'base_ymd','time','dong_cd','total_local']
    # dong_df.reset_index(drop=True, inplace=True)

    # 단일 자치구 코드
    single_gu_cd = gu_cd['gu_cd'][i]
    # print(single_gu_cd)
    # 기존에 있던 자치구별 내국인 파일
    # file = './local/{}_local.csv'.format(single_gu_cd)
    file = './l_t/{}_l_t.csv'.format(single_gu_cd)

    # 기존에 내국인, 단기 합친 파일
    # file = './l_t/{}_l_t.csv'.format(hjd_cd)

    # 해당하는 파일이 있는지 확인
    if os.path.exists(file):
        local_df = csv.read_csv(file).to_pandas()
        local_df2 = pd.merge(local_df, gu_df)
        # local_df2.to_csv('./l_t_lon/{}_l_t_l.csv'.format(hjd_cd), mode='w', index=True, header=True)
        local_df2.to_csv('./l_t_l/{}_l_t_l.csv'.format(single_gu_cd), mode='w', index=False, header=True)
        # print(local_df2)
    else:
        print("존재하지 않음")
    # dong_df.to_csv('./local/{}_local.csv'.format(str(dong_cd['dong_cd'][i])[:-2]), mode='w', index=True, header=True)
    print('----------총: ', i, '개 출력 완료----------')
    # print(type(dong_df))