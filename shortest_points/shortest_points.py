import math
import tqdm
import matplotlib.pyplot as plt
import time
import numpy as np
import json


k = 2000000
s = [290797]
p = []
distances = []
for i in range(1, k*2):
    s.append((s[i-1]**2) % 50515093)

for i, val in tqdm.tqdm(enumerate(s)):
    try:
        p.append((s[2*i],s[2*i + 1]))
    except:
        pass
    
p.sort()
output = {}
x = np.array([j[0] for j in p])
y = np.array([j[1] for j in p])
for i, coords in tqdm.tqdm(enumerate(p)):
    x1 = x[i:][abs(x[i:] - coords[0]) < 52]
    y1 = y[i:][abs(x[i:] - coords[0]) < 52]
    
    x2 = x1[abs(y1 - coords[1]) < 52]
    y2 = y1[abs(y1 - coords[1]) < 52]

    p1 = [(i, y2[list(x2).index(i)]) for i in x2]

    if len(p1) == 1:
        continue

    for j, other_coords in enumerate(p1):
        delta_x = np.array(coords[0] - other_coords[0], dtype='int64')**2
        delta_y = np.array(coords[1] - other_coords[1], dtype='int64')**2
        dist = math.sqrt(delta_x + delta_y)
        distances.append(dist)

open('distances_2mil.txt','w').close()
with open('distances_2mil.txt', 'a') as f:
    for dist in distances:
        f.write(f'{dist}\n')
    
print(min(distances))
