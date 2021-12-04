from collections import defaultdict

def read_input(file_name):
    f = open(file_name)
    lines = f.readlines()
    data = []
    for line in lines:
        line = line.strip().split()
        data.append(line)
    return data

def part1(data):
    hor_poz = 0
    depth = 0
    for inst in data:
        if inst[0] == "forward":
            hor_poz += int(inst[1])
        elif inst[0] == "up":
            depth -= int(inst[1])
        elif inst[0] == "down":
            depth += int(inst[1])
        
    return hor_poz * depth

def part2(data):
    hor_poz = 0
    depth = 0
    aim = 0
    for inst in data:
        if inst[0] == "forward":
            hor_poz += int(inst[1])
            depth += aim * int(inst[1])
        elif inst[0] == "up":
            aim -= int(inst[1])
        elif inst[0] == "down":
            aim += int(inst[1])
        
    return hor_poz * depth

def main():
    data = read_input("input1.txt")
    print(part1(data))
    print(part2(data))

main()