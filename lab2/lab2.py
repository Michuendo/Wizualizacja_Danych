import sys
import math
#zad 1
# sporty = ['kolarstwo_górskie','koszykowka','siatkówka','trójbój_siłowy']
# sporty.reverse()
# sporty.append('piłka_ręczna')
# print(sporty)

#zad 2
# slownik = {'Aten':'Ateneum', 'Arch':'Archiwum', 'Bibl':'Biblioteka'}
# print(slownik['Aten'])

#zad 3
# slownik = {'Wiedzmin_3':'10', 'Metin_2':'7', 'Minecraft':'8', 'Terraria':'7'}
# print (len(slownik))

#zad 4
# napis = input("Wprowadz napis: ")
# i=0
# for x in napis:
#     if x == 'a':
#         i+=1
# print(i)

#zad 5
# system.stdout.write("Podaj a: ")
# a = system.stdin.readline()
# system.stdout.write("Podaj b: ")
# b = system.stdin.readline()
# system.stdout.write("Podaj c: ")
# c = system.stdin.readline()
# a=int(a)
# b=int(b)
# c=int(c)
# wynik=pow(a, b)+c
# wynik=str(wynik)
# system.stdout.write(wynik)

# zad 6
# a = input("Podaj a: ")
# b = input("Podaj b: ")
# c = input("Podaj c: ")
#
# a=int(a)
# b=int(b)
# c=int(c)
#
# if a>b and a>c:
#     print(str(a) + " jest największa liczbą")
# if b>a and b>c:
#     print(str(b) + " jest najwieksza liczbą")
# if c>a and c>b:
#     print(str(c) + " jest najwieksza liczbą")


#zad 7
# lista=[4, 2, 1.4, 8, 21.15, 555,6.2,1]
# for x in lista:
#     x=pow(x, 2)
#     print(x)

#zad 8
# i=0
# lista=[]
# while(i<10):
#     x=input("Podaj liczbe: ")
#     x=int(x)
#     if(x%2==0):
#         lista.append(x)
#     i+=1
# print(lista)

#zad 9
a=input("Podaj liczbe: ")
a=int(a)
try:
    if (a<1):
        raise ValueError
    pierwiastek=math.sqrt(a)
    print(pierwiastek)
except ValueError:
    print("Podaj prawdiłową liczbe")