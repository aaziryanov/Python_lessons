from math import sqrt
a = float(input('������� a '))
c = float(input('������� c '))
h = float(input('������� h '))
p = a + c + sqrt( ((c-a)**2)/4 + h**2 )
print(f"P={p}")