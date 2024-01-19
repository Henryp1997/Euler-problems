# for 99, there is 1 way
# for 98, there are two ways
# for 97, there are three ways
# etc, up until 50, where there are N(50) ways to add to 100

target = 100

totals = [0] * (target + 1)
totals[0] = 1

for i in range(1, target):
    for j in range(i, target + 1):
        totals[j] += totals[j - i]

print(totals)