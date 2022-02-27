import sys

x = int(input("Podaj zmienną x: "))
y = int(input("Podaj zmienną y: "))
z = input("Operatory do użycia(+,-,*,/,**)")

if z == "+":
    print(x+y)
elif z == "-":
    print(x-y)
elif z == "*":
    print(x*y)
elif z == "/":
    print(x/y)
elif z == "**":
    print(x**y)
else:
    print("Podaj inny operator")