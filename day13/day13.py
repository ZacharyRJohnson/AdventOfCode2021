from collections import defaultdict

def read_input(file_name):
    f = open(file_name)
    lines = f.readlines()
    data = defaultdict(lambda: False)
    folds = []
    i = 0
    while i < len(lines):
        if lines[i].strip() == "":
            break
        cord = [int(x) for x in lines[i].strip().split(",")]
        data[(cord[0], cord[1])] = True
        i+=1
    i += 1
    while i < len(lines):
        line = lines[i]
        line_split = line.strip().split("=")
        folds.append((line_split[0][-1], int(line_split[1])))
        i+=1

    return data, folds

def part1(data, folds):
    for fold in folds:
        axis_ind = 0 if fold[0] == "x" else 1
        location = fold[1]
        new_data = data.copy()
        for key in data:
            if data[key] == False:
                continue
            if key[axis_ind] > location:
                new_cord = ()
                if fold[0] == "x":
                    new_cord = (key[axis_ind]-2*(abs(key[axis_ind] - location)), key[(axis_ind + 1)%2])
                else:
                    new_cord = (key[(axis_ind + 1)%2], key[axis_ind] - 2*(abs(key[axis_ind] - location)))
                new_data[new_cord] = True
                new_data[key] = False
        
        data = new_data.copy()
        break
        

    visible = 0
    for key in data:
        if data[key]:
            visible += 1
    return visible

def part2(data, folds):
    for fold in folds:
        axis_ind = 0 if fold[0] == "x" else 1
        location = fold[1]
        new_data = data.copy()
        for key in data:
            if data[key] == False:
                continue
            if key[axis_ind] > location:
                new_cord = ()
                if fold[0] == "x":
                    new_cord = (key[axis_ind]-2*(abs(key[axis_ind] - location)), key[(axis_ind + 1)%2])
                else:
                    new_cord = (key[(axis_ind + 1)%2], key[axis_ind] - 2*(abs(key[axis_ind] - location)))
                new_data[new_cord] = True
                new_data[key] = False
        
        data = new_data.copy()
    
    max_x = -1000
    max_y = -1000
    min_x = float("inf")
    min_y = float("inf")

    for key in data:
        x = key[0]
        y = key[1]
        max_x = max(x, max_x)
        min_x = min(x, min_x)
        max_y = max(y, max_y)
        min_y = min(y, min_y)
    for y in range(min_y, 6):
        line = ""
        for x in range(min_x, 39):
            if data[(x,y)]:
                line += "#"
            else:
                line +="."
        print(line)


def main():
    in1 = "input.txt"
    t = "test.txt"
    data, folds = read_input(in1)
    print(part1(data, folds))
    part2(data, folds)

main()