import pandas as pd
import os

subway_xy = pd.read_csv('C:\yjkim\workspace\kocca_dataset\subway\station_x_y_8.csv')
subway_line = pd.read_csv('C:\yjkim\workspace\kocca_dataset\subway\station_line_8.csv')

# 사본 복사
subway_xy_sp = subway_xy.copy()
subway_line_sp = subway_line.copy()

# 호선 담을 list
line_ls = []

for i in range(len(subway_xy_sp)): 
    # 한 행의 '역이름' 가져오기
    cur_subway = subway_xy_sp.iloc[i]['역이름']
    # 역 이름과 동일한 행에서 '전철역명' 가져오기
    matched_line = subway_line_sp.loc[subway_line_sp['전철역명'] == cur_subway]
    
    if len(matched_line) > 0 : 
        # 호선이 있을때
        line_ls.append(list(matched_line['호선']))
        
    else:
        # 호선이 없을때 
        line_ls.append(None)

# 호선 정보 부여
subway_xy_sp['호선'] = line_ls
# 수도권 지하철역 좌표는 노선 정보가 안들어갔으므로 제거 
subway_xy_sp.dropna(subset=['호선'], inplace=True, axis=0)
subway_xy_sp.columns = ['station_nm', 'y', 'x', 'line']

subway_xy_sp.to_csv('subway_xy_line_data.csv', mode='w', index=False, header=True)
