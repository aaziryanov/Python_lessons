from math import sqrt, sin, cos
e = float(input('������� e '))
f = float(input('������� f '))
g = float(input('������� g '))
h = float(input('������� h '))

a = sqrt( abs(e-3/f)**3 + g )
b = sin(e) + (cos(h))**2
c = 33*g / (e*f-3)
print(f"a={a}, b={b}, c={c}")