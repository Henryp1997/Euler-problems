numerators = [3]
denominators = [2]

for i in range(1, 1001):
    denominators.append(denominators[i-1] + numerators[i-1])
    numerators.append(denominators[i] + denominators[i-1])

count = 0
for i, val in enumerate(numerators):
    if len(str(val)) > len(str(denominators[i])):
        count += 1

print(count)