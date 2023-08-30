from tqdm import tqdm

p = [0, 1, 2, 3, 5]

for i in tqdm(range(5, 1_000_000)):
    if i % 2 == 1:
        sum = 0
        for j in range(2, int((i + 1)/2)):
            sum += 2 * p[j]
        p.append(3 + sum)
    else:
        sum = 0
        for j in range(2, int(i / 2)):
            sum += 2 * p[j]
        p.append(3 + sum + p[int(i / 2)])
    
    if int(p[i] % 1_000_000) == 0:
        print(i)
        print(p[i])
        break
