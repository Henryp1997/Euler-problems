from utils import prime_check

primes = [2]
for i in range(3, 500000):
    if prime_check(i):
        primes.append(i)

def get_prime_factors(n):
    factors = []
    for i in range(2, int(n/2)+1):
        if n % i == 0 and i in primes:
            factors.append(i)
    return factors


def totient(n):
    factors = get_prime_factors(n)
    if factors == []:
        return n - 1
    phi = n
    for factor in factors:
        phi *= (1 - (1/factor))
    return round(phi)

tot = 0
for i in range(2, 10):
    tot += totient(i)
    print(i, tot)