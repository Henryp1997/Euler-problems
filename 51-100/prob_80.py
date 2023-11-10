import math
import sys

def digital_expansion(N):
    sqrt = math.floor(math.sqrt(N))
    for i in range(1, 100):
        for j in range(10):
            check = str(sqrt) + str(j)

            to_check = str(int("".join([i for i in str(check)])) ** 2)

            if N >= 17:
                reached = int(to_check[:len(str(N))]) >= N
            else:
                reached = int(to_check[:len(str(N))]) == N
            if reached:
                sqrt = str(sqrt) + str(j - 1)
                break
            else:
                if check[-1] == '9':
                    sqrt = str(sqrt) + str('9')

    return sqrt


results = []

for N in range(2, 100):

    if math.sqrt(N) % 1 == 0:
        continue

    sqrt = digital_expansion(N)
    results.append((N, sqrt, float(sqrt)**2, sum([int(i) for i in sqrt if i != '.'])))

print(sum([i[3] for i in results]))
