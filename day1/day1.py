from collections import defaultdict

def read_input(file_name):
    f = open(file_name)
    lines = f.readlines()
    return [int(lines[i].strip()) for i in range(len(lines))]

def part1(data):
    prev = -1
    increased = 0
    for val in data:
        if prev == -1:
            prev = val
        else:
            if prev < val:
                print(str(prev) + " is less than " + str(val))
                increased += 1
        prev = val
    return increased

def main():
    data = read_input("input1.txt")
    print(part1(data))
    window_data = [(data[i]+data[i+1]+data[i+2]) for i in range(len(data)-2)]
    print(part1(window_data))
    
main()