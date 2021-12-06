from collections import defaultdict

def read_input(file_name):
    f = open(file_name)
    line = f.readline()
    data = defaultdict(lambda: 8)
    for i, val in enumerate(line.split(",")):
        data[i] = int(val)

    return data

def part1(data):
    day = 0
    new_ind = len(data)
    while (day != 80):
        extend = []
        for fish_ind in data:
            val = data[fish_ind]
            if val == 0:
                data[fish_ind] = 6
                extend.append(8)
                new_ind += 1
            else:
                data[fish_ind] -= 1
        for val in extend:
            data[new_ind] = val
            new_ind += 1
        day += 1
    return len(data)

def part2(data):
    day = 0
    groups = [0]*7
    delay = []
    to_add_ar = [()]*2
    for ind in data:
        val = data[ind]
        groups[val] += 1
    while (day != 256):
        ind = day%7
        to_add = to_add_ar.pop(0)
        to_add_ar.append(((ind+2)%7,groups[ind]))
        if to_add != ():
            groups[to_add[0]] += to_add[1]
        day += 1

    total = sum(groups) + to_add_ar[0][1] + to_add_ar[1][1]
    return total


def main():
    in1 = "input1.txt"
    t1 = "test.txt"
    data = read_input(in1)
    #print(part1(data))
    print(part2(data))

main()