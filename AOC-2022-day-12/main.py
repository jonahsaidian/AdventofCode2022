# %%
# Part 1
import string

file = "./input.txt"
with open(file) as f:
    data = f.read().splitlines()
row_max = len(data)
col_max = len(data[0])
heights = {}

for row in range(row_max):
    heights[row] = {}
    for col in range(col_max):
        try:
            heights[row][col] = string.ascii_lowercase.index(data[row][col])
        except:
            pass
    if "S" in data[row]:
        col = data[row].index("S")
        height = string.ascii_lowercase.index("a")
        start = (row, col, height)
        heights[row][col] = height
    if "E" in data[row]:
        col = data[row].index("E")
        height = string.ascii_lowercase.index("z")
        end = (row, col, height)
        heights[row][col] = height

visited = {}
queued = set()
queued.add(start)
distance = 0


def get_available_steps(
    current, heights=heights, visited=visited, row_max=row_max, col_max=col_max
):
    row, col, height = current
    available = []

    if not row == 0:
        step_up = (row - 1, col, heights[row - 1][col])
        if step_up[2] <= height + 1 and step_up not in visited.keys():
            available.append(step_up)
    if not row == row_max - 1:
        step_down = (row + 1, col, heights[row + 1][col])
        if step_down[2] <= height + 1 and step_down not in visited.keys():
            available.append(step_down)
    if not col == 0:
        step_left = (row, col - 1, heights[row][col - 1])
        if step_left[2] <= height + 1 and step_left not in visited.keys():
            available.append(step_left)
    if not col == col_max - 1:
        step_right = (row, col + 1, heights[row][col + 1])
        if step_right[2] <= height + 1 and step_right not in visited.keys():
            available.append(step_right)
    return available


while end not in visited.keys():
    if not queued:
        print("Path not found")
        break
    next_steps = set()
    while queued:
        place = queued.pop()
        visited[place] = distance
        available_steps = get_available_steps(place)
        for next_step in available_steps:
            next_steps.add(next_step)
    distance += 1
    queued = next_steps

else:
    print(f"Path distance to reach the end is {visited[end]}")
# %%
# Part 2
import string

file = "./input.txt"
with open(file) as f:
    data = f.read().splitlines()
row_max = len(data)
col_max = len(data[0])
heights = {}
visited = {}
queued = set()
distance = 0

for row in range(row_max):
    heights[row] = {}
    for col in range(col_max):
        try:
            height = string.ascii_lowercase.index(data[row][col])
            heights[row][col] = height
            if height == 0:
                queued.add((row, col, height))
        except:
            pass
    if "S" in data[row]:
        col = data[row].index("S")
        height = string.ascii_lowercase.index("a")
        start = (row, col, height)
        queued.add(start)
        heights[row][col] = height
    if "E" in data[row]:
        col = data[row].index("E")
        height = string.ascii_lowercase.index("z")
        end = (row, col, height)
        heights[row][col] = height


def get_available_steps(
    current, heights=heights, visited=visited, row_max=row_max, col_max=col_max
):
    row, col, height = current
    available = []

    if not row == 0:
        step_up = (row - 1, col, heights[row - 1][col])
        if step_up[2] <= height + 1 and step_up not in visited.keys():
            available.append(step_up)
    if not row == row_max - 1:
        step_down = (row + 1, col, heights[row + 1][col])
        if step_down[2] <= height + 1 and step_down not in visited.keys():
            available.append(step_down)
    if not col == 0:
        step_left = (row, col - 1, heights[row][col - 1])
        if step_left[2] <= height + 1 and step_left not in visited.keys():
            available.append(step_left)
    if not col == col_max - 1:
        step_right = (row, col + 1, heights[row][col + 1])
        if step_right[2] <= height + 1 and step_right not in visited.keys():
            available.append(step_right)
    return available


while end not in visited.keys():
    if not queued:
        print("Path not found")
        break
    next_steps = set()
    while queued:
        place = queued.pop()
        visited[place] = distance
        available_steps = get_available_steps(place)
        for next_step in available_steps:
            next_steps.add(next_step)
    distance += 1
    queued = next_steps

else:
    print(f"Path distance to reach the end is {visited[end]}")
# %%
