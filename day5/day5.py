from collections import defaultdict

def read_input(file_name):
    f = open(file_name)
    lines = f.readlines()
    data = defaultdict(lambda: defaultdict(int))
    for i, line in enumerate(lines):
        line = line.strip()
        split_line = line.split()
        start_cords = [int(x) for x in split_line[0].split(",")]
        end_cords = [int(x) for x in split_line[2].split(",")]
        start_x = min(start_cords[0], end_cords[0])
        end_x = max(start_cords[0], end_cords[0])
        start_y = min(start_cords[1], end_cords[1])
        end_y = max(start_cords[1], end_cords[1])
        if (start_x != end_x and start_y != end_y):
            start_x = start_cords[0]
            start_y = start_cords[1]
            end_x = end_cords[0]
            end_y = end_cords[1]
            dx = 1 if start_x < end_x else -1
            dy = 1 if start_y < end_y else -1
            #print("(", start_x, ",", start_y, ")")
            while (start_x != end_x+dx):
             #   print(start_x, start_y)
                data[start_y][start_x] += 1
                start_x += dx
                start_y += dy
        else:
            for y in range(start_y, end_y + 1):
                for x in range(start_x, end_x + 1):
                    data[y][x] += 1

    return data

def part1(data):
    num_overlap = 0
    for row in data:
        print(row, data[row])
        for cell in data[row]:
            if data[row][cell] >= 2:
                num_overlap += 1
    return num_overlap

def main():
    t1 = "test.txt"
    in1 = "input1.txt"
    data = read_input(in1)
    print(part1(data))

main()