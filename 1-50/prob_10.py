import math

def prime_check(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

s = 0
for n in range(2, 2_000_000):
    if prime_check(n):
        s += n

print(s)