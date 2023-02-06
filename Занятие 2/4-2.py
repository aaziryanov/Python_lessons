from math import sin

x = float(input('¬ведите x '))
y=0
if x>0:
    y=(sin(x))**2
else:
    y=1-2*sin(x**2)
print(f"Y = {y}")