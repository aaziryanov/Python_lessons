from math import sqrt, sin
a = float(input('¬ведите a '))
b = float(input('¬ведите b '))

x = ( 2/(a**2+25) + b ) / (sqrt(b) + (a+b/2))
y = (abs(a) + 2*sin(b)) / (5.5*a)
print(f"x={x}, y={y}")