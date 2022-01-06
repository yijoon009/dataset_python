import pymysql  # pymysql 임포트
import csv
import pandas as pd
import time

#csv 초기화
f = open('dev_near_node2.csv','w',newline='', encoding='utf-8')
wr = csv.writer(f)

# 전역변수 선언부
conn = None
cur = None
cur2 = None
cur3 = None

sql=""
sql2=""
sql3=""

# 메인 코드
conn = pymysql.connect(host='', port=, user='', password='', db='', charset='utf8')     # 접속정보
cur = conn.cursor()     # 커서생성
cur2 = conn.cursor()    # 커서생성
cur3 = conn.cursor()    # 커서생성

sql = "select distinct sits_id, origin_xcrd, origin_ycrd from kt_adm_sits_adm"  # 실행할 sql문
sql2 = """select distinct kasa.sits_id, kasa.sits_nm, a.node_id
            from (
                    select
                        (3956 * 2 * ASIN(SQRT(POWER(SIN((%s - node.lon) * pi()/180 / 2), 2) +
                        COS(%s * pi()/180) *  COS(node.lon * pi()/180) *
                        POWER(SIN((%s - node.lat) * pi()/180 / 2), 2))) * 1609.344 ) AS distance,
                        node.node_id
                    FROM  dev_node_x_y node
                ) a
            inner join kt_adm_sits_adm kasa
            where
                kasa.sits_id  = %s
                and a.distance <= 1000"""
sql3 = """select distinct road_name
        from dev_link_x_y
        where
            %s between f_node and t_node"""


result = cur.execute(sql)       # 커서로 sql문 실행

headerList = ['sits_id', 'sits_nm', 'node_id']
wr.writerow(headerList)

while (True) :  # 반복실행
    # start = time.time()
    row = cur.fetchone()        # row에 커서(테이블 셀렉트)를 한줄 입력하고 다음줄로 넘어감
    if row== None :     # 커서(테이블 셀렉트)에 더이상 값이 없으면
        break   # while문을 빠져나감

    nodeResult = cur2.execute(sql2, (row[1], row[1], row[2], row[0]))   # 커서로 sql문 실행
    while (True) : 
        row2 = cur2.fetchone()
        if row2==None :
            break
        nodeArr = []
        for item in row2:
            nodeArr.append(item)
        wr.writerow(nodeArr)

    print("---------------sits_id : ", row[0], "출력 완료---------------")
    # end = time.time()
    # print("경과: ", end - start, "sec")

f.close()

# node_id 추출 후 해당 road_name 조회
df = pd.read_csv('dev_near_node2.csv')
df_sp = df.copy()

df_node_id = df_sp["node_id"]

roads_arr = [[] for i in range(len(df_node_id))]
df_sp['road_name'] = roads_arr

for idx, nodeId in enumerate(df_node_id):
    road_names = cur3.execute(sql3, nodeId)
    row = cur3.fetchall()
    road_names_arr = []
    for road in row:
        road_names_arr.append(road[0])
    
    # roads_arr[idx] = road_names_arr
    print("---------------node_id : ", nodeId, "출력 완료--------------- idx : {0}".format(idx))
    df_sp['road_name'][idx] = road_names_arr
    
df_sp_without_duplicates = df_sp.drop_duplicates()
df_sp_without_duplicates.to_csv('dev_near_node_road_test2_without_dup.csv', mode="w", header=True, index=False)


conn.close()    # 종료

