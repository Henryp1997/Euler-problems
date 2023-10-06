import math
import itertools

def prime_check(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

primes = [2]
for i in range(3, 1001, 2):
    if prime_check(i):
        primes.append(i)
