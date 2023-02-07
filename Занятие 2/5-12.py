from math import exp

for h in range(0,1100,100):
    p = 1.29 * exp(-h*1.25*10**(-4))
    print(f"h={h}\tp={p}")