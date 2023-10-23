import math
import itertools

def prime_check(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

primes = [2]
for i in range(3, 10001, 2):
    if prime_check(i):
        primes.append(i)

for prime in primes:
    count = 0
    for i in [3, 7, 109, 673]:
        new_prime1 = int(str(prime) + str(i))
        new_prime2 = int(str(i) + str(prime))
        if prime_check(new_prime1) and prime_check(new_prime1):
            count += 1
            continue
        break
    if count == 4:
        print(prime + sum([3, 7, 109, 673]))
        break
