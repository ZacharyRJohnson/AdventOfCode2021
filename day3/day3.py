from collections import defaultdict

def read_input(file_name):
    f = open(file_name)
    lines = f.readlines()
    data = []
    i = 0
    for line in lines:
        line = line.strip()
        data.append(line)
    return data

def def_val():
    return 0

def part1(data):
    binCounter = [0 for i in range(len(data[0]))]
    for binary in data:
        for i in range(len(binary)):
            binCounter[i] += int(binary[i])
    gamma = ""
    epsilon = ""
    for val in binCounter:
        if val > len(data)//2:
            gamma += "1"
            epsilon += "0"
        else:
            gamma += "0"
            epsilon += "1"
    return int(gamma, 2) * int(epsilon, 2)

def part2(data):
    newDat = data.copy()
    i = 0
    while len(newDat) != 1:
        mostCommon = ""
        count = 0
        temp = []
        for binary in newDat:
            count += int(binary[i])
        if count >= len(newDat)/2:
            mostCommon = "1"
        else:
            mostCommon = "0"
        for binary in newDat:
            if binary[i] == mostCommon:
                temp.append(binary)
        newDat = temp.copy()
        i += 1
    ogr = newDat[0]
    newDat = data.copy()
    i = 0
    while len(newDat) != 1:
        mostCommon = ""
        count = 0
        temp = []
        for binary in newDat:
            count += int(binary[i])
        if count >= len(newDat)/2:
            mostCommon = "0"
        else:
            mostCommon = "1"
        for binary in newDat:
            if binary[i] == mostCommon:
                temp.append(binary)
        newDat = temp.copy()
        i += 1
    csr = newDat[0]
    print(ogr)
    print(csr)
    return int(ogr, 2) * int(csr, 2)
    
def main():
    t1 = "test.txt"
    in1 = "input1.txt"
    data = read_input(in1)
    print(part1(data))
    print(part2(data))
main()