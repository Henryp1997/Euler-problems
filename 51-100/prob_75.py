#%%

# the sum a + b + c is always even given that a^2 + b^2 = c^2

from utils import prime_check
primes = [2]
for i in range(3, 750_001):
    if prime_check(i):
        primes.append(i)

def has_even_power_prime_factor(n):
    factors = []
    for i in range(2, int(n/2)+1):
        if n % i == 0 and i in primes:
            power = 1
            while True:
                if int(n / (i**power)) % i != 0:
                    factors.append((i, power))
                    if power % 2 == 0:
                        return True
                    else:
                        break
                power += 1
    return False

results = []
for i, n in enumerate(range(12, 1_000, 2)):
    singular = has_even_power_prime_factor(n)
    if singular:
        results.append(n)

for i, j in enumerate(results):
    try:
        print(j, j - results[i - 1])
    except:
        print(j)

# %%
results = []
for n in range(200):
    # break1, break2, break3 = False, False, False
    for a in range(3, n):
        for b in range(3, n):
            for c in range(3, n):
                if a + b + c == n and a**2 + b**2 == c**2:
                    if (n, b, a, c) not in results:
                        results.append((n, a, b, c))
    #                 break1, break2, break3 = True, True, True
    #                 break
    #         if break1:
    #             break
    #     if break2:
    #         break
    # if break3:
    #     continue
for i in results:
    if (i[0] - 2) % 6 == 0:
        print(i)
# %%
