with open('13.txt', 'r') as f:
    lines = f.readlines()

nums = [int(i.split("\n")[0]) for i in lines]

print(str(sum(nums))[:10])