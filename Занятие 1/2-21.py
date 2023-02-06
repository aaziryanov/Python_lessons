from math import sqrt, sin
e = float(input('¬ведите e '))
f = float(input('¬ведите f '))
g = float(input('¬ведите g '))
h = float(input('¬ведите h '))

a = (e+f/2)/3
b = abs(h*h-g)
c = sqrt( (g-h)**2 - 3*sin(e) )
print(f"a={a}, b={b}, c={c}")