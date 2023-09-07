import math, random, itertools

n = '123456789'

iterations = list(itertools.permutations(list(n)))

iterations = [i for i in iterations if i[-1] not in ('2', '4', '6', '8', '5')]

numbers = [str(i)]
