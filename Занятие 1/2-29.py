from math import sqrt

x1 = float(input('������� x1 '))
y1 = float(input('������� y1 '))
x2 = float(input('������� x2 '))
y2 = float(input('������� y2 '))
x3 = float(input('������� x3 '))
y3 = float(input('������� y3 '))

a = sqrt( (x2-x1)**2 + (y2-y1)**2 )
b = sqrt( (x3-x1)**2 + (y3-y1)**2 )
c = sqrt( (x2-x3)**2 + (y2-y3)**2 )
P = a+b+c
p = P/2
S = sqrt( p*(p-a)*(p-b)*(p-c) )
print(f"P={P}, S={S}")