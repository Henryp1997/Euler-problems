coins = [1, 2, 5, 10, 20, 50, 100, 200]

N = [1]
for n in range(2, 11):
    count = N[-1]
    if n in coins:
        count += 1
    for coin in coins:
        if n % coin == 0 and coin not in (1, n):
            count += 1
    N.append(count)

print(N)