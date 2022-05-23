import sys
import pandas as pd
import numpy as np
import random
import math
import matplotlib.pyplot as plt
import seaborn as sns

#seaborn
#wykres liniowy
# sns.set(rc={'figure.figsize':(8,8)})
# sns.lineplot(x=[1,2,3,4],y=[1,4,9,16],
#               label='linia nr1',color='red',
#               marker='o', linestyle=':')
#
# sns.lineplot(x=[1,2,3,4],y=[2,5,10,17],
#              label = "linia nr2", color='green',
#              marker="^", linestyle=":")
# plt.xlabel("oś x")
# plt.ylabel("oś y")
# plt.title('Wykres liniowy')
# plt.show()

#drugi wykres
# s = pd.Series(np.random.randn(1000))
# s = s.cumsum()
# sns.set()
# wykres = sns.relplot(kind="line", data=s, label="linia")
# wykres.fig.set_size_inches(8, 6)
# wykres.fig.suptitle("Wykres liniowy losowych danych")
# wykres.set_xlabels("indeksy")
# wykres.set_ylabels("wartości")
# wykres.add_legend()
# wykres.figure.subplots_adjust(left=0.1, right=0.9 , bottom = 0.1, top = 0.9)
# plt.show()

#trzeci wykres liniowy
# sns.set()
# df = pd.read_csv('iris.csv',header = 0 , sep = ",",decimal = ".")
# print(df)
# wykres = sns.lineplot(data=df,x=df.index,y="sepal length",
#                       hue = "class",palette=['red','green','blue'])
# wykres.set_xlabel("infeksy")
# wykres.set_title("Wykres liniowy danych z Iris dataset")
# wykres.legend(title="Rodzaj kwiatu")
# plt.show()

#wykres punktowy
# sns.set()
# data = {'a': np.arange(10),
#         'c': np.random.randint(0, 10, 10),
#         'd': np.random.randn(10)}
# data['b'] = data['a'] + 10 * np.random.randn(10)
# data['d'] = np.abs(data['d']) * 100
# print(data['c'])
# print(data['d'])
# df = pd.DataFrame(data)
# plot = sns.relplot(data = df, x = "a",y = "b",
#                    hue="c", palette = "bright",size="d",legend=True)
# plot.fig.set_size_inches(6, 6)
# plot.set(xticks=data['a'])
# plt.show()

#wykres kolumnowy
# data = {'Kraj':['Belgia','Indie','Brazylia','Polska'],
#         'Stolica': ['Bruksela','New Delphi','Brasilia','Warszawa'],
#         'Kontynent': ['Europa','Azja','Ameryka Południowa','Europa'],
#         'Populacja': [11190846,1303171035,413123134,38234842]}
# df=pd.DataFrame(data)
# sns.set()
# print(df)
# plot = sns.catplot(data=df, x="Kontynent",y='Populacja',
#                    kind='bar',ci=None,hue='Kontynent',estimator=np.sum,
#                    dodge = False, palette = ['red','green','yellow'],
#                    legend_out=False)
# plot.fig.set_size_inches(7, 6)
# plot.add_legend(title="Populacja na kontynentach",loc="upper right")
# plot.fig.suptitle('Populacja na kontynentach')



# plot = sns.barplot(data=df, x= 'Kontynent', y= 'Populacja',
#                    ci=None, hue = 'Kontynent',
#                    palette= ['red','green','yellow'])
# plot.legend(title="Populacja na kontynentach")
# plot.set(title="Wykres słupkowy")
# plt.show()


#
# grupa = df.groupby("Kontynent")
# etykiety = list(grupa.groups.keys())
# wartosci = list(grupa.agg("Populacja").sum())
# plt.bar(x=etykiety ,height=wartosci, color = ["yellow",'green','red'])
# plt.xlabel('Kontynenty')
# plt.ylabel("Populacja w mdl")
# plt.show()


# Wykres liniowy
# fig = plt.figure()
# ax = fig.add_subplot(111,projection = "3d")
# print(type(ax))
# t = np.linspace(0, 2 * np.pi,100)
# z = t
# x = np.sin(t)*np.cos(t)
# y = np.tan(t)
# ax.plot(x ,y,z,label = "zadanie 1")
# ax.legend()
# plt.show()

# wykres punktowy
# np.random.seed(19680801)
# def randrange(n, vmin, vmax):
#     return(vmax - vmin)*np.random.rand(n) + vmin
#
# fig = plt.figure()
# ax = fig.add_subplot(111,projection = "3d")
# n= 100
# for c, m, zlow, zhigh in[('r','o',-50,-25),('b','^',-30,-5)]:
#     xs = randrange(n,23,32)
#     ys = randrange(n,0,100)
#     zs = randrange(n, zlow, zhigh)
#     ax.scatter(xs, ys, zs, c = c , marker=m)
# ax.set_xlabel('X label')
# ax.set_ylabel('Y label')
# ax.set_zlabel('Z label')
# ax.view_init(elev=10,azim=-35)
# plt.show()


from mpl_toolkits.mplot3d.axes3d import get_test_data
# # szerokosc 2 razy wieksza niz wysokosc
fig = plt.figure(figsize=plt.figaspect(0.5))

#pierwszy wykres

ax = fig.add_subplot(1,2,1, projection="3d")
np.random.seed(19680801)
def randrange(n, vmin, vmax):
    return (vmax - vmin)*np.random.rand(n) + vmin
n=100
for c, m, zlow, zhigh in[('r','o',-50,-25),('b','^',-30,-5)]:
    xs = randrange(n,23,32)
    ys = randrange(n,0,100)
    zs = randrange(n, zlow, zhigh)
    ax.scatter(xs, ys, zs, c = c , marker=m)
ax.set_xlabel('X label')
ax.set_ylabel('Y label')
ax.set_zlabel('Z label')
#drugi wykres

ax = fig.add_subplot(1,2,2,projection = '3d')
X, Y, Z = get_test_data()
ax.plot_wireframe(X,Y,Z, rstride=10,cstride=10)
plt.show()