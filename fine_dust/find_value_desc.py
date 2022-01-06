import pandas as pd
import pymysql

conn = None
cur = None

sql = ""

conn = pymysql.connect(host='', port=, user='', password='', db='', charset='utf8', cursorclass=pymysql.cursors.DictCursor)
cur = conn.cursor()

sql = """select descr, alert
from dev_fine_alert_crit
where pm_cd = %s and %s between start_p and end_p"""

df = pd.read_csv('sits_sgg_nm_re.csv', low_memory=False)
df_sp = df.copy()

# pm_code, dust_value 담은 데이터프레임
# pd_cd_dust_value = df_sp[['pm_code', 'dust_value']]

# print(pd_cd_dust_value['pm_code'][0])

# 컬럼명
new_col_name = ['desc', 'alert']

# 값 설명과 경보를 담은 리스트
total_list = []

for i in range(0, len(df_sp)):
    cur.execute(sql, (df_sp['pm_code'][i], df_sp['dust_value'][i]))

    row = cur.fetchone()
    if row == None:
        total_list.append([-1, -1])
        continue
    desc_list = list(row.values())
    total_list.append(desc_list)

    print("---------------총 ", i, " 개 출력 완료---------------")

new_df = pd.DataFrame(total_list, columns=new_col_name)

total_df = pd.concat([df_sp, new_df], axis=1)

# total_df = total_df.drop(['dust_value'], axis=1, inplace=True)

total_df.to_csv('final_dust_data.csv', mode='w', index=True, header=True, na_rep='-1')

conn.close()

