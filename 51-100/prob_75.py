import math

squares = [n**2 for n in range(1, 10000)]

triples = []
for square in squares:
    for other_square in squares:
        if (square + other_square) in squares:
            a = int(math.sqrt(square)); b = int(math.sqrt(other_square)); c = int(math.sqrt(square + other_square))
            if (b, a, c) not in triples:
                triples.append((a, b, c))

print(triples)