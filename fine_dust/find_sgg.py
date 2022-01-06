import pymysql  # pymysql 임포트
import csv
import pandas as pd

#csv 초기화
f = open('sits_sgg_nm.csv','w',newline='', encoding='utf-8')
wr = csv.writer(f)


# 전역변수 선언부
conn = None
cur = None
cur2 = None

sql=""
sql2=""

# 메인 코드
conn = pymysql.connect(host='', port=, user='', password='', db='', charset='utf8', cursorclass=pymysql.cursors.DictCursor)     # 접속정보
cur = conn.cursor()     # 커서생성
cur2 = conn.cursor()    # 커서생성

sql = "select distinct sits_id, sits_nm, sgg_cd from kt_adm_sits_adm"  # 실행할 sql문
sql2 = """select baseYmd, type, year, month, day, signguCode, signguNm, value
from dev_daily_average_of_fine_dust where signguCode= %s"""

cur.execute(sql)       # 커서로 sql문 실행

headerList = ['sits_id', 'sits_nm', 'base_ymd', 'pm_code', 'year', 'month', 'day', 'sgg_code', 'sgg_name', 'dust_value']
wr.writerow(headerList)

while True :
    row = cur.fetchone()
    if row== None :
        break
    
    cur2.execute(sql2, (row['sgg_cd']))   # 커서로 sql문 실행)
    
    while True : 
        row2 = cur2.fetchone()
        if row2==None :
            break
        value_list = list(row2.values())
        value_list.insert(0, row['sits_id'])
        value_list.insert(1, row['sits_nm'])
        # print(value_list)
        wr.writerow(value_list)

    print("---------------sits_id : ", row['sits_id'], "출력 완료---------------")

f.close()


















