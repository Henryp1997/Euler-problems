import math

p = 0

while True:
    p += 1
    if (sqrt := math.sqrt(1 - 4*p + 12*(p**2))) % 4 == 3:
        if p > 165:
            # calculate triangle number from index of pentagonal number
            t = int(0.5 * (-1 + sqrt))
            h = int(0.25 * (1 + sqrt))
            tri_num = int(0.5 * t * (t + 1))
            pent_num = int(0.5 * p * (3*p - 1))
            hex_num = int(h * ((2*h) - 1))

            print(tri_num, pent_num, hex_num)
            print(t, p, h)
            break