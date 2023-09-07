with open('0042_words.txt', 'r') as f:
    words = [i.strip('"') for i in f.readlines()[0].split(",")]

longest = ''
for word in words:
    if len(word) > len(longest):
        longest = word
    
length_longest = len(longest)
max_possible_val = 26 * length_longest

# get all triangle numbers up to the maximum possible (bounded by length of longest word in file)
tri_nums = []
for n in range(1, 100):
    tri_num = 0.5*n*(n+1)
    tri_nums.append(int(tri_num))
    if tri_num > max_possible_val:
        break

count = 0
for word in words:
    val_of_word = sum([int(ord(c)) - 64 for c in word])
    if val_of_word in tri_nums:
        count += 1

print(count)