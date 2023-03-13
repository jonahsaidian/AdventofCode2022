# %%
# Part 1
wins = ("A Y", "B Z", "C X")
losses = ("A Z", "B X", "C Y")
draws = ("A X", "B Y", "C Z")
points = {"X": 1, "Y": 2, "Z": 3}

file = "./input.txt"
with open(file) as f:
    score = 0
    for row in f:
        row = row.rstrip()
        if row in wins:
            score += 6
        elif row in draws:
            score += 3
        score += points[row[-1]]
print(score)
# %%
# Part 2
end = {"X": 0, "Y": 3, "Z": 6}
rocks = ("A Y", "B X", "C Z")
papers = ("A Z", "B Y", "C X")
scissors = ("A X", "B Z", "C Y")

file = "./input.txt"
with open(file) as f:
    score = 0
    for row in f:
        row = row.rstrip()
        if row in rocks:
            score += 1
        elif row in papers:
            score += 2
        elif row in scissors:
            score += 3
        score += end[row[-1]]
print(score)
