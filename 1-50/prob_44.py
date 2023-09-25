import math

p = [1]
current_offset = 4
for i in range(1, 10000):
    p.append(i + current_offset)
    current_offset += (i+1)*3

# for pk in p:
#     if math.sqrt(48 * pk) % 1 == 0:
#         print(pk, p.index(pk)+1)

break_outer_loop = False
i = 0
while True:
    for j in range(1, i):
        delta = p[i] - p[j]
        if math.sqrt(1 + (24 * delta)) % 6 == 5:
            print(delta)
            break_outer_loop = True
            break
    if break_outer_loop:
        break
    i += 1
