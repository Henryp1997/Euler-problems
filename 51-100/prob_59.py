import sys

sys.set_int_max_str_digits(5000)

# look for the word 'the' or 'and' in the encrypted message
# this will be present probably quite a few times, and can be foud by checking for repeated triplets

with open('0059_cipher.txt', 'r') as f:
    values = [int(i) for i in f.readlines()[0].split(",")]

triplets = []
for i, val in enumerate(values):
    try:
        triplets.append((val, values[i+1], values[i+2]))
    except:
        pass

triplets_filtered = []
for triplet in triplets:
    if triplet in triplets_filtered:
        continue
    triplets_filtered.append((triplet, triplets.count(triplet)))

possible_the = max(triplets_filtered, key=lambda x: x[1])[0]

t = str(ord('t')); h = str(ord('h')); e = str(ord('e'))
a = str(ord('a')); n = str(ord('n')); d = str(ord('d'))

# enc key is between aaa and zzz, ord(a) = 97 and ord(z) = 122, so enc key is between 97, 97, 97 and 122, 122, 122
# this key is repeated to match the length of the encrypted message though
# length of message is 1455 characters so the key must be repeated 1455 / 3 = 485 times

# find locations of possible 'the' or 'and' words
the_and_locs = []
for i, val in enumerate(values):
    try:
        if (val, values[i + 1], values[i + 2]) == possible_the:
            the_and_locs.append(i)
    except:
        pass

# generate all possible keys
keys = []
for i in range(97, 123):
    for j in range(97, 123):
        for k in range(97, 123):
            key = "".join([str(i), str(j), str(k)]*485)
            keys.append(key)

for key in keys:
    enc_message = [bin(i) for i in values]
    print(enc_message)
    # message = int(key) ^ int(enc_message)
    # print(message)