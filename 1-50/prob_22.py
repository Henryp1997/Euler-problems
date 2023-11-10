def compare_names(name1, name2):
    if len(name1) <= len(name2):
        length = len(name1)
    else:
        length = len(name2)
    
    for i in range(length):
        if ord(name1[i]) < ord(name2[i]):
            result = name1
            break
        elif ord(name1[i]) > ord(name2[i]):
            result = name2
            break
    return result

with open('0022_names.txt', 'r') as f:
    names = f.readlines()

names = [i.strip('"') for i in names[0].split(",")]

names.sort()

names_sorted = []
for i, name in enumerate(names):
    names_sorted.append(name)
    if len(names_sorted) == 1:
        continue
    alpha_result = compare_names(name, names_sorted[i - 1])
    
    names_sorted[i] = name if alpha_result != name else names_sorted[i - 1]
    names_sorted[i - 1] = names_sorted[i - 1] if alpha_result != name else name

    break

total = 0
for i, name in enumerate(names):
    total += (i + 1) * sum([ord(i) - 64 for i in name])

print(total)