from math import sqrt

x1 = float(input('¬ведите x1 '))
y1 = float(input('¬ведите y1 '))
x2 = float(input('¬ведите x2 '))
y2 = float(input('¬ведите y2 '))

d = sqrt( (x2-x1)**2 + (y2-y1)**2 )
print(f"d={d}")