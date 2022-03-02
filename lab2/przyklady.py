import sys
import math

# ---------przyklad 1----------

# a = int(input("podaj a:"))
# b = int(input("podaj b:"))
# if a==b:
#     print("obie zmienne są równe")
# elif a>b:
#     print("a jest wieksze od b")
# else:
#     print("b jest wieksze od a")


#  ---------przylad 2----------

# a = int(input("podaj a:"))
# b = int(input("podaj b:"))
# c = int(input("podaj c:"))
# d = int(input("podaj d:"))
#
# if (a>b)&(c>d):
#     print("jest git")
# else:
#     print("nie jest git")


#  ---------Przyklad 3----------

# range(start,stop,step)

# a = int(input("podaj a:"))
# for x in range(1,a+1,1):
#     print(x)


# ---------Przykład 4----------

# lista = ['a',5,4,6,5.6]
#
# for x in lista:
#     print(x)
# else:
#     print("Wyświetlone zostały wszystkie elementy z listy")

# ----------Przykład 4----------
#
# x=0
# while x<11:
#     print(x)
#     x+=1

# ----------Przykład 5-----------

# lista = [4,6,9,5,7,2,3]
# liczba = input('podaj liczbę:')
# licznik = 0
# while licznik < len(lista):
#     if int(liczba) - lista[licznik] == 0:
#         print('liczba ' + str(liczba)+' - '+str(lista[licznik])+' = 0\n')
#         break
#     else:
#         licznik +=1
# else:
#     print('żadna z wartości nie dała odpowiedniego wyniku')


# ----------Przykład 6-----------
# lista1 = [4,6,8,2,3,9]
# lista2 = [4,7,5,2]
# suma = []
# for a in lista1:
#     for b in lista2:
#         wynik = a + b
#         suma.append(wynik)
#     print(suma)
# ----------Przykład 7-----------
#
# try:
#     wynik = a/b
#     print(wynik)
# except ZeroDivisionError:
#     print("Nie można dzielić przez zero")
# except ValueError:
#     print("nie wczytano liczby całkowitej")


