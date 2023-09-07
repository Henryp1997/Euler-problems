import math

results = []

for i in range(10_000_000):
    digits = str(i)
    digit_sum = 0
    for k in digits:
        digit_sum += math.factorial(int(k))
    
    if digit_sum == i:
        results.append(i)
    
print(results)