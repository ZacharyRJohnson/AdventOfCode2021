import copy
# Left and right will either be an int or another SNumber
class SNumber:
    def __init__ (self, parent, val):
        self.parent = parent
        self.val = val
        self.left = None
        self.right = None
    
    def get_magnitude(self):
        left = 0
        if self.left.val is not None:
            left = self.left.val
        else:
            left = self.left.get_magnitude()
        right = 0
        if self.right.val is not None:
            right = self.right.val
        else:
            right = self.right.get_magnitude()
        return 3*left + 2*right


def read_input(file_name):
    f = open(file_name)
    lines = f.readlines()
    data = []
    for line in lines:
        line = line.strip()
        data.append(parse_snum(line))
    return data

def pretty_print(snum):
    if snum.val is None:
        pretty_print(snum.left)
        pretty_print(snum.right)
    else:
        print(snum.val)

def closing_bracket_ind(num, ind):
    depth = 1
    ind += 1
    while depth != 0:
        if ind >= len(num):
            print("No closing bracket")
            return 
        if num[ind] == "[":
            depth += 1
        elif num[ind] == "]":
            depth -= 1
        ind += 1
    return ind

def parse_snum(num_str, parent=None):
    ind = 1
    snum = SNumber(parent, None)
    if num_str[ind] == "[":
        close_ind = closing_bracket_ind(num_str, ind)
        snum.left = parse_snum(num_str[ind:close_ind], snum)
        #print("Left:", num_str[ind:close_ind])
        ind = close_ind+1
    else:
        snum.left = SNumber(snum, int(num_str[ind]))
        #print("Left:", snum.left.val)
        ind += 2
    
    if num_str[ind] == "[":
        close_ind = closing_bracket_ind(num_str, ind)
        snum.right = parse_snum(num_str[ind:close_ind], snum)
        #print("Right:", num_str[ind:close_ind])
        ind = close_ind+1
    else:
        snum.right = SNumber(snum, int(num_str[ind]))
        #print("Right:",snum.right.val)
    return snum

def explode(snum):
    current = snum
    snum_stack = []
    num_stack = []
    depth = 0
    exploded = False
    complete = False
    right_val = 0
    while True:
        if current.val is None:
            if depth == 4 and exploded == False:
                if num_stack:
                    left_num = num_stack.pop()
                    left_num.val += current.left.val
                exploded = True
                right_val = current.right.val
                parent = current.parent
                
                if current is parent.left:
                    parent.left = SNumber(parent, 0)
                elif current is parent.right:
                    parent.right = SNumber(parent, 0)
                else:
                    print("Something is wrong, current is an object in its parent")
                    exit()
                if snum_stack:
                    (current, depth) = snum_stack.pop()
                    current = current.right
            else:
                snum_stack.append((current, depth))
                current = current.left
                depth += 1
        else:
            if exploded and complete == False:
                current.val += right_val
                complete = True
            num_stack.append(current)
            if(snum_stack):
                (current, depth) = snum_stack.pop()

                current = current.right
                depth+=1
            else:
                break
    return exploded

def split(snum):
    splited = False
    current = snum
    stack = []
    while True:
        if current.val is None:
            stack.append(current)
            current = current.left
        else:
            if current.val > 9:
                val = current.val
                left = int(float(val)/2)
                right = int(float(val)/2 + .5)
                current.val = None
                current.left = SNumber(current, left)
                current.right = SNumber(current, right)
                splited = True
                break
            elif(stack):
                current = stack.pop()
                current = current.right
            else:
                break
    return splited

def add(o_snum1, o_snum2):
    snum1 = copy.deepcopy(o_snum1)
    snum2 = copy.deepcopy(o_snum2)
    new_snum = SNumber(None, None)
    snum1.parent = new_snum
    snum2.parent = new_snum
    new_snum.left=snum1
    new_snum.right=snum2
    return new_snum

def reduce_snum(snum):
    op_performed = True
    while op_performed:
        op_performed = explode(snum)
        if op_performed:
            continue
        else:
            op_performed = split(snum)

def part1(data):
    i = 0
    snum = data[i]
    for i in range(1, len(data)):
        next_snum = data[i]
        snum = add(snum, next_snum)
        reduce_snum(snum)
    return snum.get_magnitude()

def part2(data):
    mags = []
    for i in range(len(data)-1):
        for j in range(i+1,len(data)):
            snum1 = add(data[i], data[j])
            snum2 = add(data[j], data[i])
            reduce_snum(snum1)
            reduce_snum(snum2)
            mags.append(snum1.get_magnitude())
            mags.append(snum2.get_magnitude())
    return max(mags)


def main():
    t = "test.txt"
    in1 = "input.txt"
    data = read_input(in1)
    print(part1(data))
    print(part2(data))

main()