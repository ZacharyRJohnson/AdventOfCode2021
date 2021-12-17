from collections import defaultdict
import re
import itertools

def read_input(file_name):
    f = open(file_name)
    line = f.readline()
    data = defaultdict(bool)
    
    line_split = line.strip().split()
    x_range = [int(x) for x in re.findall('\d+|-\d+', line_split[2])]
    y_range = [int(x) for x in re.findall('\d+|-\d+', line_split[3])]
    x_range.sort()
    y_range.sort()
    for y in range(y_range[0], y_range[1]+1):
        for x in range(x_range[0], x_range[1]+1):
            data[(x, y)] = True

    return data, [x_range, y_range]

def max_height(vy):
    height = 0
    for v in range(vy,0,-1):
        height += v
    return height

# Brute force lol
def part1(data, ranges):
    max_y = 0
    y_range = ranges[1]
    y_difs = [1]
    ind = 0

    vy = 1
    while vy < 100:

        height = max_height(vy)
        while height - y_difs[ind] > y_range[1]:
            y_difs.append(y_difs[ind] + ind+2)
            ind += 1
        hit = False
        if y_range[0] <= height-y_difs[ind] <= y_range[1]:
            if max_y < height:
                max_y = height
                hit = True
        vy += 1
    return max_y

def part2(data, ranges):
    x_range = ranges[0]
    y_range = ranges[1]
    xvs = []
    yvs = []

    for xv in range(0, x_range[1]+1):
        pos = 0
        temp = xv
        while pos < x_range[0] and temp != 0:
            pos += temp
            temp -= 1
        if x_range[0] <= pos <= x_range[1]:
            xvs.append(xv)
    
    for yv in range(-200, 200):
        pos = 0
        temp = yv
        while pos > y_range[1]:
            pos += temp
            temp -= 1
        if y_range[0] <= pos <= y_range[1]:
            yvs.append(yv)
    
    total = 0
    for xv in xvs:
        for yv in yvs:
            vel = (xv, yv)
            if check_vel(vel, data, x_range, y_range):
                total += 1
    return total

def check_vel(vel, data, x_range, y_range):
    cur = [0,0]
    xv = vel[0]
    yv = vel[1]
    while (cur[0] < x_range[1]) and (cur[1] > y_range[0]):
        cur = [cur[0]+xv, cur[1]+yv]
        xv -= 1 if xv != 0 else 0
        yv -= 1
        if data[(cur[0], cur[1])]:
            return True
    return False

def main():
    in1 = "input.txt"
    t = "test.txt"
    data, ranges = read_input(in1)
    print(part1(data, ranges))
    print(part2(data, ranges))

main()