# %%
# Part 1
file = "./input.txt"
head_pos = (0, 0)
tail_pos = (0, 0)
visitations = set()


def update_tail():
    global head_pos
    global tail_pos
    global visitations

    delta = (head_pos[0] - tail_pos[0], head_pos[1] - tail_pos[1])
    if (
        abs(delta[0]) > 1
        and abs(delta[1]) > 0
        or abs(delta[0]) > 0
        and abs(delta[1]) > 1
    ):
        tail_pos = (
            tail_pos[0] + delta[0] / abs(delta[0]),
            tail_pos[1] + delta[1] / abs(delta[1]),
        )
        update_tail()
    elif abs(delta[0]) > 1:
        tail_pos = (tail_pos[0] + delta[0] / abs(delta[0]), tail_pos[1])
        update_tail()
    elif abs(delta[1]) > 1:
        tail_pos = (tail_pos[0], tail_pos[1] + delta[1] / abs(delta[1]))
        update_tail()
    visitations.add(tail_pos)


with open(file) as f:
    for row in f:
        row = row.rstrip()
        direction, step = row.split(" ")
        step = int(step)
        update_tail()
        if direction == "L":
            for i in range(step):
                head_pos = (head_pos[0] - 1, head_pos[1])
                update_tail()
        elif direction == "R":
            for i in range(step):
                head_pos = (head_pos[0] + 1, head_pos[1])
                update_tail()
        elif direction == "U":
            for i in range(step):
                head_pos = (head_pos[0], head_pos[1] + 1)
                update_tail()
        elif direction == "D":
            for i in range(step):
                head_pos = (head_pos[0], head_pos[1] - 1)
                update_tail()
print(len(visitations))

# %%
# Part 1
file = "./input.txt"
num_knots = 9
positions = {}
for i in range(num_knots + 1):
    positions[i] = (0, 0)
visitations = set()


def update_tail():
    global positions
    global visitations

    for i in range(num_knots):
        delta = (
            positions[i][0] - positions[i + 1][0],
            positions[i][1] - positions[i + 1][1],
        )
        if (
            abs(delta[0]) > 1
            and abs(delta[1]) > 0
            or abs(delta[0]) > 0
            and abs(delta[1]) > 1
        ):
            positions[i + 1] = (
                positions[i + 1][0] + delta[0] / abs(delta[0]),
                positions[i + 1][1] + delta[1] / abs(delta[1]),
            )
            update_tail()
        elif abs(delta[0]) > 1:
            positions[i + 1] = (
                positions[i + 1][0] + delta[0] / abs(delta[0]),
                positions[i + 1][1],
            )
            update_tail()
        elif abs(delta[1]) > 1:
            positions[i + 1] = (
                positions[i + 1][0],
                positions[i + 1][1] + delta[1] / abs(delta[1]),
            )
            update_tail()
        visitations.add(positions[num_knots])


with open(file) as f:
    for row in f:
        row = row.rstrip()
        direction, step = row.split(" ")
        step = int(step)
        update_tail()
        if direction == "L":
            for i in range(step):
                positions[0] = (positions[0][0] - 1, positions[0][1])
                update_tail()
        elif direction == "R":
            for i in range(step):
                positions[0] = (positions[0][0] + 1, positions[0][1])
                update_tail()
        elif direction == "U":
            for i in range(step):
                positions[0] = (positions[0][0], positions[0][1] + 1)
                update_tail()
        elif direction == "D":
            for i in range(step):
                positions[0] = (positions[0][0], positions[0][1] - 1)
                update_tail()
print(len(visitations))
# %%
