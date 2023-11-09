numerators = [3]
denominators = [2]

count = 0
for i in range(1, 1001):
    d = denominators[i-1] + numerators[i-1]
    denominators.append(d)
    n = denominators[i] + denominators[i-1]
    numerators.append(n)
    if len(str(n)) > len(str(d)):
        count += 1

print(count)