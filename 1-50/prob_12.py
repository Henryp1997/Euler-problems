import math
import numpy as np

# generate triangle numbers greater than 500
# when is n(n+1)/2 > 500? --> n^2 + n - 1000 = 0 --> n approx 31

def check_factors(num):
    count = 2
    factors_checked = [1, num]
    for i in range(2, num):
        if i not in factors_checked:
            if num % i == 0:
                count += 2 # add two because the factor must be multiplied by another number
                factors_checked.append(i)
                factors_checked.append(int(num / i))

    return count

# n = 30
# for i in range(1, 1000):
#     a = i * n
#     count = check_factors(a)
#     print(i, count)

# with open('12.txt', 'a') as f:
#     n = 1779
#     results = []
#     while True:
#         tri_num = int((n*(n+1))/2)

#         if tri_num % 10 != 0:
#             n += 1
#             continue

#         count = check_factors(tri_num)
#         f.write(f'{n}, {tri_num}, {count}\n')

#         if count > 500:
#             print(tri_num)
#             break

#         n += 1
#

x = math.factorial(500)

print(x)

y = 1 + 8*x

print((10**568)**2 > y)