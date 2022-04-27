import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ts = pd.Series(np.random.randn(1000))
# ts = ts.cumsum()
#
# ts.plot()
# plt.show()

# dane = {'Kraj':['Belgia','Indie','Brazylia','Polska'],
#         'Stolica': ['Bruksela','New Delphi','Brasilia','Warszawa'],
#         'Populacja': [11190846,1303171035,413123134,38234842],
#         'Kontynent': ['Europa','Azja','Ameryka Południowa','Europa']}
# df = pd.DataFrame(dane)
# grupa = df.groupby('Kontynent').agg({'Populacja':['sum']})
# print(grupa)
# grupa.plot(kind="bar",xlabel="Kontynent",ylabel="Populacjaw mld",rot = 0,title = "Populacja kontynentów")
# wykres = grupa.plot.bar() #Czysty wykres
# wykres.set_xlabel('Kontynent')
# wykres.set_ylabel('Populacja w mld')
# wykres.tick_params(axis='x',labelrotation = 0)
# wykres.legend(loc = 'center')
# wykres.set_title('Populacja na kontynentach')
# # plt.savefig('wykres.png') #Zapis wykresu do pliku
# plt.show()

# df = pd.read_csv('dane.csv',header=0,sep=";",decimal=".")
# print(df)
# grupa = df.groupby('Imię i nazwisko').agg({'Wartość zamówienia':['sum']})
# grupa.plot(kind='pie',subplots = True, autopct='%.2f %%',fontsize=10,figsize=(5,5),colors=['darkgreen','purple'])
# plt.legend(loc='upper left')
# plt.show()

# df = pd.DataFrame(ts)
# print(df)
# df['Średnia krocząca'] = df.rolling(window=50).mean() #Średnia krocząca :)
# df.plot()
# plt.legend(['Wartości','Średnia z n-elementów'])
# plt.show()


#----------------------------------------------------------------------------------------------------
# Zadania 1-3
# xlsx = pd.ExcelFile('imiona.xlsx')
# df=pd.read_excel(xlsx,header = 0)


# Zad1
# grupa = df.groupby('Rok').agg({"Liczba":['sum']})
# print(grupa)
# grupa.plot(xlabel="Rok",ylabel="Urodzone dzieci",rot=0,title="Urodzone dzieci dla każdego roku",)
# plt.show()
# Zad2
# grupa = df.groupby('Plec').agg({'Liczba':['sum']})
# print(grupa)
# grupa.plot(kind="bar",xlabel="płeć",ylabel="liczba",rot=0,title="Liczba urodzonych dzieci")
# plt.legend(loc='center')
# plt.show()
# Zad3

# sort = df[df['Rok']>=2012]
# grupa = sort.groupby('Plec').agg({'Liczba':['sum']})
# grupa.plot(kind='pie',title="Liczba urodzonych dzieci w ostatnich 5 latach",subplots = True, autopct='%.2f %%',fontsize=10,figsize=(5,5),colors=['darkgreen','purple'])
# plt.show()

# zad4
df = pd.read_csv('zamowienia.csv',header=0,sep=";",decimal=".")
# print(df)
grupa = df.groupby('Sprzedawca').agg({'idZamowienia':['sum']})
print(grupa)
grupa.plot(kind="bar",xlabel="sprzedawcy",figsize=(10,5),ylabel="ilość zamówień",rot=0,title="ilość założonych zamówień")
plt.legend(['Ilość zamówień'])
plt.show()