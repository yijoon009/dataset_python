# %% first cell
#-*- coding: euc-kr -*-
import pandas as pd
import os

# ������ ������ ���� ����Ʈ
# path_dir = 'C:\yjkim\memo\KOCCA\�����Ȱ�α�\��ġ�� ����(������)\LOCAL_PEOPLE_GU_2018'
# path_dir = 'C:\yjkim\memo\KOCCA\�����Ȱ�α�\��ġ�� ����(�ܱ�ü�� �ܱ���)\TEMP_FOREIGNER_GU_2018'
path_dir = 'C:\yjkim\memo\KOCCA\�����Ȱ�α�\��ġ�� ����(���ü�� �ܱ���)\LONG_FOREIGNER_GU_2018'

dir_list = os.listdir(path_dir)
sortedDirList = sorted(dir_list)

# Dataframe for��
for idx, value in enumerate(sortedDirList):
    # ������ ������ ���� ���� ����Ʈ
    path_dir = 'C:\yjkim\memo\KOCCA\�����Ȱ�α�\��ġ�� ����(���ü�� �ܱ���)\LONG_FOREIGNER_GU_2018\{}'.format(value)
    # ������ID, �ð��뱸��, �������ڵ�, �ѻ�Ȱ�α��� <- �տ� �װ��� ��������
    col = [0,1,2,3]
    try:
        df = pd.read_csv(path_dir, usecols=col, header=None, low_memory=False)
    except:
        # �ش� csv �÷����� �ѱ۷� �Ǿ��־ encoding ���� ����Ű�� ���� �� �־���
        # ������ �÷����� ��ó���͸� �ʿ��ؼ� laitn1�� ���ڵ��ϰ� �����Ҷ� �÷��� ������([1:]) �����ϴ� ������� �ذ���
        df = pd.read_csv(path_dir, usecols=col, header=None, low_memory=False, encoding='latin1')
    # print(df)
    if idx == 0:
        df.columns = ['base_ymd', 'time', 'gu_cd', 'total_long']
        total_local = df[1:].to_csv('total_long.csv', mode='w', index=False, header=True)
    else:
        total_local = df[1:].to_csv('total_long.csv', mode='a', index=False, header=False)
    print(idx)

# %% second(2)
path_dir = 'C:\yjkim\memo\KOCCA\�����Ȱ�α�\��ġ�� ����(���ü�� �ܱ���)\LONG_FOREIGNER_GU_2019.csv'
col = [0,1,2,3]
df = pd.read_csv(path_dir, usecols=col, header=None, low_memory=False)
df[1:].to_csv('total_long.csv', mode='a', index=False, header=False)
