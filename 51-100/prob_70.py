#%%

import math

primes = [2]
def prime_check(n):
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True
for i in range(3, 5_000_001):
    if prime_check(i):
        primes.append(i)

def rel_prime(n, m):
    for i in range(2, int(0.5*n) + 1):
        if n % i == 0 and m % i == 0:
            return False
    return True

def totient1(n):
    delta = 0
    for m in range(1, n):
        if not rel_prime(n, m):
            delta += 1
    return n - delta - 1

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

def totient2(n):
    factors = get_prime_factors(n)
    phi = n
    for factor in factors:
        phi *= (1 - (1/factor[0]))
    if n in primes:
        phi -= 1
    return math.floor(phi)


x = []
for num in range(2, 200_001):
    phi = totient2(num)
    if phi is None:
        continue
    phi_list = [i for i in str(phi)]
    phi_list.sort()
    phi_sorted = "".join([i for i in phi_list])

    num_list = [i for i in str(num)]
    num_list.sort()
    num_sorted = "".join([i for i in num_list])

    if phi_sorted == num_sorted:
        result = num / phi
        if result < 1.00874:
            x.append((num, phi, result))
            break

# print(min(x, key=lambda y: y[2]))

# print(get_prime_factors(162619))


print(to_check)
# %%
