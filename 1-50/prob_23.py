from prob_21 import get_divisors

# abundant_nums = []
# for i in range(1, 28124):
#     if sum(get_divisors(i)) > i:
#         abundant_nums.append(i)
    
# with open('abundant.txt', 'a') as f:
#     for num in abundant_nums:
#         f.write(f'{num}\n')

with open('abundant.txt', 'r') as f:
    nums = f.readlines()

nums = [int(i.strip("\n")) for i in nums]

odd_nums = [i for i in nums if i % 2 == 1]



