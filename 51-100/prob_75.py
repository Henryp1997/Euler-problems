#%%
import math
import collections

# the sum a + b + c is always even given that a^2 + b^2 = c^2
# generate all primative triples whose sum does not exceed 1,500,000

singulars = {}
arr = []
for m in range(1, 866):

    if m % 2 == 0:
        n_range = range(1, m, 2)

    if m % 2 == 1:
        n_range = range(2, m + 1, 2)

    for n in n_range:
        if math.gcd(n, m) == 1 and (m - n) % 2 == 1:
            a = m**2 - n**2
            b = 2 * m * n
            c = m**2 + n**2
            if a + b + c > 1_500_000:
                continue
            singulars[a + b + c] = 1


for num in list(singulars.keys()):
    for i in range(2, math.floor(1_500_000 / num) + 1):
        val = num * i
        if val > 1_500_000:
            break
        try:
            singulars[val] += 1
        except:
            singulars[val] = 1

singulars = collections.OrderedDict(sorted(singulars.items()))

count = 0
for i in list(singulars.keys()):
    if singulars[i] == 1:
        count += 1

print(count)

# %%
