from collections import defaultdict
import copy



def read_input(file_name):
    f = open(file_name)
    line = f.readlines()
    data = []
    for i, val in enumerate(line):
        val = val.strip()
        data.append([int(x) for x in val])
    return data

def flash(x, y, data):
    change = [(-1,0), (1,0), (0,-1), (0,1), (1,1), (1,-1), (-1,1), (-1,-1)]
    # print(data)
    # print()
    for d in change:
        new_x = x+d[0]
        new_y = y+d[1]
        if 0 <= new_x < len(data) and 0 <= new_y < len(data[0]):
            if data[new_x][new_y] > 9 or data[new_x][new_y] == -1:
                continue
            data[new_x][new_y] += 1
            if data[new_x][new_y] > 9:
                data[new_x][new_y] = -1
                flash(new_x, new_y, data)

def part1(data):
    flashes = 0
    for i in range(100):
        # print("Step:", i)
        # print(data)
        for x in range(len(data)):
            for y in range(len(data[x])):
                data[x][y] += 1
        for x in range(len(data)):
            for y in range(len(data[x])):
                energy_lvl = data[x][y]
                if energy_lvl > 9:
                    flash(x, y, data)

        for x in range(len(data)):
            for y in range(len(data[x])):
                if data[x][y] > 9 or data[x][y] == -1:
                    flashes += 1
                    data[x][y] = 0

    return flashes

def part2(data):
    step = 0
    while True:
        # print("Step:", i)
        # print(data)
        for x in range(len(data)):
            for y in range(len(data[x])):
                data[x][y] += 1
        for x in range(len(data)):
            for y in range(len(data[x])):
                energy_lvl = data[x][y]
                if energy_lvl > 9:
                    flash(x, y, data)

        for x in range(len(data)):
            for y in range(len(data[x])):
                if data[x][y] > 9 or data[x][y] == -1:
                    data[x][y] = 0
        step += 1
        is_synched = True
        for x in range(len(data)):
            for y in range(len(data[x])):
                if data[x][y] != 0:
                    is_synched = False
                    break
            if not is_synched:
                break
        if is_synched:
            return step




def main():
    t = "test.txt"
    in1 = "input.txt"
    data = read_input(in1)
    #print(part1(data))
    print(part2(data))

main()