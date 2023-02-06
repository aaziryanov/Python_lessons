from math import sqrt
a = float(input('¬ведите a '))
c = float(input('¬ведите c '))
h = float(input('¬ведите h '))
p = a + c + sqrt( ((c-a)**2)/4 + h**2 )
print(f"P={p}")