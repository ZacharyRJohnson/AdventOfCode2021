from collections import defaultdict
import copy

def read_input(file_name):
    f = open(file_name)
    lines = f.readlines()
    enhancement_alg = [ 0 if x=="." else 1 for x in lines[0].strip()]
    data = defaultdict(int)
    max_x = len(lines[2].strip())
    max_y = len(lines)-2
    for i in range(2, len(lines)):
        line = lines[i].strip()
        for x in range(len(line)):
            data[(x, i-2)] = 0 if line[x] == "." else 1
        
    return data, enhancement_alg, (max_x, max_y)

def get_alg_index(cord, data):
    x = cord[0]
    y = cord[1]
    grid = [(x-1,y-1), (x, y-1), (x+1, y-1), (x-1, y), (x, y), (x+1, y), (x-1, y+1), (x, y+1), (x+1, y+1)]
    bin_str = ""
    #print("Cord:",cord)
    for grid_cord in grid:
    #    print(grid_cord, data[grid_cord])
        bin_str += str(data[grid_cord])
    # print(bin_str)
    return int(bin_str, 2)

def part1(data, alg, max_cord):
    min_cord = (0, 0)
    steps = 50
    board = copy.deepcopy(data)
    for i in range(steps):
        print(i)
        if i % 2 == 0:
            next_board = defaultdict(lambda: alg[0])
        else:
            next_board = defaultdict(lambda: alg[len(alg)-1])
        new_min = (min_cord[0]-1, min_cord[1]-1)
        new_max = (max_cord[0]+1, max_cord[1]+1)
        for y in range(new_min[1], new_max[1]+1):
            for x in range(new_min[0], new_max[0]+1):
                cord = (x,y)
                next_board[cord] = alg[get_alg_index(cord, board)]
                

        min_cord = new_min
        max_cord = new_max
        board = copy.deepcopy(next_board)
    total_lit = 0
    for y in range(min_cord[1], max_cord[1]+1):
        for x in range(min_cord[0], max_cord[0]+1):
            cord = (x,y)
            total_lit += board[cord]
            
    return total_lit

def main():
    in1 = "input.txt"
    t = "test.txt"
    data, alg, max_cord = read_input(in1)
    #get_alg_index((1,0), data)
    print(part1(data, alg, max_cord))
    #print(part2(data))

main()