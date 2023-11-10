import itertools

lst = list(range(1, 11))

perms = list(itertools.permutations(lst))

perms = [i for i in perms if i[0] == 10]

solutions = []
results = []
for perm in perms:
    a, b, c, d, e, f, g, h, i, j = perm
    X = a + b + c
    if d + c + e != X:
        continue
    if f + e + g != X:
        continue
    if h + g + i != X:
        continue
    if j + i + b != X:
        continue
    solution = [a, b, c, d, c, e, f, e, g, h, g, i, j, i, b]
    min_outer_val = min([j for i, j in enumerate(solution) if i % 3 == 0])
    locs_min_val = []
    for i, val in enumerate(solution):
        if i % 3 == 0 and val == min_outer_val:
            locs_min_val.append(i)
    results.append(int("".join([str(i) for i in solution[locs_min_val[0]:] + solution[:locs_min_val[0]]])))

print(max(results))