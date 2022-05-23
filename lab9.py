import numpy as np
import pandas as pd
import random

# s = pd.Series([1,3,5.5,np.nan,'a'])
# print(s)
# print('-------------------------')
s1 = pd.Series([10,12,8,14], index = ['a','b','c','d'])
# print(s1)
# print('-------------------------')
dane = {'Kraj':['Belgia','Indie','Brazylia'],
        'Stolica': ['Bruksela','New Delphi','Brasilia'],
        'Populacja': [11190846,1303171035,413123134]}
df = pd.DataFrame(dane)
# print(df)
# print('-------------------------')
# daty = pd.date_range('20220420',periods=5)
# df = pd.DataFrame(np.random.randn(5,4),index = daty,columns=list('ABCD'))
# print(df)
# print('-------------------------')
iris_df= pd.read_csv('iris.csv',header=0,sep=',',decimal=".")
# print(iris_df)
iris_df.to_csv('nowy.csv',index=False)
# print('-------------------------')
# xlsx=pd.ExcelFile('wyniki.xlsx')
# df = pd.read_excel(xlsx,header = 0)
# print(df)
# print('-------------------------')
# df.to_excel('nowy.xlsx',sheet_name='Arkusz_1',index=False)
# print('-------------------------')
# print(s1['a'])
# print(s1.a)
# print(df['Populacja'])
# print(df.Populacja)
# print('-------------------------')
# print(df.iloc[[0]])
# print('-------------------------')
# print(df.loc[[0]],['Kraj'])
# print('-------------------------')
# print(df.at[0,'Kraj'])
# print('-------------------------')
# print('Kraj:'+df.Kraj)
# print(df.sample(1))
#
# print(df.sample(frac=0.5))
#
# print('')
# print(df.sample(10,replace=True))

# print(iris_df.head())
#
# print(s1[s1>10])
# print(s1.where(s1 > 10),'Elementy nie spełnia warunków')

#
# seria = s1.copy()
# print(seria)
# print(s1[~(s1>10)])
# print(s1[(s1<13)&(s1>8)])
# print('-------------------------')
# print(df[df['Populacja']>12000000000])
# print(df[(df.Populacja > 1000000)&(df.index.isin([0,2]))])
# print('-------------------------')
# szukaj = ['Belgia', 'Brasilia']
# print(df.isin(szukaj))
# df.loc[3]='nowy_element'
# df.loc[4] = ['Polska','Warszawa',38675632]
# print(df)
# print('-------------------------')
# df.drop(3,inplace=True)
# print(df)
# print('-------------------------')
# df.drop('Kraj',axis=1,inplace = True)
# print(df)
df['Kontynent'] = ['Europa','Azja','Ameryka Południowa','Europa']
print(df)
print(df.sort_values(by='Kraj'))
grupa = df.groupby(by='Kontynent')
print(grupa.get_group('Europa'))

print(df.groupby(by='Kontynent').agg({'Populacja':['sum']}))