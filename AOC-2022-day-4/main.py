# %%
# Part 1
file = "./input.txt"
with open(file) as f:
    score = 0
    for row in f:
        row = row.rstrip()
        g1, g2 = row.split(",")
        g1l, g1u = g1.split("-")
        g2l, g2u = g2.split("-")
        g1 = set(range(int(g1l), int(g1u) + 1))
        g2 = set(range(int(g2l), int(g2u) + 1))
        if g1.issubset(g2) or g2.issubset(g1):
            score += 1
print(score)

# %%
# Part 2
file = "./input.txt"
with open(file) as f:
    score = 0
    for row in f:
        row = row.rstrip()
        g1, g2 = row.split(",")
        g1l, g1u = g1.split("-")
        g2l, g2u = g2.split("-")
        g1 = set(range(int(g1l), int(g1u) + 1))
        g2 = set(range(int(g2l), int(g2u) + 1))
        if g1.intersection(g2):
            score += 1
score
