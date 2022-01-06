import pymysql
import pandas as pd
import time

# 전역변수 선언부
conn = None
cur = None

sql = ""

# 접속정보
conn = pymysql.connect(host='', port=, user='', password='', db='', charset='utf8')
# 커서생성
cur = conn.cursor()

sql = """select distinct branch_nm
from traffic_data_from_seoul2"""

# db에 있는 도로명 가져오기
cur.execute(sql)
rows = cur.fetchall()

# db 도로명 담을 list
db_road_list = []

for row in rows:
    # str로 변환
    str_row = str(row)
    replace_str = "',"

    # 불필요한 특수문자 제거
    for x in range(len(replace_str)):
        str_row = str_row.replace(replace_str[x], "")

    # 앞뒤 () 제거
    str_row = str_row[1:-1]
    db_road_list.append(str_row)
    

# 전체 데이터 가져오기
df = pd.read_csv('dev_near_node_road_test2_without_dup.csv')

# 사본 복사
df_sp = df.copy()

# 전체 road_name
road_names = df_sp['road_name']

# 새로운 데이터프레임 초기화
new_df = {'sits_id':['0'], 'sits_nm':['0'], 'road_nm':['0']}
new_frame = pd.DataFrame(new_df)

# 하나의 행에 해당하는 도로명들
for idx, road in enumerate(road_names):
    # 정확한 도로명 추출
    characters = "[',]"

    for x in range(len(characters)):
        road = road.replace(characters[x], "")
    road_list = road.split()

    for i in range(0,len(road_list)):
        if (any (road_list[i] in s for s in db_road_list)):
            # db_road_list에 해당 도로명 존재할 때           
            new_data = {'sits_id':df_sp['sits_id'][idx], 'sits_nm':df_sp['sits_nm'][idx], 'road_nm':road_list[i]}
            new_frame = new_frame.append(new_data, ignore_index=True)

            # 중복행 제거
            new_frame_without_duplicates = new_frame.drop_duplicates()
    
    print("---------------sits_id : ", df_sp['sits_id'][idx], "출력 완료 idx : ", idx, "---------------")
    # print(new_frame_without_duplicates)

# 초기화때 생성한 [0,0,0] 삭제
new_frame_without_duplicates = new_frame_without_duplicates.drop(0, axis=0)

new_frame_without_duplicates.to_csv('dev_near_road_split2.csv', mode="w", header=True, index=False)

# 종료
conn.close()