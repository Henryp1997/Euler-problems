#%%
import math
from utils import prime_check

primes = [2]
for i in range(3, 500000):
    if prime_check(i):
        primes.append(i)

def get_prime_factors(n):
    factors = []
    for i in range(2, int(n/2)+1):
        if n % i == 0 and i in primes:
            power = 1
            while True:
                if int(n / (i**power)) % i != 0:
                    factors.append((i, power))
                    break
                power += 1
    return factors

def totient_two_factors(p1, p2):
    return p1 * p2 * (1 - (1/p1)) * (1 - (1/p2))


def check_perm(n, m):
    n_list = [i for i in str(n)]
    n_list.sort()
    n_sorted = "".join([i for i in n_list])

    m_list = [i for i in str(m)]
    m_list.sort()
    m_sorted = "".join([i for i in m_list])

    if n_sorted == m_sorted:
        return True
    return False

loc_start_check = [i - 1 for i, j in enumerate(primes) if j > math.sqrt(1e7)][0]

results = []
for prime in primes[loc_start_check::-1]:
    for other_prime in primes[loc_start_check:]:
        
        product = int(prime * other_prime)

        if product > 1e7:
            break

        phi = int(totient_two_factors(prime, other_prime))
        if abs(phi - product) % 9 == 0:
            if check_perm(phi, product):
                results.append((product, phi, product / phi))

print(len(results))
print(min(results, key = lambda x: x[2]))



# %%
