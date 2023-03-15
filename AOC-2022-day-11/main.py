# %%

# Part 1
class Monkey:
    def __init__(self, items, operation, test, targets):
        self.items = items
        self.operation = operation
        self.test = test
        self.targets = targets
        self.inspections = 0

    def turn(self):
        while self.items:
            item = int(self.items.pop(0))
            item = eval(self.operation, {"old": item})
            item = int(item / 3)
            test_result = eval(self.test, {"x": item})
            target = self.targets[test_result]
            self.throw(item, target)
            self.inspections += 1

    def add_item(self, item):
        self.items.append(item)

    def throw(self, item, target):
        monkey_list[target].add_item(item)


file = "./input.txt"
monkey_list = {}
monkey_id = None
items = None
operation = None
test = None
true_target = None
false_target = None

with open(file) as f:
    for row in f:
        row = row.rstrip()
        if "Monkey" in row:
            monkey_id = row.split(" ")[1][:-1]
        if "Starting items" in row and monkey_id:
            items = row.split(": ")[-1].split(", ")
        if "Operation" in row:
            operation = row.split("= ")[-1]
        if "Test" in row:
            if "divisible by" in row:
                n = row.split(" ")[-1]
                test = f"bool(not x%{n})"
            else:
                raise ValueError()
        if "If true" in row:
            true_target = row.split(" ")[-1]
        if "If false" in row:
            false_target = row.split(" ")[-1]
        if monkey_id and items and operation and test and true_target and false_target:
            monkey_list[monkey_id] = Monkey(
                items, operation, test, {True: true_target, False: false_target}
            )

            monkey_id = None
            items = None
            operation = None
            test = None
            true_target = None
            false_target = None

n_rounds = 20
while n_rounds > 0:
    for id, monkey in monkey_list.items():
        monkey.turn()
    n_rounds -= 1
else:
    first = (0, 0)
    second = (0, 0)
    for id, monkey in monkey_list.items():
        if monkey.inspections > first[1]:
            second = first
            first = (id, monkey.inspections)
        elif monkey.inspections > second[1]:
            second = (id, monkey.inspections)
    print(first[1] * second[1])
# %%

# Part 2
class Monkey:
    def __init__(self, items, operation, test, targets):
        self.items = items
        self.operation = operation
        self.test = test
        self.targets = targets
        self.inspections = 0

    def turn(self):
        while self.items:
            item = int(self.items.pop(0))
            item = eval(self.operation, {"old": item})
            # item = int(item /3)
            test_result = eval(self.test, {"x": item})
            target = self.targets[test_result]
            self.throw(item, target)
            self.inspections += 1

    def add_item(self, item):
        self.items.append(item)

    def throw(self, item, target):
        monkey_list[target].add_item(item)


file = "./input.txt"
monkey_list = {}
divisor_list = []
monkey_id = None
items = None
operation = None
test = None
true_target = None
false_target = None

with open(file) as f:
    for row in f:
        row = row.rstrip()
        if "Monkey" in row:
            monkey_id = row.split(" ")[1][:-1]
        if "Starting items" in row and monkey_id:
            items = row.split(": ")[-1].split(", ")
        if "Operation" in row:
            operation = row.split("= ")[-1]
        if "Test" in row:
            if "divisible by" in row:
                n = row.split(" ")[-1]
                divisor_list.append(n)
                test = f"bool(not x%{n})"
            else:
                raise ValueError()
        if "If true" in row:
            true_target = row.split(" ")[-1]
        if "If false" in row:
            false_target = row.split(" ")[-1]
        if monkey_id and items and operation and test and true_target and false_target:
            monkey_list[monkey_id] = Monkey(
                items, operation, test, {True: true_target, False: false_target}
            )

            monkey_id = None
            items = None
            operation = None
            test = None
            true_target = None
            false_target = None

lcm = 1
for i in divisor_list:
    lcm *= int(i)

n_rounds = 10000
while n_rounds > 0:
    for id, monkey in monkey_list.items():
        monkey.turn()
    n_rounds -= 1
    for monkey in monkey_list.values():
        new_list = []
        for item in monkey.items:
            new_list.append(item % lcm)
        monkey.items = new_list
else:
    first = (0, 0)
    second = (0, 0)
    for id, monkey in monkey_list.items():
        if monkey.inspections > first[1]:
            second = first
            first = (id, monkey.inspections)
        elif monkey.inspections > second[1]:
            second = (id, monkey.inspections)
    print(first[1] * second[1])
# %%
