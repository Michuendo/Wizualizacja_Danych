import random
#zad 1
# A=[1-x for x in range(1, 11)]
# print(A)
# B=[4**x for x in range(0, 8)]
# print(B)
# C=[x for x in B if x%2==0]
# print(C)

#zad 2
# lista=[]
# for x in range(10):
#     lista.append(random.randrange(1, 50))
# print(lista)
# lista2=[x for x in lista if x%2==0]
# print(lista2)

#zad 3
# produkty={'Masło':"KG", "Bułki":"Sztuki", "Cukierki":"KG","Karton_mleka":"Sztuki"}
# print(produkty)
# produkty2={key:value for key, value in produkty.items() if value=="Sztuki"}
# print(produkty2)

#zad 4
# def czyProstokatny(a, b, c):
#     if pow(a, 2)+pow(b, 2)==pow(c, 2):
#         print("Jest prostokątny")
#     else:
#         print("Nie jest prostokątny")
# czyProstokatny(3,4,5)

#zad 5
# def poleTrapezu(a=5.5, b=6.5, h=2.5):
#     pole=((a+b)*h)/2
#     return pole
# print(poleTrapezu())

#zad 6
# def ciag(a1=1,b=4,ile=10):
#     for x in range(ile):
#         a1=a1*b
#     return a1
# print(ciag())


#zad 7
# def ciag2(*liczba):
#     if len(liczba)==0:
#         return 0
#     else:
#         iloczyn = 1
#         for x in liczba:
#             iloczyn=iloczyn*x
#     return iloczyn
# print(ciag2(1,2,3,4,5))

#zad 8
# def zakupy(**a):
#     ile=len(a.items())
#     wartosc = 0
#     for key, value in a.items():
#         wartosc+=value
#     return ile,wartosc
#
# print(zakupy(pomidor=12,salata=10))