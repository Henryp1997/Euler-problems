#%%

from utils import prime_sieve

primes = prime_sieve(1_000_100)

max_length = 2
max_num = 1_000_000
loc_max_num = [i for i, prime in enumerate(primes) if prime > max_num][0] + 1
while True:
    break_outer = False
    for i in range(loc_max_num - max_length):
        primes_to_add = primes[i:i + max_length]
        if primes_to_add[0] != 2 and max_length % 2 == 0:
            max_length += 1
            break
        potential = sum(primes_to_add)
        if potential > max_num:
            
            if i == 0:
                break_outer = True
                break
            else:
                max_length += 1
                break

        if potential in primes:
            print(potential, max_length, primes_to_add)
            max_length += 1
            break
    if break_outer:
        break
print(max_length)
# %%
