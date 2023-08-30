with open('0067.txt', 'r') as f:
    lines = f.readlines()

arr = [[] for i in range(100)]

for i, line in enumerate(lines):
    line = line.strip("\n")
    arr[i] = [int(k) for k in line.split(" ") if k != " "]

for i in range(98, -1, -1):
    temp_arr = []
    for k, j in enumerate(arr[i]):
        result = max([arr[i+1][k] + j, arr[i+1][k+1] + j])
        temp_arr.append(result)

    arr = [lst for lst in arr[:i]] + [temp_arr]

result = arr[0][0]

print(result)
