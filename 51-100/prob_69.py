import time
import math

primes = [2]
def prime_check(n):
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True
for i in range(3, 1_000_001):
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

def totient(n):
    factors = get_prime_factors(n)
    phi = n
    for factor in factors:
        phi *= (1 - (1/factor[0]))
    return round(phi)

# hypothesise that the answer is not going to be a prime
# also hypothesise that if m = n^k for any value m already computed, then the result n / phi(n) is the same
# the list of numbers in the file 69_nums_to_check has these numbers removed

with open('69_nums_to_check.txt', 'r') as f:
    nums = f.readlines()

nums = [int(i) for i in nums]

now = time.time()

results = []
for n in nums:
    # also hypothesise that if m = n^k for any value m already computed, then the result n / phi(n) is the same
    result = (n, n / totient(n))
    with open('69_results.txt', 'a') as f:
        f.write(f'{result}\n')
    results.append(result)

print(max(results, key=lambda x: x[1])[0])
print(time.time() - now)

""" generate 69_nums_to_check.txt file """
# import math
# import numpy as np
# nums = list(range(2, 1_000_001))

# primes = [2]
# def prime_check(n):
#     for i in range(2, int(math.sqrt(n) + 1)):
#         if n % i == 0:
#             return False
#     return True
# for i in range(3, 1_000_001):
#     if prime_check(i):
#         primes.append(i)

# # now remove all numbers which are squares, cubes, fourths etc
# power_nums = []
# for i in range(2, 1_000_001):
    
#     with open('test.txt', 'w') as f:
#         f.write(f'{i}\n')
#     for j in range(2, int(math.sqrt(i)) + 1):
#         k = np.log10(i) / np.log10(j)
#         if k / (math.ceil(k)) == 1:
#             power_nums.append(i)
#             break

# nums = list(set(nums) - set(primes) - set(power_nums))

# with open('out.txt', 'w') as f:
#     for num in nums:
#         f.write(f'{num}\n')