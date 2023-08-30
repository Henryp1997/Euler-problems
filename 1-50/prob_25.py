f = [1, 1]

while True:
    i = f[-2] + f[-1]
    f.append(i)
    if len(str(i)) == 1000:
        break

print(len(f))