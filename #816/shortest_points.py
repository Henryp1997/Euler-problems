import math
import tqdm
import matplotlib.pyplot as plt
import time
import numpy as np
import json

x_locs = []
y_locs = []
# for i in range(1,100):
# ks = [0]
# results = [100000000]
# for n, k in enumerate(np.arange(0,100000,500)):
    # if k == 0:
        # continue
    # ks.append(k)
k = 2000000
s = [290797]
x = []
y = []
p = []
locs = []
distances = []
for i in range(1, k*2):
    s.append((s[i-1]**2) % 50515093)

for i, val in tqdm.tqdm(enumerate(s)):
    try:
        x.append(s[2*i])
        y.append(s[2*i + 1])
        p.append((s[2*i],s[2*i + 1]))
    except:
        pass
# print(p)
p.sort()
# print(p)
output = {}
# open('output.json','w').close()
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
    #     output[f'{i}'] = str(p1)
    #     with open('output.json','a') as f:
    #         json.dump(output, f)

    for j, other_coords in enumerate(p1):
        delta_x = np.array(coords[0] - other_coords[0], dtype='int64')**2
        # if delta_x == 0:
        #     continue
        delta_y = np.array(coords[1] - other_coords[1], dtype='int64')**2
        dist = math.sqrt(delta_x + delta_y)
        distances.append(dist)

open('distances_2mil.txt','w').close()
with open('distances_2mil.txt', 'a') as f:
    for dist in distances:
        f.write(f'{dist}\n')
    
print(min(distances))

# open('shortest_points.txt',"w").close()
# with open('shortest_points.txt', "a") as f:
#     for n, i in enumerate(ks[1:]):
#         f.write(f'{i}, {results[n]}\n')

# plt.plot(ks[1:],results[1:],"kx")
# plt.show()

# # print()
# # all_mins = []
# # d0 = min(distances)
# # print(math.sqrt(d0))
# if len(s) == len(set(s)):
#     print("yes")

# plt.plot(x,"kx")
# plt.show()

# ks.append(k)
# results.append(math.sqrt(d0))

# plt.plot(ks,results,"kx")
# plt.show()
# x0 = locs[distances.index(d0)][0]
# y0 = locs[distances.index(d0)][1]
# x01 = locs[distances.index(d0)][2]
# y01 = locs[distances.index(d0)][3]
# distances[distances.index(d0)] = 1e15
# print(x0,y0,x01,y01)
# all_mins.append(d0)

# d1 = min(distances)
# distances[distances.index(d1)] = 1e15

# d2 = min(distances)
# x2 = locs[distances.index(d2)][0]
# y2 = locs[distances.index(d2)][1]
# x21 = locs[distances.index(d2)][2]
# y21 = locs[distances.index(d2)][3]
# distances[distances.index(d2)] = 1e15
# print(x2,y2,x21,y21)
# all_mins.append(d2)

# d3 = min(distances)
# distances[distances.index(d3)] = 1e15

# d4 = min(distances)
# x4 = locs[distances.index(d4)][0]
# y4 = locs[distances.index(d4)][1]
# x41 = locs[distances.index(d4)][2]
# y41 = locs[distances.index(d4)][3]
# distances[distances.index(d4)] = 1e15
# print(x4,y4,x41,y41)
# all_mins.append(d4)

# d5 = min(distances)
# distances[distances.index(d5)] = 1e15

# d5 = min(distances)
# x5 = locs[distances.index(d5)][0]
# y5 = locs[distances.index(d5)][1]
# x51 = locs[distances.index(d5)][2]
# y51 = locs[distances.index(d5)][3]
# distances[distances.index(d5)] = 1e15
# print(x5,y5,x51,y51)
# all_mins.append(d5)

# d6 = min(distances)
# distances[distances.index(d6)] = 1e15

# final = [math.sqrt(d) for d in all_mins]

# print()
# print(final)
# print(x1,y1)

# plt.plot(x,y,"kx")
# plt.show()