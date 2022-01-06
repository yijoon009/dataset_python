import pandas as pd

df = pd.read_csv('sits_sgg_nm.csv')
print(df.columns)
df.drop(['sgg_code'], axis=1)
df = df[['sits_id', 'sits_nm', 'sgg_name', 'base_ymd', 'year', 'month', 'day', 'pm_code', 'dust_value']]
df.to_csv('sits_sgg_nm_re.csv', mode='w', index=False, header=True)