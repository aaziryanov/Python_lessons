from math import sqrt
for h in range(1,11):
    d = sqrt( (6350+h)**2 - 6350**2)
    print(f"h={h}\td={d}")