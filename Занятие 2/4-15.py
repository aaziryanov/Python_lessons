from math import sqrt

a = float(input('������� a '))
b = float(input('������� b '))
c = float(input('������� c '))

d = b**2 - 4*a*c
if d<0:
    print("������ ���")
else:
    print("����� ����")
    x1= (-b + sqrt(d))/(2*a)
    x2= (-b - sqrt(d))/(2*a)
    print(f"x1 = {x1}\tx2 = {x2}")