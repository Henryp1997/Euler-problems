#%%
def check_89(n, results):
    while True:
        n = str(n)
        if (n := digit_sum(n)) == 89:
            return True
        elif n == 1:
            return False
        elif n in results:
            return False

def digit_sum(n):
    return sum([int(j)**2 for j in str(n)])

print(check_89(49, []))

n_89 = 0
results = []
squared_sum_results = []
for i in range(1, 10_000_000):
    if not check_89(i, results):
        results.append(i)
        continue
    n_89 += 1

print(n_89)
# %%
