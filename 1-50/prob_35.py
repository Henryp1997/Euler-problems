import math

def cycle_prime(n):
    n = str(n)
    others = []
    for i in range(len(n)):
        new_n = [n[a - i] for a in range(len(n))]
        others.append(int("".join(new_n)))
    return others

def prime_check(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

count = 0
for i in range(2, 1_000_000):
    if any(val in str(i) for val in ['2', '4', '5', '6', '8', '0']) and len(str(i)) > 1:
        continue
    if prime_check(i):
        result = [prime_check(p) for p in cycle_prime(i)]
        if False not in result:
            count += 1
    
print(count)
 