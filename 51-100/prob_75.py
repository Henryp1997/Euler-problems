import math

# squares = [n**2 for n in range(1, 100)]

# triples = []
# values = []
# for square in squares:
#     for other_square in squares:
#         if (square + other_square) in squares:
#             a = int(math.sqrt(square)); b = int(math.sqrt(other_square)); c = int(math.sqrt(square + other_square))
#             if (b, a, c) not in triples:
#                 triples.append((a, b, c))
#                 values.append(a + b + c)

# values.sort()
# print(values)

primes = [2]
def prime_check(n):
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True
for i in range(3, 750_001):
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

for n in range(12, 100, 2):
    singular = len([i[1] for i in get_prime_factors(n) if i[1] % 2 == 0]) > 0
    if singular:
        print(n)

# values = [12, 24, 30]
# n = 32
# while n < 40:
#     for i, val in enumerate(values):
#         count = 0
#         multiples = []
#         for j in range(i):
#             if n % values[j] == 0:
#                 skip_val = False
#                 for multiple in multiples:
#                     if multiple % (n / values[j]) == 0:
#                         skip_val = True
#                 if not skip_val:
#                     multiples.append(int(n/values[j]))
#                     count += 1
#                     if count == 1:
#                         values.append(n)
#                     if count == 2:
#                         break
#     n += 2

# print(values)