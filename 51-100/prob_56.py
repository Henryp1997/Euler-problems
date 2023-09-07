sums = []

for a in range(1, 100):
    for b in range(1, 100):
        current = a**b
        digits = str(current)
        digit_sum = 0
        for dig in digits:
            digit_sum += int(dig)
        sums.append(digit_sum)

print(max(sums))