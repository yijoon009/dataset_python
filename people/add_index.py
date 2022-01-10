import pandas as pd

# 행정동 코드 가져오기
dong_cd = pd.read_csv('dong_cd.csv')
# print(dong_cd)

for idx in dong_cd.index:
    single_dong_cd = str(dong_cd['dong_cd'][idx])[:-2]
    df = pd.read_csv('./l_t_lon/{}_l_t_l.csv'.format(single_dong_cd))
    df.columns = ['index', 'base_ymd', 'time', 'dong_cd', 'total_local', 'total_temp', 'total_long']
    df.to_csv('./l_t_l_idx/{}_l_t_l.csv'.format(single_dong_cd), mode='w', index=False, header=True)