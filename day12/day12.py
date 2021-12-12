from collections import defaultdict

def read_input(file_name):
    f = open(file_name)
    line = f.readlines()
    data = defaultdict(list)
    for i, val in enumerate(line):
        vals = val.strip().split("-")
        data[vals[0]].append(vals[1])
        data[vals[1]].append(vals[0])
    return data

def part1(data):
    paths = []
    to_visit = [(x, ["start"]) for x in data["start"]]
    while len(to_visit) != 0:
        node = to_visit.pop()
        if node[0] == "end":
            paths.append(node[1] + ["end"])
        else:
            path = node[1].copy() + [node[0].lower()]
            to_visit += [(x, path) for x in data[node[0]] if x not in path]
    return len(paths)

def part2(data):
    paths = set()
    to_visit = [(x, ["start"], []) for x in data["start"]]
    while len(to_visit) != 0:
        node = to_visit.pop()
        if node[0] == "end":
            p_temp = "".join(node[1]) + "end"
            if p_temp not in paths:
                paths.add(p_temp)
        else:
            path = node[1].copy() + [node[0]]
            temp_to_visit = []
            for x in data[node[0]]:
                if x == "start":
                    continue
                if x.islower():
                    double_cave = [] if node[2] == [] else node[2][0]
                    num_x = path.count(x)
                    if double_cave == []: 
                        if num_x == 0:
                            temp_to_visit += [(x, path, [x])]
                            temp_to_visit += [(x, path, [])]
                        elif num_x == 1:
                            temp_to_visit += [(x, path, [x])]
                    else:
                        if x == double_cave and num_x < 2:
                            temp_to_visit += [(x, path, node[2])]
                        elif x != double_cave and num_x == 0:
                            temp_to_visit += [(x, path, node[2])]
                elif x.isupper():
                    temp_to_visit += [(x, path, node[2])]
            to_visit += temp_to_visit
    return len(paths)


def main():
    in1 = "input.txt"
    t = "test.txt"
    t2 = "test2.txt"
    t3 = "test3.txt"
    data = read_input(in1)
    print(part1(data))
    print(part2(data))

main()