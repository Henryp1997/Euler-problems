import math

N = 26241

top_right = [4*(n**2) - 2*n + 1 for n in range(1, int(N/2) + 1)]
top_left = [4*(n**2) + 1 for n in range(1, int(N/2) + 1)]
bottom_left = [4*(n**2) + 2*n + 1 for n in range(1, int(N/2) + 1)]

def prime_check(num):
    for i in range(2, math.floor(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

count = 0

for val in top_right:
    if prime_check(val):
        count += 1

for i, val in enumerate(top_left):
    if prime_check(val):
        count += 1

for val in bottom_left:
    if prime_check(val):
        count += 1

total = 2*N - 1

if count < 0.1 * (total):
    print("yes", N, count, total)
print((count / total) * 100)

# print(ratios)