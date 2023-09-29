final_result = []

cubes = {}
for n in range(10000):
    cube_ = [i for i in str(n ** 3)]
    cube_.sort()
    cube_ = "".join(cube_)
    if cube_ not in list(cubes.keys()):
        cubes[cube_] = 1
        continue
    cubes[cube_] += 1
    if cubes[cube_] == 5:
        # result variable is one of the integers which when cubed 
        # gives a number which can be permuted to give 4 other cubes
        # now need to find what the smallest cube is out of these 5
        result = n
        cube_sorted = cube_
        for a in range(result):
            cube_other = [i for i in str(a ** 3)]
            cube_other.sort()
            cube_other = "".join(cube_other)
            if cube_other == cube_:
                final_result.append(a ** 3)
        break

print(min(final_result))