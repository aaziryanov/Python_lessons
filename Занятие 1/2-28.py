from math import tan

a = float(input('������� a '))
c = float(input('������� c '))
alpha = float(input('������� alpha '))
h = (c-a)/2*tan(alpha/180*3.14)
s = (a+c)/2*h
print(f"S={s}")