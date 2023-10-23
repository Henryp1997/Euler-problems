import math

count = 0
chain_nums = []
chain_lengths = []
for n in range(12, 1_000_000):

    nums_hit = [n]
    while True:
        next_ = sum([math.factorial(int(i)) for i in str(n)])
        if next_ in nums_hit:
            break
        nums_hit.append(next_)
        length = len(nums_hit)
        if next_ in chain_nums:
            length += chain_lengths[chain_nums.index(next_)]
            break
        n = next_
    for i, num in enumerate(nums_hit):
        if num in chain_nums:
            continue
        chain_nums.append(num)
        chain_lengths.append(length - i)
    if len(nums_hit) == 60:
        count += 1

print(count)
