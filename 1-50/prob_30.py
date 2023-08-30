results = []

# only need to check up to 9^5 * 6 because 9^5 * 6 < 1,000,000 (so no 6 digit numbers will satisfy the check)
for i in range(2, 9**5 * 6):
    digits = [j for j in str(i)]

    if 1000 <= i <= 9999 and i > ((9**4) * 4) and '1' in digits:
        continue

    if 10000 <= i <= 99999 and i > 9**5 * 5 and '1' in digits:
        continue

    print(i)

    digits_sum = 0
    for k in digits:
        digits_sum += int(k)**5

    if digits_sum == i:
        results.append(i)
    
print(results)