import math
import sys

index = 2
n = 3
while True:
    continue_loop = False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            continue_loop = True
            continue
    if continue_loop:
        n += 2
        continue
    if index == 10_001:
        print(n)
        sys.exit()
    n += 2
    index += 1
