# %%
import string

# %%
alphabet = list(string.ascii_lowercase) + list(string.ascii_uppercase)
priority = {}
for i, letter in enumerate(alphabet):
    priority[letter] = i + 1

# %%
# Part 1
file = "./input.txt"
with open(file) as f:
    score = 0
    for row in f:
        row = row.rstrip()
        l = int(len(row) / 2)
        p1 = row[:l]
        p2 = row[l:]
        letter = list(set(p1).intersection(p2))
        score += priority[letter[0]]
print(score)

# %%
file = "./input.txt"
with open(file) as f:
    score = 0
    group = []
    for row in f:
        row = row.rstrip()
        group.append(row)
        if len(group) == 3:
            letter = list(set(group[0]).intersection(group[1]).intersection(group[2]))
            score += priority[letter[0]]
            group = []
print(score)
