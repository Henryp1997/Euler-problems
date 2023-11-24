import math

count = 0
chains = {}
for n in range(1, 1_000_000):

    nums_hit = [n]
    i = 0
    while True:

        next_ = sum([math.factorial(int(i)) for i in str(nums_hit[i])])
        if next_ in nums_hit:
            length = len(nums_hit)
            break

        nums_hit.append(next_)
        length = len(nums_hit)
        try:
            # length += chains[next_] - 1
            nums_hit += chains[next_][1:]
            if nums_hit[0] == nums_hit[-1]:
                nums_hit = nums_hit[:-1]
            break
        except:
            pass

        i += 1

    for i, num in enumerate(nums_hit):
        # chains[num] = length - i
        chains[num] = nums_hit[i:]

for key in list(chains.keys()):
    # if chains[key] == 60:
    #     count += 1
    if len(chains[key]) == 60:
        count += 1

print(count)
