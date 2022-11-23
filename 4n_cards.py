#%%
import itertools
import math
import numpy as np

n = 2
lst = list(range(4*n))
seqs = list(itertools.permutations(lst))
seqs_new = []

# generate all possible sequences of values (includes duplicates)
for seq in seqs:
    s_temp = []
    for i, j in enumerate(list(seq)):
        if j in [0,1,2,3]:
            s_temp.append(0)
        elif j in [4,5,6,7]:
            s_temp.append(1)
    seqs_new.append(s_temp)

# figure out maximum number of piles for each sequences
maxima = []
for j, seq_ in enumerate(seqs_new):
    max_per_seq = []
    piles_counts = [0 for i in range(n)]
    for i, val in enumerate(seq_):
        piles_counts[val] += 1

        if piles_counts[val] > 3 or piles_counts[val - 1] > 3:
            if piles_counts[val - 1] > 3:
                max_temp = len(piles_counts) - 2
            else:
                if piles_counts[val - 1] == 0:
                    max_temp = len(piles_counts) - 2
                else:
                    max_temp = len(piles_counts) - 1
        else:
            if piles_counts[val - 1] == 0:
                max_temp = len(piles_counts) - 1
            else:
                max_temp = len(piles_counts)
        
        max_per_seq.append(max_temp)

        if j == 0:
            print(piles_counts)
            print(max_temp)

    maxima.append(max(max_per_seq))


duplicate_factor = math.factorial(4*n)

E_n = (1*maxima.count(1) + 2*maxima.count(2)) / duplicate_factor

print(E_n)
# %%
