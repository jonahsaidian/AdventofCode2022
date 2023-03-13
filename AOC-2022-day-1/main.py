# %%
f = "./input.txt"
with open(f) as file:
    sum = 0
    elves = []
    for row in file:
        if row == "\n":
            elves.append(sum)
            sum = 0
        else:
            sum += int(row)

# %%
max(elves)

# %%
elves.sort()
elves[-3] + elves[-2] + elves[-1]
