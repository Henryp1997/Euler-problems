with open('69_results.txt', 'r') as f:
    lines = f.readlines()

results = [(int(line.split("(")[1].split(",")[0]), float(line.split(")")[0].split(", ")[1])) for line in lines]

results.sort(key=lambda x: x[1])

for i in results[-30:]:
    print(i)