from collections import defaultdict

def read_input(file_name):
    f = open(file_name)
    line = f.readlines()
    data = []
    for i, val in enumerate(line):
        val = val.strip()
        data.append([int(x) for x in val])
    return data

def check_neighbors(x, y, data):
    val = data[x][y]
    if x != 0:
        if val >= data[x-1][y]:
            return False
    if x != len(data) - 1:
        if val >= data[x+1][y]:
            return False
    if y != 0:
        if val >= data[x][y-1]:
            return False
    if y != len(data[x]) - 1:
        if val >= data[x][y+1]:
            return False
    return True

def get_neighbors(x, y, data):
    neighbors = []
    if x != 0:
        neighbors.append((x-1, y))
    if x != len(data) - 1:
        neighbors.append((x+1, y))
    if y != 0:
        neighbors.append((x, y-1))
    if y != len(data[x]) - 1:
        neighbors.append((x, y+1))
    return neighbors

def get_basin(x, y, data):
    visited = {(x,y)}
    basin = {(x,y)}
    to_visit = get_neighbors(x, y, data)
    while len(to_visit) != 0:
        cord = to_visit.pop()
        val = data[cord[0]][cord[1]]
        visited.add(cord)
        if val != 9:
            to_visit += [x for x in get_neighbors(cord[0], cord[1], data) if x not in visited]
            basin.add(cord)
    return len(basin)

def part1(data):
    lows = []
    for x in range(len(data)):
        for y in range(len(data[x])):
            if check_neighbors(x, y, data):

                lows.append(data[x][y]+1)
    return sum(lows)

def part2(data):
    lows = []
    for x in range(len(data)):
        for y in range(len(data[x])):
            if check_neighbors(x, y, data):
                lows.append((x, y))
    basin_size = []
    for low in lows:
        basin_size.append(get_basin(low[0], low[1], data))
    basin_size.sort()
    
    return basin_size[-1] * basin_size[-2] * basin_size[-3]

def main():
    in1 = "input.txt"
    t1 = "test.txt"
    data = read_input(in1)
    print(part1(data))
    print(part2(data))

main()