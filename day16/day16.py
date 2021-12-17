def read_input(file_name):
    f = open(file_name)
    code = {"0": "0000", "1": "0001", "2": "0010", "3": "0011", "4": "0100", "5": "0101", "6": "0110", "7": "0111", "8": "1000", "9": "1001", "A": "1010", "B": "1011", "C": "1100", "D": "1101", "E": "1110", "F": "1111"}
    line = f.readline()
    line = line.strip()
    data = ""
    for c in line:
        data += code[c]
    return data

def read_raw(val):
    num_bits = len(val)*4
    data = bin(int(val, 16))[2:].zfill(num_bits)
    return data

def build_tree(packets):
    packet = packets.pop()
    sub_packs = []
    bits_read = packet[-1]
    packs_read = 1

    if packet[1] == 4:
        return packet[2], sub_packs, bits_read, packs_read
    else:
        tot_read = 0
        while packet[3]-tot_read > 0:
            (val, subp, b_read, p_read) = build_tree(packets)
            sub_packs.append((val, subp))
            tot_read += b_read if packet[2] == 0 else 1
            bits_read += b_read
            packs_read += p_read
    return packet[1], sub_packs, bits_read, packs_read

def eval(tree):
    value = 0
    if tree[1] == []:
        value = tree[0]
    else:
        op = tree[0]
        sub_packs = tree[1]
        if op == 0:
            temp = 0
            while sub_packs:
                temp += eval(sub_packs.pop())
            value += temp
        elif op == 1:
            temp = 1
            while sub_packs:
                temp *= eval(sub_packs.pop())
            value += temp
        elif op == 2:
            temp = []
            while sub_packs:
                temp.append(eval(sub_packs.pop()))
            value += min(temp)
        elif op == 3:
            temp = []
            while sub_packs:
                temp.append(eval(sub_packs.pop()))
            value += max(temp)
        elif op == 5:
            temp = 1 if eval(sub_packs[0]) > eval(sub_packs[1]) else 0
            value += temp
        elif op == 6:
            temp = 1 if eval(sub_packs[0]) < eval(sub_packs[1]) else 0
            value += temp
        elif op == 7:
            temp = 1 if eval(sub_packs[0]) == eval(sub_packs[1]) else 0
            value += temp
    return value
            
def part1(data):
    v_sum = 0
    packets = []
    i = 0
    while i < len(data):
        if set(data[i:]) == {"0"}:
            break
        packet = []
        v_num = int(data[i:i+3], 2)
        v_sum += v_num
        i+=3
        type_id = int(data[i:i+3], 2)
        i+=3
        if type_id == 4:
            bin_num = ""
            group = data[i:i+5]
            i += 5
            while group[0] != "0":
                bin_num += group[1:]
                group = data[i:i+5]
                i+=5
            bin_num += group[1:]
            lit_num = int(bin_num, 2)
            packet = [v_num, type_id, lit_num]
            packets.append(packet)
        else:
            len_id = int(data[i], 2)
            i += 1
            len_val = 0
            if len_id == 0:
                len_val = int(data[i:i+15],2)
                i+=15
            else:
                len_val = int(data[i:i+11],2)
                i+=11
            packet = [v_num, type_id, len_id, len_val]
            packets.append(packet)

    return v_sum

def part2(data):
    v_sum = 0
    packets = []
    i = 0
    while i < len(data):
        if set(data[i:]) == {"0"}:
            break
        packet = []
        pack_start = i
        v_num = int(data[i:i+3], 2)
        v_sum += v_num
        i+=3
        type_id = int(data[i:i+3], 2)
        i+=3
        if type_id == 4:
            bin_num = ""
            group = data[i:i+5]
            i += 5
            while group[0] != "0":
                bin_num += group[1:]
                group = data[i:i+5]
                i+=5
            bin_num += group[1:]
            lit_num = int(bin_num, 2)
            pack_len = i-pack_start
            packet = [v_num, type_id, lit_num, pack_len]
            packets.append(packet)
        else:
            len_id = int(data[i], 2)
            i += 1
            len_val = 0
            if len_id == 0:
                len_val = int(data[i:i+15],2)
                i+=15
            else:

                len_val = int(data[i:i+11],2)
                i+=11
            pack_len = i-pack_start
            packet = [v_num, type_id, len_id, len_val, pack_len]
            packets.append(packet)
    packets.reverse()
    ret = build_tree(packets)
    tree = (ret[0], ret[1])
    return eval(tree)

def main():
    t = "test.txt"
    t2 = "test3.txt"
    in1 = "input.txt"
    #data = read_input(in1)
    data = read_raw("9C0141080250320F1802104A08")
    #print(part1(data))
    print(part2(data))

main()