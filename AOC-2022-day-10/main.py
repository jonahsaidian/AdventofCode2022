# %%
# Part 1
file = "./input.txt"
x = {}
x[0] = 1
i = 0
selection = [20, 60, 100, 140, 180, 220]
sum = 0

with open(file) as f:
    for row in f:
        row = row.rstrip()
        row = row.split(" ")

        if row[0] == "noop":
            i += 1
            x[i] = x[i - 1]
            if i in selection:
                sum += x[i] * i
        elif row[0] == "addx":
            i += 1
            x[i] = x[i - 1]
            if i in selection:
                sum += x[i] * i
            i += 1
            x[i] = x[i - 1]
            if i in selection:
                sum += x[i] * i
            x[i] += int(row[1])
print(sum)

# %%
# %%
# Part 2
file = "./input.txt"
x = {}
x[0] = 1
lit = {}
i = 0

with open(file) as f:
    for row in f:
        row = row.rstrip()
        row = row.split(" ")

        if row[0] == "noop":
            i += 1
            x[i] = x[i - 1]
            if i % 40 == 0:
                r = 40
            else:
                r = i % 40
            lit[i] = r in range(x[i], x[i] + 3)
        elif row[0] == "addx":
            i += 1
            x[i] = x[i - 1]
            if i % 40 == 0:
                r = 40
            else:
                r = i % 40
            lit[i] = r in range(x[i], x[i] + 3)
            i += 1
            x[i] = x[i - 1]
            if i % 40 == 0:
                r = 40
            else:
                r = i % 40
            lit[i] = r in range(x[i], x[i] + 3)
            x[i] += int(row[1])
result = []
for row in range(6):
    sub_row = []
    for pos in range(1, 41):
        i = row * 40 + pos
        if lit[i]:
            sub_row.append("#")
        else:
            sub_row.append(".")
    result.append(sub_row)
    print(sub_row)

# %%
