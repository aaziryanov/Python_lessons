from math import sqrt, sin
x = float(input('¬ведите x '))
y = float(input('¬ведите y '))

z = (x + (2+y)/(x**2)) / (y + 1/sqrt(x**2 + 10))
q = 7.25*sin(x) - abs(y)
print(f"z={z}, q={q}")