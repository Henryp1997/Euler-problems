from utils import prime_check

primes = [2]
for i in range(3, 1_000_001):
    if prime_check(i):
        primes.append(i)

n = 600851475143
m = 1
for prime in primes:
    if n % prime == 0:
        m *= prime
    if m == n:
        print(prime)
        break
