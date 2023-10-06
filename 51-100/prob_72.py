import matplotlib.pyplot as plt

x = []
y = []

for d in range(1, 500):

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

    x.append(d)
    y.append(len(fracs))

with open('out_x.txt', 'a') as f:
    for i in range(len(x)):
        f.write(f'{x[i]}\n')

with open('out_y.txt', 'a') as f:
    for i in range(len(x)):
        f.write(f'{y[i]}\n')

plt.plot(x,y,"kx")
plt.show()
