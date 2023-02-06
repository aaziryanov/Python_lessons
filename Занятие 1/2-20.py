from math import sqrt, sin, cos
e = float(input('¬ведите e '))
f = float(input('¬ведите f '))
g = float(input('¬ведите g '))
h = float(input('¬ведите h '))

a = sqrt( abs(e-3/f)**3 + g )
b = sin(e) + (cos(h))**2
c = 33*g / (e*f-3)
print(f"a={a}, b={b}, c={c}")