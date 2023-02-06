from math import sqrt

a = float(input('Введите a '))
b = float(input('Введите b '))
c = float(input('Введите c '))

d = b**2 - 4*a*c
if d<0:
    print("Корней нет")
else:
    print("Корни есть")
    x1= (-b + sqrt(d))/(2*a)
    x2= (-b - sqrt(d))/(2*a)
    print(f"x1 = {x1}\tx2 = {x2}")