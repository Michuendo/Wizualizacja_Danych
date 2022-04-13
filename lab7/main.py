import sys
import numpy as np
import math
import random
# Zad1
# a = np.array([2,1,5])
# b = np.array([3,8,4])
# c = a*b
# print(c)

# Zad2
# def minwier(tab):
#     for n in range(len(tab)):
#         s = 999999999999999999999
#         for x in tab[n]:
#             if x < s:
#                 s = x
#         print(" Rz¹d ", n + 1, ": ", s)
# def minkol(tab):
#     for w in range(len(tab)):
#         licznik = 999999999
#         for k in range(len(tab)):
#             if tab[k,w]<licznik:
#                 licznik = tab[k,w]
#         print("Kolumna ",w+1,":",licznik)
# a = np.array([[2,1,3],[5,2,1],[8,4,2]])
# b = np.array([[8,6,9,7],[3,2,5,2],[6,3,1,2],[4,1,2,7]])
# print("Macierz A:")
# minwier(a)
# minkol(a)
# print("------------")
# print("Macierz B:")
# minwier(b)
# minkol(b)

# zad3
# a = np.array([2,1,5])
# b = np.array([3,8,4])
# c = b.dot(a)
# print(c)

# Zad4
# a = np.array([2,1,6],dtype="int")
# b = np.array([6,3,8],dtype="float")
# print(a*b)

# zad5

# s = np.array([[2,6,4],[3,6,1]])
# a = []
# for x in range(len(s)):
#     for n in s[x]:
#         a.append( math.sin(n))
#
# print(a)
# # Zad6
# es = np.array([[6,4,2],[9,2,6]])
# b = []
#
# for x in range(len(es)):
#     for n in es[x]:
#         b.append( math.cos(n))
# print(b)
# # Zad7
# def dod(a,b):
#     lista= []
#     for x in range(len(a)):
#         lista.append(a[x]+b[x])
#     return lista
#
# print(dod(a,b))

# zad8
a=np.arange(9).reshape(3,3)
for x in a:
    print(x)

# Zad9
b = a.T
print(b)
