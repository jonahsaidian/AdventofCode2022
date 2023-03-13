# %%
# Part 1
file = "./input.txt"
with open(file) as f:
    stream = f.readline().rstrip()
    for i in range(len(stream)):
        s = set(stream[i : i + 4])
        if len(s) == 4:
            print(i + 4)
            break

# %%
# Part 2
file = "./input.txt"
with open(file) as f:
    stream = f.readline().rstrip()
    for i in range(len(stream)):
        s = set(stream[i : i + 14])
        if len(s) == 14:
            print(i + 14)
            break
