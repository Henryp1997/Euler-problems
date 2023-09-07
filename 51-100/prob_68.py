import random, time


# for i in range(100):
for i in range(5):

    if i == 0:
        a, b, c = 0, 0, 0
        while a == b and b == c and a == c:
            a = random.randint(1, 9); b = random.randint(1, 9); c = random.randint(1, 9)
        row1 = [a, b, c]

        remaining_digits = [i for i in range(1, 10) if i not in row1]

        row_sum = sum(row1)
        if row_sum < remaining_digits[0] + remaining_digits[1]:
            break

        rows = [row1]
        continue

    remainder = row_sum - rows[i - 1][2]

    t = time.time()
    while True and time.time() - t < 10:
        x = random.randint(min(remaining_digits), max(remaining_digits)); y = random.randint(min(remaining_digits), max(remaining_digits))
        if x + y == remainder and x != y:
            break

    row = [x, rows[i - 1][2], y]
    remaining_digits = [i for i in remaining_digits if i != x and i != y]
    rows.append(row)

print(rows)