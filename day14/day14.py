from collections import defaultdict

def read_input(file_name):
    f = open(file_name)
    lines = f.readlines()
    start = lines[0].strip()
    data = defaultdict(str)
    i = 2
    while i < len(lines):
        line = lines[i].strip()
        line_split = [x.strip() for x in line.split("->")]
        data[line_split[0]] = line_split[1]
        i+=1
    return start, data

def part1(start, data):
    steps = 10
    start_str = start
    new_str = start
    for j in range(steps):
        offset = 0
        for i in range(len(start_str)-1):
            new_str = new_str[:i+1+offset] + data[start_str[i:i+2]] + new_str[i+1+offset:]
            offset += 1
        start_str = new_str

    lets = defaultdict(int)
    for let in start_str:
        lets[let] += 1
    max_num = 0
    min_num = float("inf")
    for key in lets:
        val = lets[key]
        if val > max_num:
            max_num = val
        elif val < min_num:
            min_num = val
    return max_num - min_num

def part2(start, data):
    steps = 40
    lets = defaultdict(int)
    chunks = [start[i] + start[i+1] for i in range(len(start)-1)]
    pairs = defaultdict(int)
    for let in start:
        lets[let] += 1
    for chunk in chunks:
        pairs[chunk] += 1
    for i in range(steps):
        new_dict = pairs.copy()
        for key in pairs:
            num_occ = pairs[key]
            new_char = data[key]
            lets[new_char] += num_occ
            left_pair = key[0] + new_char
            right_pair = new_char + key[1]
            new_dict[key] -= num_occ
            new_dict[left_pair] += num_occ
            new_dict[right_pair] += num_occ
        pairs = new_dict.copy()
        
    max_num = 0
    max_let = ""
    min_num = float("inf")
    min_let = ""
    for key in lets:
        val = lets[key]
        if val > max_num:
            max_num = val
            max_let = key
        elif val < min_num:
            min_num = val
            min_let = key
    return max_num - min_num
    

def main():
    t = "test.txt"
    in1 = "input.txt"
    start, data = read_input(in1)
    print(part1(start, data))
    print(part2(start, data))

main()
