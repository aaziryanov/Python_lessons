from math import sqrt

x1 = float(input('������� x1 '))
y1 = float(input('������� y1 '))
x2 = float(input('������� x2 '))
y2 = float(input('������� y2 '))

d = sqrt( (x2-x1)**2 + (y2-y1)**2 )
print(f"d={d}")