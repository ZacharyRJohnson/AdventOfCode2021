from collections import defaultdict
import copy

def read_input(file_name):
    f = open(file_name)
    lines = f.readlines()
    data = defaultdict(int)
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        data[i] = int(line.split()[4])
        i+=1
    return data

def part1(data):
    scores = [0]*2
    die = 1
    player1_turn = 1
    total_rolls = 0
    while scores[0] < 1000 and scores[1] < 1000:
        roll = 0
        for i in range(3):
            if die == 101:
                die = 1
            roll += die
            total_rolls += 1
            die += 1
            
        if player1_turn:
            temp = (data[0]+roll) % 10
            data[0] = temp if temp > 0 else 10
            scores[0] += data[0]
            player1_turn = 0
        else:
            temp = (data[1]+roll) % 10
            data[1] = temp if temp > 0 else 10
            scores[1] += data[1]
            player1_turn = 1
    loser = 1 if scores[0] >= 1000 else 0
    return total_rolls * scores[loser]

def part2(data):
    print(helper((data[0], data[1]), (0, 0), 0, defaultdict(tuple)))

def helper(pos, scores, turn, memo):
    unis_code = {3:1, 4:3, 5:6, 6:7, 7:6, 8:3, 9:1}
    key1 = (pos, scores, turn)
    totals = [0, 0]
    if memo[key1] != ():
        return memo[key1]
    elif scores[0] >= 21:
        return (1,0)
    elif scores[1] >= 21:
        return (0,1)
    
    if turn % 2 == 0:
        cur_play_pos = pos[0]
        for roll in range(3, 10):
            temp = (cur_play_pos+roll) % 10
            new_spot = temp if temp > 0 else 10
            new_pos = (new_spot, pos[1])
            new_scores = (scores[0]+new_spot, scores[1])
            ret = helper(new_pos, new_scores, turn+1, memo)
            memo[(new_pos, new_scores, turn+1)] = ret
            totals[0] += (unis_code[roll] * ret[0])
            
    else:
        cur_play_pos = pos[1]
        for roll in range(3, 10):
            temp = (cur_play_pos+roll) % 10
            new_spot = temp if temp > 0 else 10
            new_pos = (pos[0], new_spot)
            new_scores = (scores[0], scores[1]+new_spot)
            ret = helper(new_pos, new_scores, turn+1, memo)
            memo[(new_pos, new_scores, turn+1)] = ret
            totals[1] += (unis_code[roll] * ret[1])
    print(totals)
    return tuple(totals)
    
    # p1_pos = pos[0]
    # p2_pos = pos[1]
    # p1_won = 0
    # p1_newspots = []
    # leftover = 0
    # for roll in range(3, 10):
    #     temp = (p1_pos+roll) % 10
    #     new_spot = temp if temp > 0 else 10
    #     if scores[0] + new_spot >= 21:
    #         p1_won += unis_code[roll]
    #     else:
    #         leftover += unis_code[roll]
    #         p1_newspots.append(new_spot)

    # p2_won = 0
    # p2_newspots = []
    # for roll in range(3, 10):
    #     temp = (p2_pos+roll) % 10
    #     new_spot = temp if temp > 0 else 10
    #     if scores[1] + new_spot >= 21:
    #         p2_won += leftover * unis_code[roll]
    #     else:

    #         p2_newspots.append(new_spot)

    # for p1_new in p1_newspots:
    #     for p2_new in p2_newspots:
    #         p1_temp, p2_temp = helper((p1_new, p2_new), (scores[0] + p1_new, scores[1] + p2_new))
    #         p1_won *= p1_temp
    #         p2_won *= p2_temp
    # return p1_won, p2_won    


def main():
    in1 = "input.txt"
    t = "test.txt"
    data = read_input(t)
    print(part1(data))
    print(part2(data))
main()