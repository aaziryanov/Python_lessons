from math import sqrt, sin
e = float(input('������� e '))
f = float(input('������� f '))
g = float(input('������� g '))
h = float(input('������� h '))

a = (e+f/2)/3
b = abs(h*h-g)
c = sqrt( (g-h)**2 - 3*sin(e) )
print(f"a={a}, b={b}, c={c}")