from collections import defaultdict

def read_input(file_name):
    f = open(file_name)
    line = f.readlines()
    data = []
    for i, val in enumerate(line):
        val = val.strip()
        data.append(val)
    return data

def part1(data):
    pairings = defaultdict(str)
    pairings["("] = ")"
    pairings["["] = "]"
    pairings["{"] = "}"
    pairings["<"] = ">"

    bad_chars = []
    i = 0
    while i < len(data):
        line = data[i]
        stack = []
        openers = {"(", "[", "{", "<"}
        closer = {")", "]", "}", ">"}
        bad_line = False
        for char in line:
            if char in openers:
                stack.append(char)
            elif char in closer:
                first = stack.pop()
                if pairings[first] != char:
                    bad_line = True
                    data.pop(i)
                    bad_chars.append(char)
                    break
        if not bad_line:
            i+=1
            
            
    total = 0
    for char in bad_chars:
        if char == ")":
            total+=3
        elif char == "]":
            total+=57
        elif char == "}":
            total+=1197
        elif char == ">":
            total+= 25137
    return total

def part2(data):
    pairings = defaultdict(str)
    pairings["("] = ")"
    pairings["["] = "]"
    pairings["{"] = "}"
    pairings["<"] = ">"

    closing_chars = []
    i = 0
    while i < len(data):
        line = data[i]
        stack = []
        openers = {"(", "[", "{", "<"}
        closer = {")", "]", "}", ">"}
        bad_line = False
        for char in line:
            if char in openers:
                stack.append(char)
            elif char in closer:
                first = stack.pop()
                if pairings[first] != char:
                    bad_line = True
                    data.pop(i)
                    break
        if not bad_line:
            closing_chars.append([pairings[x] for x in stack])
            i+=1
        
    totals = []
    for line in closing_chars:
        line.reverse()
        line_total = 0
        for char in line:
            line_total *= 5
            if char == ")":
                line_total+=1
            elif char == "]":
                line_total+=2
            elif char == "}":
                line_total+=3
            elif char == ">":
                line_total+= 4
        totals.append(line_total)
    totals.sort()
    mid = len(totals)//2
    return totals[mid]

def main():
    t = "test.txt"
    in1 = "input.txt"
    data = read_input(in1)
    print(part1(data))
    print(part2(data))

main()