# %%
# Part 1
file = "./input.txt"
with open(file) as f:
    heights = f.read().splitlines()
i_max = len(heights)
j_max = len(heights[0])
count = 0

for i in range(i_max):
    for j in range(j_max):
        left = None
        right = None
        up = None
        down = None

        if i == 0:
            up = True
        else:
            up = all(heights[i][j] > heights[t][j] for t in range(i))

        if i == i_max - 1:
            down = True
        else:
            down = all(heights[i][j] > heights[t][j] for t in range(i + 1, i_max))

        if j == 0:
            left = True
        else:
            left = all(heights[i][j] > heights[i][t] for t in range(j))

        if j == j_max - 1:
            right = True
        else:
            right = all(heights[i][j] > heights[i][t] for t in range(j + 1, j_max))

        final_visibility = left or right or up or down
        if final_visibility:
            count += 1
print(count)
# %%
file = "./input.txt"
with open(file) as f:
    heights = f.read().splitlines()
i_max = len(heights)
j_max = len(heights[0])
best_score = 0
for i in range(i_max):
    for j in range(j_max):
        left = 0
        right = 0
        up = 0
        down = 0

        if i > 0:
            for t in range(i - 1, -1, -1):
                if heights[i][j] > heights[t][j]:
                    up += 1
                else:
                    up += 1
                    break

        if i < i_max - 1:
            for t in range(i + 1, i_max):
                if heights[i][j] > heights[t][j]:
                    down += 1
                else:
                    down += 1
                    break

        if j > 0:
            for t in range(j - 1, -1, -1):
                if heights[i][j] > heights[i][t]:
                    left += 1
                else:
                    left += 1
                    break

        if j < j_max - 1:
            for t in range(j + 1, j_max):
                if heights[i][j] > heights[i][t]:
                    right += 1
                else:
                    right += 1
                    break

        score = left * right * up * down
        if score > best_score:
            best_score = score
print(best_score)
# %%
