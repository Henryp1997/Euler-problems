# only need to check 4 digit numbers for the product
# this is because d(a) + d(b) = 9 - d(c) where d(x) is the number of digits in x
# but also d(ab) = d(c), so floor(log(a) + log(b)) + 1 = floor(log(c)) + 1
# --> floor(log(a)) + floor(log(b)) + 1 <= floor(log(c)) + 1
# --> d(a) - 1 + d(b) <= d(c)
# (use d(a) + d(b) = 9 - d(c)) --> d(c) >= 4

import math
import sys

def get_divisors(n):
    divisors = []
    for i in range(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            divisors.append(i)
            divisors.append(int(n / i))
    divisors.sort()
    return divisors[:-1]

all_digits = "123456789"

def check_all_different(n):
    return all(str(n).count(val) == 1 for val in str(n))

results = []
for i in range(1234, 9876):
    if set(str(i)).issubset(all_digits) and check_all_different(i):
        remaining_digits = "".join(list(set(all_digits) - set(str(i))))
        for divisor in get_divisors(int(i)):
            if set(str(divisor)).issubset(remaining_digits) and check_all_different(divisor):
                final_digits = list(set(remaining_digits) - set(str(divisor)))
                final_digits.sort()
                other_divisor = list(str(int(i / divisor)))
                other_divisor.sort()
                if other_divisor == final_digits and check_all_different(int(i / divisor)):
                    results.append((i, divisor, int(i / divisor)))

print()
print(results)
print()
print(sum(list(set([i[0] for i in results]))))

