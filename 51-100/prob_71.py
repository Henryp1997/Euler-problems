import time
time_start = time.time()

nume = 2
denom = 5
target = [3, 7]
for d in range(1, 20):
    if d == (new_denom := target[1] + denom):
        nume, denom = target[0] + nume, new_denom
        print(nume, denom)

print(nume)
print((time.time() - time_start)*1000)