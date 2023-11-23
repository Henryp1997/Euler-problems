import time
time_start = time.time()

from utils import prime_check

def sort_string(n):
    n = list(str(n))
    n.sort()
    return int("".join(n))

# only need to check 4 and 7 digit numbers since n*(n+1)/2
# is a multiple of 3 for n = 2, n = 3, n = 5, n = 6, n = 8, n = 9

current_prime = 0

# 4 digit numbers
for n in range(1234, 9877, 2):
    if sort_string(n) == 1234:
        if n > current_prime:
            if prime_check(n):
                current_prime = n

# 7 digit numbers
for n in range(1234567, 9876545, 2):
    if sort_string(n) == 1234567:
        if n > current_prime:
            if prime_check(n):
                current_prime = n

if __name__ == "__main__":
    print(current_prime)
    print(f'{(time.time() - time_start) * 1000:.2f}ms')