from utils import prime_check

s = 0
for n in range(2, 2_000_000):
    if prime_check(n):
        s += n

print(s)