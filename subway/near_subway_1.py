import pymysql
import pandas as pd
import csv

#csv 초기화
f = open('near_subway_1.csv','w',newline='', encoding='utf-8')
wr = csv.writer(f)

conn = None
cur = None
cur2 = None

sql = ""
sql2 = ""

# 접속 정보
conn = pymysql.connect(host='', port=, user='', password='', db='', charset='utf8', cursorclass=pymysql.cursors.DictCursor)
# 커서 생성
cur = conn.cursor()
cur2 = conn.cursor()


sql = "select distinct sits_id, sits_nm, origin_xcrd, origin_ycrd from kt_adm_sits_adm"
sql2 = """select distinct kasa.sits_id, kasa.sits_nm, a.name
            from (
                    SELECT
                           (6371*acos(cos(radians(%s))*cos(radians(subway.origin_ycrd))*cos(radians(subway.origin_xcrd)
                           -radians(%s))+sin(radians(%s))*sin(radians(subway.origin_ycrd)))) AS distance, subway.name
                    FROM dev_station_coordinate subway
                    HAVING distance <= 1
                    ORDER BY distance
                ) a
            inner join kt_adm_sits_adm kasa
            where kasa.sits_id = %s"""

cur.execute(sql)

headerList = ['sits_id', 'sits_nm', 'subway_nm']
wr.writerow(headerList)

while True :
    row = cur.fetchone()
    if row== None :
        break

    cur2.execute(sql2, (row['origin_ycrd'], row['origin_xcrd'], row['origin_ycrd'], row['sits_id']))   # 커서로 sql문 실행
    while True : 
        row2 = cur2.fetchone()
        if row2==None :
            break
        value_list = list(row2.values())
        # print(value_list)
        wr.writerow(value_list)

    print("---------------sits_id : ", row['sits_id'], "출력 완료---------------")

f.close()





