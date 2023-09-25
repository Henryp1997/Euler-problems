from prob_46 import prime_check

primes = [2]
for i in range(3, 1_000_001, 2):
    if prime_check(i):
        primes.append(i)

for prime in primes:
    sums = []
    index = primes.index(prime)
    for j in range(index):
        current_sum = 0
        count = 0
        for i in range(j):
            current_sum += primes[i]
            count += 1
        sums.append((current_sum, count))

    
    for sum in sums:
        if prime == sum[0]:
            with open('temp.txt', 'a') as f:
                f.write(f'{sum[1]}, {prime}\n')
            f.close()
