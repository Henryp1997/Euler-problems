from tqdm import tqdm

results = []

for n in tqdm(range(2, 1_000_000)):
    count = 0
    current_val = n
    while current_val != 1:
        if current_val % 2 == 0:
            current_val /= 2
        else:
            current_val *= 3; current_val += 1
        count += 1
    results.append(count)

print(max(results), results.index(max(results)) + 2)
