from math import sin

x = float(input('¬ведите x '))
k=0
if sin(x)<0:
    k=x**2
else:
    k=abs(x)
y=0    
if k<x:
    y=k*x
else:
    y=k+x
print(f"Y = {y}")