from math import tan

a = float(input('¬ведите a '))
c = float(input('¬ведите c '))
alpha = float(input('¬ведите alpha '))
h = (c-a)/2*tan(alpha/180*3.14)
s = (a+c)/2*h
print(f"S={s}")