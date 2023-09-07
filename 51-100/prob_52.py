i = 1

while True:
    yes = 0
    for multiplier in [2, 3, 4, 5, 6]:
        if "".join(sorted(str(multiplier * i))) == "".join(sorted(str(i))):
            yes += 1
    if yes == 5:
        print(i)
        break
    i += 1