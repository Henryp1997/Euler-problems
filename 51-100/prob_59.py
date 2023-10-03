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

t = ord('t'); h = ord('h'); e = ord('e')
a = ord('a'); n = ord('n'); d = ord('d')
f = ord('f'); o = ord('o'); r = ord('r')

# enc key is between aaa and zzz, ord(a) = 97 and ord(z) = 122, so enc key is between 97, 97, 97 and 122, 122, 122
# this key is repeated to match the length of the encrypted message though
# length of message is 1455 characters so the key must be repeated 1455 / 3 = 485 times

for triplet in triplets_filtered:
    # find locations of possible 'the' or 'and' words
    the_and_locs = []
    for i, val in enumerate(values):
        try:
            if (val, values[i + 1], values[i + 2]) == triplet[0]:
                the_and_locs.append(i)
        except:
            pass

    x, y, z = values[the_and_locs[0]], values[the_and_locs[0] + 1], values[the_and_locs[0] + 2]
    possible_key = [str(e ^ z), str(t ^ x), str(h ^ y)]*485
    new_values = []
    for i, val in enumerate(values):
        character = val ^ int(possible_key[i])
        new_values.append(character)


    message_the = "".join([chr(i) for i in new_values])
    if 'and' in message_the:
        print()
        print(message_the)
        print()
        print(f'key = \'{"".join([chr(int(i)) for i in possible_key[:3]])}\'')
        print()
        print(sum([ord(i) for i in message_the]))
        break
            