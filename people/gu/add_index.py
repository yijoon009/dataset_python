import pandas as pd

# 자치구 코드 가져오기
gu_cd = pd.read_csv('gu_cd.csv')

for idx in gu_cd.index:
    df = pd.read_csv('./l_t_l/{}_l_t_l.csv'.format(gu_cd['gu_cd'][idx]))
    df.columns = ['index', 'base_ymd', 'time', 'gu_cd', 'total_local', 'total_temp', 'total_long']
    df.to_csv('./l_t_l_idx/{}_l_t_l.csv'.format(gu_cd['gu_cd'][idx]), mode='w', index=False, header=True)