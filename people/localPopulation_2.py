import pandas as pd
import datetime
from pyarrow import csv
import os

# 집계구 코드 csv 파일 읽기
smguCd = pd.read_csv('/Users/choejiyeon/Documents/project/KOCCA/python/population/집계구코드.csv')
localFileName = pd.read_csv('/Users/choejiyeon/Documents/project/KOCCA/python/population/집계구내국인파일명.csv')

for key, smguCode in smguCd.iterrows():
    smgu_cd = smguCode.values[0]  # 집계구 코드

    smgu_local_list = pd.DataFrame()  # 집계구별 데이터 담는 Df
    for key, fileName in localFileName.iterrows():
        start_time = datetime.datetime.now()

        start_time1 = datetime.datetime.now()
        filepath = fileName.values[0]

        # # include_columns : 읽을 컬럼명만 지정
        convert_opts = csv.ConvertOptions(include_columns=['f0', 'f1', 'f2', 'f3', 'f4'])

        # localDf = csv.read_csv('/Users/choejiyeon/Documents/project/KOCCA/99.기타/Data/kocca_데이터_수집_파일/서울생활인구/집계구 단위(내국인)/{0}/{1}'.format(filepath[:19], filepath), csv.ParseOptions(ignore_empty_lines=False)).to_pandas()
        localDf = csv.read_csv(
            '/Users/choejiyeon/Documents/project/KOCCA/99.기타/Data/kocca_데이터_수집_파일/서울생활인구/집계구 단위(내국인)/{0}/{1}'.format(filepath[:19], filepath),
            read_options=csv.ReadOptions(
                autogenerate_column_names=True,
                skip_rows=1),
            convert_options=convert_opts).to_pandas()
        # localDf = localDf[['기준일ID', '시간대구분', '행정동코드', '집계구코드', '총생활인구수']]
        # print(localDf)
        end_time1 = datetime.datetime.now()
        elapsed_time1 = end_time1 - start_time1
        print("1 : ", elapsed_time1)
        # 집계구 내국인 데이터에서 특정 값(집계구코드)을 가진 행 찾기
        start_time2 = datetime.datetime.now()
        local_row = localDf.loc[localDf['f3'] == smgu_cd]
        end_time2 = datetime.datetime.now()
        elapsed_time2 = end_time2 - start_time2
        print("2 : ", elapsed_time2)
        # 시간대구분 기반으로 정렬하기
        local_row = local_row.sort_values(by=['f1'])

        end_time = datetime.datetime.now()
        elapsed_time = end_time - start_time

        smgu_local_list = pd.concat([smgu_local_list, local_row])

        print(str(key) + " 시작시간 : {0}, 종료시간 : {1}, 걸린시간 : {2}".format(start_time, end_time, elapsed_time))
        print(smgu_local_list)
        print('-------------------------{0} - {1}완료 ---------------'.format(smgu_cd, filepath))

        del localDf
    smgu_local_list.columns = ['STDR_DE_ID', 'TMZON_PD_SE', 'ADSTRD_CODE_SE', 'SMGU_CD', 'NATIVE_TOT']
    # smgu_local_list.rename(columns={'f0': 'STDR_DE_ID', 'f1': 'TMZON_PD_SE', 'f2': 'ADSTRD_CODE_SE', 'f3': 'SMGU_CD', 'f4': 'NATIVE_TOT'})
    smgu_local_list.to_csv(
        '/Users/choejiyeon/Documents/project/KOCCA/96.DB/부가데이터/서울생활인구/집계구/내국인/{0}_집계구_내국인.csv'.format(
            smgu_cd), mode="w", header=True, index=False)  # 데이터프레임 csv 파일로 저장
    del smgu_local_list  # 데이터프레임 초기화
