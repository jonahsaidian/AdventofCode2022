# %%
# Part 1
file = "./input.txt"
max_dir_size = 100000
path = []
dirs = dict()
listing = False
with open(file) as f:
    for row in f:
        row = row.rstrip()
        row = row.split(" ")
        if row[0] == "$":
            if row[1] == "ls":
                pass
            elif row[1] == "cd":
                if row[2] == "..":
                    path.pop()
                else:
                    new_dir = row[-1]
                    path.append(new_dir)
                    dir_path = "/".join(path)
                    if dir_path not in dirs.keys():
                        dirs[dir_path] = 0
        elif row[0] == "dir":
            pass
        else:
            size = row[0]
            file_name = row[1]
            for i, p in enumerate(path):
                cur_path = "/".join(path[: i + 1])
                dirs[cur_path] += int(size)

sub_size = 0
for dir in dirs.keys():
    if dirs[dir] <= max_dir_size:
        sub_size += dirs[dir]
print(sub_size)
# %%
# Part 2
file = "./input.txt"
total_size = 70000000
free_size_needed = 30000000
path = []
dirs = dict()
listing = False
with open(file) as f:
    for row in f:
        row = row.rstrip()
        row = row.split(" ")
        if row[0] == "$":
            if row[1] == "ls":
                pass
            elif row[1] == "cd":
                if row[2] == "..":
                    path.pop()
                else:
                    new_dir = row[-1]
                    path.append(new_dir)
                    dir_path = "/".join(path)
                    if dir_path not in dirs.keys():
                        dirs[dir_path] = 0
        elif row[0] == "dir":
            pass
        else:
            size = row[0]
            file_name = row[1]
            for i, p in enumerate(path):
                cur_path = "/".join(path[: i + 1])
                dirs[cur_path] += int(size)

free_space = total_size - dirs["/"]
difference = free_size_needed - free_space
smallest_dir = ("/", total_size)
for dir in dirs.keys():
    if dirs[dir] >= difference and dirs[dir] < smallest_dir[1]:
        smallest_dir = (dir, dirs[dir])
print(smallest_dir[1])
# %%
