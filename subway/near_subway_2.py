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
sql = """select * from subway_ride_quit_data order by base_ymd"""

# select 결과 dataframe으로 저장
cur.execute(sql)
rows = cur.fetchall()
db_rows_df = pd.DataFrame(rows)

# 전체 데이터 가져오기
split_df = pd.read_csv('near_subway_1.csv')
# 중복 제거
# split_df = split_df.drop_duplicates()

# 사본 복사
split_df_sp = split_df.copy()   

# 전체 branch_nm
subway_names = split_df_sp['subway_nm']

for i in range(0, len(subway_names)):

    # 컬럼의 값과 조건을 비교
    # 그 결과를 새로운 변수에 할당
    is_same_subway_nm = db_rows_df['subway_nm'] == subway_names[i]
    # 조건을 충족하는 데이터를 새로운 변수에 저장
    same_subway_nm = db_rows_df[is_same_subway_nm]

    # # db에 있는 교통량 정보 담을 dataframe 생성
    # subset_df = pd.DataFrame()

    # 맨 앞 컬럼으로 sits_id 추가
    same_subway_nm.insert(0, 'sits_id', split_df_sp['sits_id'][i])
    # sits_id 뒤에 sits_nm 컬럼 추가
    same_subway_nm.insert(1, 'sits_nm', split_df_sp['sits_nm'][i])

    if i == 0:
        # 처음일땐 새로 생성
        total_subway_df = pd.DataFrame(data=same_subway_nm)
    else:
        # 그 이후로는 추가(합치기)
        total_subway_df = pd.concat([total_subway_df, same_subway_nm])
        
    print("----------idx : ", i, "출력 완료----------")

# 중복행 제거
total_subway_df_without_duplicates = total_subway_df.drop_duplicates()

# 인덱스 초기화 (0부터 시작)
total_subway_df_without_duplicates.reset_index(drop=True, inplace=True)
total_subway_df_without_duplicates.to_csv("near_subway_data_2.csv", mode="w", header=True, index=True, na_rep='-1')

# 엑셀로 일평균값 데이터 추가하기 위해 엑셀로 저장
# total_subway_df_without_duplicates.to_excel('new_traffic_data_2.xlsx', index=True, na_rep='-1')

# 종료
conn.close()
