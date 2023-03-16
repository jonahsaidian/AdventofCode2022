# %%
# Part 1
import ast

file = "./input.txt"
with open(file) as f:
    data = f.read().splitlines()
packets = {}
for i in range(1, round(len(data) / 3 + 1)):
    packets[i] = {}
    left_index = (i - 1) * 3
    right_index = left_index + 1
    packets[i]["left"] = ast.literal_eval(data[left_index])
    packets[i]["right"] = ast.literal_eval(data[right_index])


def compare_packet(left, right):
    r = 0
    l = 0
    l_max = len(left)
    r_max = len(right)
    ordered = None
    done = False
    while not done:
        if l == l_max and r == r_max:
            ordered, done = [None, False]
            return [None, False]
        if (not left) or l >= l_max:
            ordered, done = [True, True]
            return [True, True]
        if (not right) or r >= r_max:
            ordered, done = [False, True]
            return [False, True]
        if type(left[l]) == list and type(right[r]) == list:
            ordered, done = compare_packet(left[l], right[r])
            l += 1
            r += 1
            continue
        elif type(left[l]) == list and type(right[r]) == int:
            ordered, done = compare_packet(left[l], [right[r]])
            l += 1
            r += 1
            continue
        elif type(left[l]) == int and type(right[r]) == list:
            ordered, done = compare_packet([left[l]], right[r])
            l += 1
            r += 1
            continue
        elif type(left[l]) == int and type(right[r]) == int:
            if left[l] < right[r]:
                return [True, True]
            elif left[l] > right[r]:
                return [False, True]
            else:
                l += 1
                r += 1
                continue
        else:
            pass
    else:
        return [ordered, done]


total = 0
for index, packet in packets.items():
    if compare_packet(packet["left"], packet["right"])[0]:
        print(index)
        total += index
print(total)
# %%
# Part 2
import ast

file = "./input.txt"
with open(file) as f:
    data = f.read().splitlines()
initial_packet_0 = [[2]]
initial_packet_1 = [[6]]
sorted_packets = [initial_packet_0, initial_packet_1]


def compare_packet(left, right):
    r = 0
    l = 0
    l_max = len(left)
    r_max = len(right)
    ordered = None
    done = False
    while not done:
        if l == l_max and r == r_max:
            ordered, done = [None, False]
            return [None, False]
        if (not left) or l >= l_max:
            ordered, done = [True, True]
            return [True, True]
        if (not right) or r >= r_max:
            ordered, done = [False, True]
            return [False, True]
        if type(left[l]) == list and type(right[r]) == list:
            ordered, done = compare_packet(left[l], right[r])
            l += 1
            r += 1
            continue
        elif type(left[l]) == list and type(right[r]) == int:
            ordered, done = compare_packet(left[l], [right[r]])
            l += 1
            r += 1
            continue
        elif type(left[l]) == int and type(right[r]) == list:
            ordered, done = compare_packet([left[l]], right[r])
            l += 1
            r += 1
            continue
        elif type(left[l]) == int and type(right[r]) == int:
            if left[l] < right[r]:
                return [True, True]
            elif left[l] > right[r]:
                return [False, True]
            else:
                l += 1
                r += 1
                continue
        else:
            pass
    else:
        return [ordered, done]


def sort_packet(packet, sorted_packets):
    length = len(sorted_packets)
    index = int(length / 2)
    step = index
    is_sorted = False
    while not is_sorted:
        step = int(step / 2)
        if index <= 0 or index >= length:
            is_sorted = True
        elif compare_packet(sorted_packets[index], packet)[0]:
            index = index + max(step, 1)
        elif compare_packet(packet, sorted_packets[index - 1])[0]:
            index = index - max(1, step)
        else:
            is_sorted = True
    sorted_packets.insert(index, packet)
    return sorted_packets


for i in range(len(data)):
    if data[i] == "":
        continue
    packet = ast.literal_eval(data[i])
    # print(f"sorting {packet} into {sorted_packets}")
    sorted_packets = sort_packet(packet, sorted_packets)
print(
    (
        sorted_packets.index(initial_packet_0) + 1,
        sorted_packets.index(initial_packet_1) + 1,
    )
)
# %%
