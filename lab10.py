import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import openpyxl
import seaborn as sb
from PIL import Image
#zadanie 1
# def f(x):
#     return 1/x
#
# x=np.linspace(1,20)
# plt.plot(x,f(x), label='f(x)=1/x')
# plt.xlabel('x')
# plt.ylabel('f(x)')
# plt.title('Wykres funkcji f(x) dla x [1,20]')
# plt.legend(loc='upper right')
# plt.show()
#zadanie 2

# def f(x):
#     return 1/x
#
# x=np.arange(1,21)
# plt.plot(x,f(x),'g>', label='f(x)=1/x',linestyle = 'dotted')
# plt.xlabel('x')
# plt.ylabel('f(x)')
# plt.xlim(xmin=0, xmax=20)
# plt.ylim(ymin=0, ymax=1)
# plt.title('Wykres funkcji f(x) dla x [1,20]')
# plt.legend(loc='upper right')
# plt.show()
#zadanie 3
# x=np.arange(0,30,0.1)
# y1=np.sin(x)
# y2=np.cos(x)
# plt.plot(x, y1, label='sin(x)')
# plt.plot(x, y2, label='cos(x)')
# plt.xlabel('x')
# plt.ylabel('cos(x) i sin(x)')
# plt.title('Wykres funkcji sin i cos w przedziale x[0,30]')
# plt.legend(loc='upper right')
# plt.show()
#zadanie 4
#kolumna1=x
#kolumna2=y
# df = pd.read_csv('iris.data', sep=',', decimal='.', header=None)
# print(df)
# x=df[0]
# y=df[1]
# print(x)
# print(y)
# d=np.abs(x-y)
# color=np.random.randint(0, 150, 150)
# plt.scatter(x, y, c=color, s=d)
# plt.xlabel('Sepal Lenght')
# plt.ylabel('Sepal Width')
# plt.show()
#zadanie 5
excel=pd.ExcelFile('imiona.xlsx')
df=pd.read_excel(excel, header=0)
plt.subplot(3,1,1)
plt.bar('Rok', 'Liczba', data=df)
plt.xticks(df['Rok'].unique(), rotation=30)
plt.tick_params(axis='x', which='major', labelsize=6)
plt.tick_params(axis='y', which='major', labelsize=6)
plt.show()