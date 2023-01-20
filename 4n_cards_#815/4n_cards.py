#%%
import itertools
import math
import numpy as np
from tqdm import tqdm
from sympy.utilities.iterables import multiset_permutations

# n=4 gives 36324288000 unique sequences

n = 3
lst = []
for i in range(n):
    for j in range(4):
        lst.append(i)
seqs = list(tqdm(multiset_permutations(lst)))

# figure out maximum number of piles for each sequences
maxima = []
for j, seq in tqdm(enumerate(seqs)):
    max_per_seq = []
    piles_counts = [0 for i in range(n)]
    for i, val in enumerate(seq):
        max_temp = 0
        piles_counts[val] += 1
        for count in piles_counts:
            if count in [1,2,3]: # don't count a pile with no cards or > 3 cards
                max_temp += 1
        max_per_seq.append(max_temp)
    maxima.append(max(max_per_seq))


duplicate_factor = len(seqs)
print(maxima.count(1))
E_n = 0
for i in range(1,n+1):
    E_n += (i)*maxima.count(i)
E_n = E_n / duplicate_factor

print(E_n)

E_n = (2*duplicate_factor - maxima.count(1) + maxima.count(3)) / duplicate_factor
print(E_n)


# %%
import random
from tqdm import tqdm

n = 4
seqs = []
orig = []
for i in range(n):
    for j in range(4):
        orig.append(i)

for N in [10,50,100,500,1000,5000,10000]:
    for k in tqdm(range(N)):
        lst = []
        nums_used = []
        for l in range(1000):
            num = random.randint(0,4*n - 1)
            if num not in nums_used:
                lst.append(orig[num])
                nums_used.append(num)

        if lst not in seqs:
            seqs.append(lst)

    print(f'num sequences: {len(seqs)}')
    # figure out maximum number of piles for each sequences
    maxima = []
    for j, seq in tqdm(enumerate(seqs)):
        max_per_seq = []
        piles_counts = [0 for i in range(n)]
        for i, val in enumerate(seq):
            max_temp = 0
            piles_counts[val] += 1
            for count in piles_counts:
                if count in [1,2,3]: # don't count a pile with no cards or > 3 cards
                    max_temp += 1
            max_per_seq.append(max_temp)
        maxima.append(max(max_per_seq))

    for i in range(1,5):
        print(maxima.count(i))

    duplicate_factor = len(seqs)

    E_n = 0
    for i in range(1,n+1):
        E_n += (i)*maxima.count(i)
    E_n = E_n / duplicate_factor

    print(f'Result: {E_n}')

# %%
