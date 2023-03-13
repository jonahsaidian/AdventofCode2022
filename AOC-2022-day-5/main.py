# %%
# Part 1
n_stacks = 9
file = "./input.txt"
with open(file) as f:
    header = 0
    stack = {}
    raw = []
    count = 0
    for row in f:
        row = row.rstrip()
        if row == "":
            header = 1
            raw.reverse()
            for i in range(len(raw)):
                for j in range(n_stacks):
                    if i ==0:
                        stack[j+1]=[]
                        continue
                    if not raw[i][1+4*j] == ' ':
                        stack[j+1].append(raw[i][1+4*j])
            continue  
        if header == 0:
            raw.append(row)
            
        if header ==1:
            r1,r2 = row.split(' from ')
            r2,r3 = r2.split(' to ')
            _,r1 = r1.split(' ')
            n = int(r1)
            f = int(r2[0])
            t = int(r3[0])
            for i in range(n):
                item = stack[f].pop(-1)
                stack[t].append(item)
            count +=1
s = ''
for i in range(n_stacks):
    s+=stack[i+1][-1]
print(s)

# %%
# Part 2
n_stacks = 9
file = "./input.txt"
with open(file) as f:
    header = 0
    stack = {}
    raw = []
    count = 0
    for row in f:
        row = row.rstrip()
        if row == "":
            header = 1
            raw.reverse()
            for i in range(len(raw)):
                for j in range(n_stacks):
                    if i ==0:
                        stack[j+1]=[]
                        continue
                    if not raw[i][1+4*j] == ' ':
                        stack[j+1].append(raw[i][1+4*j])
            continue  
        if header == 0:
            raw.append(row)
            
        if header ==1:
            r1,r2 = row.split(' from ')
            r2,r3 = r2.split(' to ')
            _,r1 = r1.split(' ')
            n = int(r1)
            f = int(r2[0])
            t = int(r3[0])
            items = stack[f][-n:]
            for item in items:
                stack[f].pop(-1)
                stack[t].append(item)
            count +=1

s = ''
for i in range(n_stacks):
    s+=stack[i+1][-1]
print(s)