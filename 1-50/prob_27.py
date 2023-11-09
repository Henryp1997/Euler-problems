import math

def prime_check(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def count_consecutive(a, p):
    n = 1
    count = 0
    while True:
        next_p = p + (2*n - 1) + a
        if not prime_check(next_p):
            return n
        p = next_p
        n += 1
        count += 1

primes_to_check = [i for i in range(1, 1001, 2) if prime_check(i)]

results = []
for prime in primes_to_check:
    for a in range(1, 1001, 2): # step size 2 since a must be odd
        results.append((a, prime, count_consecutive(a, prime)))
        results.append((-a, prime, count_consecutive(-a, prime)))

result = max(results, key=lambda x: x[2])
print(result)
print(result[0] * result[1])


# %%
