d = 1_000_000

def get_hcf(a, b):
    for i in range(int(b/2), 0, -1):
        if b % i == 0 and a % i == 0:
            hcf = i
            break
    return hcf

fracs = []
for n in range(1, d):
    for m in range(n + 1, d + 1):
        if m % n == 0:
            fracs.append(f'1/{int(m / n)}')
            continue
        hcf = None
        for i in range(int(m/2), 0, -1):
            if m % i == 0 and n % i == 0:
                hcf = i
                break
        fracs.append(f'{int(n / hcf)}/{int(m / hcf)}')

fracs = list(set(fracs)) # remove duplicates

fracs.sort(key=lambda x: int(x.split("/")[0]) / int(x.split("/")[1]))

print(fracs)

# print(get_hcf(3, 8))