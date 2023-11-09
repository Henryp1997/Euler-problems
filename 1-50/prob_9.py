import math

for c in range(2, 1001):
    try:
        if (x := math.sqrt(c**2 + 2000*c - 1e6)) % 1 == 0:
            b = int(0.5 * ((1000 - c) + x))
            if (a := 1000 - b - c) > 0:
                print(a, b, c)
                print(a * b * c)
    except ValueError: # sqrt domain error
        pass
