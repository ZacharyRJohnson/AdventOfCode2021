from collections import defaultdict

def read_input(file_name):
    f = open(file_name)
    line = f.readline()
    data = defaultdict(int)
    for i, val in enumerate(line.split(",")):
        data[int(val)] += 1

    return data

def calculate_fuel(position, data):
    fuel = 0
    for key in data:
        fuel += abs(key-position)*data[key]
    return fuel

def calculate_fuel2(position, data):
    fuel = 0
    for key in data:
        cost = sum([x for x in range(1, abs(key-position)+1)])
        fuel += cost*data[key]
    return fuel


def part1(data):
    prev = float("inf")
    position = 0
    is_decreasing = True
    while 1:
        cur = calculate_fuel(position, data)
        if cur > prev and is_decreasing == False:
            position += 1
            break
        elif cur < prev:
            prev = cur
        else:
            is_decreasing = False
        
        if is_decreasing:
            position += 1
        else:
            position -= 1

    return calculate_fuel(position, data)


def part2(data):
    prev = float("inf")
    position = 0
    is_decreasing = True
    while 1:
        cur = calculate_fuel2(position, data)
        if cur > prev and is_decreasing == False:
            position += 1
            break
        elif cur < prev:
            prev = cur
        else:
            is_decreasing = False
        
        if is_decreasing:
            position += 1
        else:
            position -= 1

    return calculate_fuel2(position, data)


def main():
    in1 = "input.txt"
    t1 = "test.txt"
    data = read_input(in1)
    #print(part1(data))
    print(part2(data))

main()