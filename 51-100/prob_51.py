import math
import sys

primes = []
raw_primes = []

def prime_check(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

for i in range(100000, 1000000):
    if prime_check(i):
        digits = list(str(i))
        repeated_count = 0
        checked_digits = []
        for j, digit in enumerate(digits):
            if digits.count(digit) > 1 and digit not in checked_digits:
                repeated_count += 1
                checked_digits.append(digit)

        if repeated_count != 0:
            if repeated_count == 1 and digits.count(digits[-1]) == 2:
                continue
            primes.append((int(repeated_count), checked_digits, i))
            raw_primes.append(i)


one_to_nine = [str(i) for i in range(10)]
for prime in primes:
    break_outer = False
    digits_to_replace = prime[1]
    value = prime[2]

    for digit in digits_to_replace:
        permutations = [str(value).replace(digit, val) for val in one_to_nine]

        count = 0
        perms_prime = []
        for n in permutations:
            if int(n) in raw_primes:
                perms_prime.append(n)
                count += 1

        if count == 8:
            print(value)
            sys.exit()
