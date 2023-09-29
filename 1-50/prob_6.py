n = 100

sum_square = (0.5 * n * ((n + 1) * (n - 1) + 2))
for i in range(1, n - 1):
    sum_square -= 0.5 * i * (i + 1)

square_sum = (0.5 * n * (n + 1)) ** 2

print(int(square_sum - sum_square))