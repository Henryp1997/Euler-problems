#%%
import itertools
import math
import numpy as np
from tqdm import tqdm
from sympy.utilities.iterables import multiset_permutations

# n=4 gives 36324288000 unique sequences

n = 4
lst = []
for i in range(n):
    for j in range(4):
        lst.append(i)
seqs = list(tqdm(multiset_permutations(lst)))

# figure out maximum number of piles for each sequences
maxima = []
for j, seq_ in tqdm(enumerate(seqs)):
    max_per_seq = []
    piles_counts = [0 for i in range(n)]
    for i, val in enumerate(seq_):
        max_temp = 0
        piles_counts[val] += 1
        for count in piles_counts:
            if count in [1,2,3]: # don't count a pile with no cards or > 3 cards
                max_temp += 1
        max_per_seq.append(max_temp)
    maxima.append(max(max_per_seq))


duplicate_factor = math.factorial(4*n)/24**2

E_n = 0
for i in range(1,n+1):
    E_n += (i)*maxima.count(i)
E_n = E_n / duplicate_factor

print(E_n)
# %%
