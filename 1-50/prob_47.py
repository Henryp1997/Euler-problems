# %%
import math

latest = 72409

from utils import prime_check

primes = [2]
for i in range(1_000_000):
    if prime_check(i):
        primes.append(i)

def get_prime_factors(n):
    factors = []
    for i in range(2, int(n/2)+1):
        if n % i == 0 and i in primes:
            factors.append(i)
    return factors

n = 0
while True:
    if n not in primes:
        factors = get_prime_factors(n)
        if len(factors) == 4:
            result = 0
            for i in range(1, 4):
                if all((n + i) % factor in (0, i) for factor in factors):
                    if len(get_prime_factors(n + i)) == 4:
                        result += 1
                        continue
            if result == 3:
                print(n)
                break
    n += 1


# %%
