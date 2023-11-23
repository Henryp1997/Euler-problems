import math

def prime_check(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True

def prime_sieve(n):
    arr = [(0, False), (1, False)] + [(i, True) for i in range(2, n + 1)]
    for i in range(2, n + 1):
        if arr[i][1]:
            count = 0
            while True:
                j = (i ** 2) + (i * count)
                if j > n:
                    break
                arr[j] = (j, False)
                count += 1
    return [i[0] for i in arr if i[1]]

