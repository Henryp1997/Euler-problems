a = [1, 1]
b = []
for i in range(2, 100):
    x = a[i - 1] + a[i - 2]
    if x > 4_000_000:
        break
    a.append(x)
    if x % 2 == 0:
        b.append(x)
print(sum(b))