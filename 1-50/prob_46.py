import math
from utils import prime_check

primes = [2]

if __name__ == "__main__":

    n = 1
    while True:
        n += 2
        if prime_check(n):
            primes.append(n)
            continue

        cont = False
        for prime in primes:
            if math.sqrt(0.5 * (n - prime)) % 1 == 0:
                cont = True
        if cont:
            continue
        
        print(n)
        break