import math

num_multiples = []

for i in range(2, 1001):
    count = 0
    for j in range(2, math.floor(math.sqrt(i)) + 1):
        if i % j == 0:
            count += 1
    num_multiples.append(count)

for i in range(2, 1001):
    try:
        if num_multiples[i - 2] == max(num_multiples):
            print(i)
            break
    except:
        pass