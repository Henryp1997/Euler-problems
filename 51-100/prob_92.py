#%%
def check_89(n, ones):
    n = "".join([i for i in str(n) if i != '0'])
    while True:
        if (n := digit_sum(n)) == '89':
            return 89
        elif n == '1' or int(n) in ones:
            return 1

def digit_sum(n):
    return str(sum([int(j)**2 for j in str(n)]))

n_89 = 0
ones = []
squared_sum_results = []
for i in range(1, 10_000_000):
    if check_89(i, ones) == 1:
        ones.append(i)
        continue
    n_89 += 1

# print(n_89)
# %%
