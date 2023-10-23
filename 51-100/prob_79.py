with open('0079_keylog.txt', 'r') as f:
    lines = f.readlines()

logins = [i.split("\n")[0] for i in lines]

logins = list(set(logins))

rank_dict = {f'{i}': 0 for i in range(10) if i not in [4, 5]}
count_dict = {f'{i}': 0 for i in range(10) if i not in [4, 5]}
for l in logins:
    for i in range(3):
        rank_dict[l[i]] += 3 - i
        count_dict[l[i]] += 1

for i in range(10):
    if i not in [4, 5]:
        rank_dict[str(i)] /= count_dict[str(i)]

results = [(list(rank_dict.keys())[i], list(rank_dict.values())[i]) for i in range(len(rank_dict))]
results.sort(key=lambda x: x[1], reverse=True)

print("".join(i[0] for i in results))