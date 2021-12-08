from collections import defaultdict

def read_input(file_name):
    f = open(file_name)
    line = f.readlines()
    data = defaultdict(list)
    for i, val in enumerate(line):
        line_split = val.strip().split("|")
        data[i] = [["".join(sorted(sig)) for sig in line_split[0].split()], ["".join(sorted(sig)) for sig in line_split[1].split()]]
    return data

def part1(data):
    total = 0
    for key in data:
        val = data[key]
        for digits in val[1]:
            dig_len = len(digits)
            if dig_len == 4 or dig_len == 7 or dig_len == 2 or dig_len == 3:
                total += 1
    return total

def count_overlap(dig, sig):
    overlap = 0
    for char in dig:
        overlap += sig.count(char)
    return overlap

def find_mapping(signals):
    mappings = defaultdict(lambda: -1)
    not_known = []
    one_sig = ""
    four_sig = ""
    for i,sig in enumerate(signals):
        if len(sig) == 7:
            mappings[sig] = 8
        elif len(sig) == 4:
            mappings[sig] = 4
            four_sig = sig
        elif len(sig) == 3:
            mappings[sig] = 7
        elif len(sig) == 2:
            mappings[sig] = 1
            one_sig = sig
        else:
            not_known.append(sig)

    for sig in not_known:
        one_overlap = count_overlap(one_sig, sig)
        four_overlap = count_overlap(four_sig, sig)
        if one_overlap == 2: 
            if len(sig) == 5:
                mappings[sig] = 3
            if len(sig) == 6:
                if four_overlap == 4:
                    mappings[sig] = 9
                elif four_overlap == 3:
                    mappings[sig] = 0
        elif one_overlap == 1: 
            if len(sig) == 6:
                mappings[sig] = 6
            elif four_overlap == 3:
                mappings[sig] = 5
            else:
                mappings[sig] = 2
    return mappings

def part2(data):
    total = 0
    for key in data:
        val = data[key]
        mappings = find_mapping(val[0])
        num = ""
        for out in val[1]:
            num += str(mappings[out])
        total += int(num)
    return total

def main():
    in1 = "input.txt"
    t1 = "test.txt"
    t2 = "test1.txt"
    data = read_input(in1)
    print(part1(data))
    print(part2(data))

main()