#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
from pandas import DataFrame

path='./2019_kbo_for_kaggle_v2.csv'
df=pd.read_csv(path)
for year in range(2015,2019):
    s_df=df[df['year']==year]

    H_10=s_df.sort_values(by='H', ascending=False).head(10)
    avg_10=s_df.sort_values(by='avg', ascending=False).head(10)
    HR_10=s_df.sort_values(by='HR', ascending=False).head(10)
    OBP_10=s_df.sort_values(by='OBP', ascending=False).head(10)

    print(year,' 안타 상위 10: ',H_10[['batter_name','H','year']].to_string(index=False),"\n")
    print(year,' 타율 상위 10: ',avg_10[['batter_name','avg','year']].to_string(index=False),"\n")
    print(year,' 홈런 상위 10: ',HR_10[['batter_name','HR','year']].to_string(index=False),"\n")
    print(year,' 출루율 상위 10: ',OBP_10[['batter_name','OBP','year']].to_string(index=False),"\n")

second_df=df[df['year']==2018]    
max_war=second_df.loc[second_df.groupby('cp')['war'].idxmax()]

print(year,' 포지션 당 최고 승리 기여도: ',max_war[['batter_name','war','cp','year']].to_string(index=False),"\n")

corr_df=df[['R','H','HR','RBI','SB','war','avg','OBP','SLG','salary']]
correlation=corr_df.corr();
salary_corr=correlation['salary']
salary_corr=salary_corr.drop('salary',axis=0)
salary_df=pd.DataFrame(salary_corr)
max_corr=salary_df.idxmax();

print('연봉과의 관계:\n',salary_df.to_string(header=False),"\n")
print('highest correlation with salary: ',max_corr['salary'])


# In[ ]:




