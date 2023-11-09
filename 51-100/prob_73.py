import sys
# %%
def get_hcf(a, b):
    hcf = 1
    for i in range(int(b/2), 0, -1):
        if b % i == 0 and a % i == 0:
            hcf = i
            break
    return hcf
d = 5
fracs = []
for n in range(1, d):
    for m in range(n + 1, d + 1):
        if m % n == 0:
            fracs.append(f'1/{int(m / n)}')
            continue
        hcf = None
        hcf = get_hcf(m, n)
        fracs.append(f'{int(n / hcf)}/{int(m / hcf)}')

fracs = list(set(fracs)) # remove duplicates

fracs.sort(key=lambda x: int(x.split("/")[0]) / int(x.split("/")[1]))
numes = [int(i.split("/")[0]) for i in fracs]
denoms = [int(i.split("/")[1]) for i in fracs]

idx_1 = fracs.index('1/3')
idx_2 = fracs.index('1/2')

print(fracs[idx_1: idx_2 + 1])
print(fracs[idx_1: idx_2 + 1])

print(get_hcf(10, 20))

#%%
def get_hcf(a, b):
    hcf = 1
    for i in range(int(b/2), 0, -1):
        if b % i == 0 and a % i == 0:
            hcf = i
            break
    return hcf

fracs = ['1/3', '1/2']
for d in range(5, 12001):
    with open('test.txt', 'w') as f:
        f.write(f'{d}')
    f.close()
    for i, frac in enumerate(fracs):
        try:
            vals = frac.split("/")
            vals_next = fracs[i + 1].split("/")
            if int(vals[1]) + int(vals_next[1]) == d:
                numerator = int(vals[0]) + int(vals_next[0])
                current = f"{numerator}/{d}"
                if current not in fracs:
                    fracs = fracs[:i+1] + [current] + fracs[i+1:]
                break
        except:
            pass

new_fracs = []
for frac in fracs:
    numerator = int(frac.split("/")[0])
    denominator = int(frac.split("/")[1])
    hcf = get_hcf(numerator, denominator)
    frac = f'{int(numerator / hcf)}/{int(denominator / hcf)}'
    if frac not in new_fracs:
        new_fracs.append(frac)

new_fracs = list(set(new_fracs))

new_fracs.sort(key=lambda x: int(x.split("/")[0]) / int(x.split("/")[1]))

print(len(new_fracs) - 2)
# %%
