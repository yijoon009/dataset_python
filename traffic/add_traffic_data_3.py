import pandas as pd
import pymysql
import openpyxl

# 전역변수 선언부
conn = None
cur = None

sql=""

# 메인 코드
conn = pymysql.connect(host='', port=, user='', password='', db='', charset='utf8', cursorclass=pymysql.cursors.DictCursor)
cur = conn.cursor()

# db 정보 가져오기
sql = """select year, month, day, baseYmd, branch_nm, direction, classify, data_0, data_1, data_2, data_3, data_4, data_5, data_6, data_7, data_8, data_9, data_10, data_11, data_12, data_13, data_14, data_15, data_16, data_17, data_18, data_19, data_20, data_21, data_22, data_23
from traffic_data_from_seoul2"""

# select 결과 dataframe으로 저장
cur.execute(sql)
rows = cur.fetchall()
db_rows_df = pd.DataFrame(rows)


    
# 전체 데이터 가져오기
split_df = pd.read_csv('dev_near_road_split2.csv')

# test
# split_df = {'sits_id': ['110', '110', '112', '112', '114'],
#         'sits_nm': ['서울숲', '서울숲', '경복궁', '경복궁', '우리집'],
#         'road_nm': ['백제고분로', '종합운동장', '백제고분로', '종합운동장', '성산로']}
# new_split_df = pd.DataFrame(split_df)

# 사본 복사
split_df_sp = split_df.copy()   

# 전체 road_name
road_names = split_df_sp['road_nm']

for i in range(0, len(road_names)):
    # db에 있는 교통량 정보 담을 dataframe 생성
    subset_df = pd.DataFrame()

    #도로명이 포함되는 컬럼 뽑아오기
    contains_road_nm = db_rows_df['branch_nm'].str.contains(road_names[i])
    # 도로에 해당하는 교통량 정보 dataframe
    subset_df = db_rows_df[contains_road_nm]
    # 맨 앞 컬럼으로 sits_id 추가
    subset_df.insert(0, 'sits_id', split_df_sp['sits_id'][i])
    # sits_id 뒤에 sits_nm 컬럼 추가
    subset_df.insert(1, 'sits_nm', split_df_sp['sits_nm'][i])

    if i == 0:
        # 처음일땐 새로 생성
        final_traffic_df = pd.DataFrame(data=subset_df)
    else:
        # 그 이후로는 추가(합치기)
        final_traffic_df = pd.concat([final_traffic_df, subset_df])

# 중복행 제거
final_traffic_df_without_duplicates = final_traffic_df.drop_duplicates()

# 인덱스 초기화 (0부터 시작)
final_traffic_df_without_duplicates.reset_index(drop=True, inplace=True)
# final_traffic_df_without_duplicates.to_csv("final_traffic_data.csv", mode="w", header=True, index=True, na_rep='-1')

# 엑셀로 일평균값 데이터 추가하기 위해 엑셀로 저장
final_traffic_df_without_duplicates.to_excel('traffic_data_without_avg_data.xlsx', index=True, na_rep='-1')

# 종료
conn.close()
