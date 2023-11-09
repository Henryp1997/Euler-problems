max_power = 0
while True:
    if max_power > len(str(9**max_power)):
        break
    max_power += 1

# generate all (2, 9)^power for powers up to max_power - 1
count = 0
for power in range(1, max_power):
    for i in range(2, 10):
        if len(str(i**power)) == power:
            count += 1

# 1 is also an answer
print(count + 1)