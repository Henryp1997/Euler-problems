import numpy as np
import math

x = [[131,673,234,103,18],[201,96,342,965,150],[630,803,746,422,111],[537,699,497,121,956],[805,732,524,37,331]]
x = np.array(x)
y = np.matrix.transpose(x)

with open('p081_matrix.txt','r') as f:
    data = f.readlines()

x = []
for j, line in enumerate(data):
    lst = []
    for i in line.split(","):
        if '\n' in i:
            i = i.split("\n")[0]
        lst.append(int(i))
    x.append(list(lst))

x = np.array(x)

# perm = [1,0,0,1,0,1,1,0]

# steps = [1,1,0,0,1,0,1,0]

# def find_sum(permutation):
#     a, b = 0, 0
#     nums_hit = []
#     nums_hit.append(x[0,0])
#     for step in permutation:
#         if step == 1:
#             a += 1
#         elif step == 0:
#             b += 1
#         nums_hit.append(x[a,b])
#     return sum(nums_hit)


def find_permutation(a,b):
    if x[a - 1, b] < x[a, b - 1]:
        a, b = a-1, b
    else:
        a, b = a, b-1
    return a, b

a, b = [len(x[0])-1, len(x[0])-1]
result = 0
coords_hit = []
nums_hit = []
result += x[-1,-1]
for i in range(142):
    a,b = find_permutation(a,b)
    nums_hit.append(x[a,b])
    coords_hit.append((x[a,b], (a,b)))
    result += x[a,b]

print(coords_hit)
print(len(nums_hit))
print(result)