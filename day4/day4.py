from collections import defaultdict

def read_input(file_name):
    f = open(file_name)
    line = f.readline().strip()
    draws = []
    boards = []
    draws += [int(x) for x in line.split(",")]
    line = f.readline()
    lines = f.readlines()
    temp = []

    for line in lines:
        line = line.strip()
        if line == "":
            boards.append(temp)
            temp = []
            continue
        temp.append([[int(x), False] for x in line.split()])
    boards.append(temp)

    return (draws, boards)

def isWinner(board):
    len_board = len(board)

    for i in range(len_board):
        row_win = 1
        row_val = 0
        col_win = 1
        col_val = 0

        for j in range(len(board[i])):
            row_cell = board[i][j]
            col_cell = board[j][i]
            row_val += row_cell[0]
            col_val += col_cell[0]
            if row_cell[1] == False:
                row_win = 0
            if col_cell[1] == False:
                col_win = 0
            if row_win == 0 and col_win == 0:
                break
        if row_win == 1 or col_win == 1:
            return (True, (row_win * row_val) + (col_win * col_val))
    return (False, 0)
        
def update_board(val, board):
    for row in board:
        for cell in row:
            if val == cell[0]:
                cell[1] = True
                return



def part1(draws, boards):
    for draw in draws:
        for board in boards:
            update_board(draw, board)
            (is_winner, val) = isWinner(board)
            if is_winner:
                val = 0
                for row in board:
                    for cell in row:
                        if cell[1] == False:
                            val += cell[0]
                
                return val * draw

def part2(draws, boards):
    win_list = []
    for draw in draws:
        for i, board in enumerate(boards):
            if board == 0:
                continue
            update_board(draw, board)
            (is_winner, val) = isWinner(board)
            if is_winner:
                win_list.append(board)
                boards[i] = 0

        if len(win_list) == len(boards):
            val = 0
            last_board = win_list[-1]
            for row in last_board:
                for cell in row:
                    if cell[1] == False:
                        val += cell[0]
            
            return val * draw
    

def main():
    t1 = "t1.txt"
    in1 = "in1.txt"
    (draws, boards) = read_input(in1)
    print(part1(draws, boards))
    print(part2(draws, boards))

main()