import sys
import math
import random

# zad 1
# a = []
# for x in range(1,11):
#     a.append(1-x)
# print(a)
#
# b = []
# for x in range(0,7):
#     b.append(4**x)
# print(b)
#
# c = []
# for x in b:
#     if x%2 == 0:
#         c.append(x)
# print(c)


# zad2
# lista = []
# for x in range(0,10):
#     lista.append(random.randint(0,100))
# print(lista)
# listapa = []
# for x in lista:
#     if x%2 == 0:
#         listapa.append(x)
# print(listapa)


# zad 3
slownik = {'ziemniaki': 'kg',
           'arbuz': 'kg',
           'bułki': 'sztuki',
           'ciasto': 'sztuki'}
lista_sztuk = []
for key,value in slownik.items():
    if slownik[key] == 'sztuki':
        lista_sztuk.append(slownik[key])

print(slownik)
print(lista_sztuk)

