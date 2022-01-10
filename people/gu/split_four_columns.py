# %% first cell
#-*- coding: euc-kr -*-
import pandas as pd
import os

# 행정동 내국인 폴더 리스트
# path_dir = 'C:\yjkim\memo\KOCCA\서울생활인구\자치구 단위(내국인)\LOCAL_PEOPLE_GU_2018'
# path_dir = 'C:\yjkim\memo\KOCCA\서울생활인구\자치구 단위(단기체류 외국인)\TEMP_FOREIGNER_GU_2018'
path_dir = 'C:\yjkim\memo\KOCCA\서울생활인구\자치구 단위(장기체류 외국인)\LONG_FOREIGNER_GU_2018'

dir_list = os.listdir(path_dir)
sortedDirList = sorted(dir_list)

# Dataframe for문
for idx, value in enumerate(sortedDirList):
    # 행정동 내국인 폴더 파일 리스트
    path_dir = 'C:\yjkim\memo\KOCCA\서울생활인구\자치구 단위(장기체류 외국인)\LONG_FOREIGNER_GU_2018\{}'.format(value)
    # 기준일ID, 시간대구분, 행정동코드, 총생활인구수 <- 앞에 네개만 가져오기
    col = [0,1,2,3]
    try:
        df = pd.read_csv(path_dir, usecols=col, header=None, low_memory=False)
    except:
        # 해당 csv 컬럼명이 한글로 되어있어서 encoding 문제 일으키는 폴더 몇몇개 있었음
        # 어차피 컬럼명은 맨처음것만 필요해서 laitn1로 인코딩하고 저장할때 컬럼명 버리고([1:]) 저장하는 방식으로 해결함
        df = pd.read_csv(path_dir, usecols=col, header=None, low_memory=False, encoding='latin1')
    # print(df)
    if idx == 0:
        df.columns = ['base_ymd', 'time', 'gu_cd', 'total_long']
        total_local = df[1:].to_csv('total_long.csv', mode='w', index=False, header=True)
    else:
        total_local = df[1:].to_csv('total_long.csv', mode='a', index=False, header=False)
    print(idx)

# %% second(2)
path_dir = 'C:\yjkim\memo\KOCCA\서울생활인구\자치구 단위(장기체류 외국인)\LONG_FOREIGNER_GU_2019.csv'
col = [0,1,2,3]
df = pd.read_csv(path_dir, usecols=col, header=None, low_memory=False)
df[1:].to_csv('total_long.csv', mode='a', index=False, header=False)
