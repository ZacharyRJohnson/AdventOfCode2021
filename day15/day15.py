from collections import defaultdict
import heapq

def read_input(file_name):
    f = open(file_name)
    lines = f.readlines()
    data = defaultdict(lambda: -1)
    y = 0
    max_x = len(lines[0].strip())-1
    for line in lines:
        line = line.strip()
        for x, val in enumerate(line):
            data[(x,y)] = int(val)
        y += 1
    max_y = y-1
    return data, (max_x, max_y)

def read_input2(file_name):
    f = open(file_name)
    lines = f.readlines()
    data = defaultdict(lambda: -1)
    max_x = len(lines[0].strip())-1
    max_y = len(lines)-1
    dest = ((max_x+1)*5-1, (max_y+1)*5-1)
    y_offset = 0
    for y_tile in range(5):
        x_offset = 0
        for x_tile in range(5):
            y = 0
            for line in lines:
                line = line.strip()
                for x, val in enumerate(line):
                    cord = (x+(x_offset * len(line)),y+(y_offset*len(lines)))
                    new_val = int(val) + x_offset + y_offset
                    data[(x+(x_offset * len(line)),y+(y_offset*len(lines)))] = new_val if new_val <= 9 else new_val-9
                y += 1
            x_offset += 1
        y_offset += 1
    return data, dest

# From the heapq documentation
def add_task(pq, entry_finder, task, priority):
    'Add a new task or update the priority of an existing task'
    if task in entry_finder:
        remove_task(entry_finder, task)
    entry = [priority, task]
    entry_finder[task] = entry
    heapq.heappush(pq, entry)

def remove_task(entry_finder, task):
    'Mark an existing task as REMOVED.  Raise KeyError if not found.'
    entry = entry_finder.pop(task)
    entry[-1] = (-1,-1)

def pop_task(pq, entry_finder):
    'Remove and return the lowest priority task. Raise KeyError if empty.'
    while pq:
        priority, task = heapq.heappop(pq)
        if task != (-1,-1):
            del entry_finder[task]
            return task
    raise KeyError('pop from an empty priority queue')

def get_neighbors(cord, data):
    change = [(0,1), (0,-1), (1,0), (-1,0)]
    neighbors = []
    for delt in change:
        neighbor = (cord[0]+delt[0], cord[1]+delt[1])
        if data[neighbor] != -1:
            neighbors.append(neighbor)
    return neighbors

def part1(data, dest):
    src = (0,0)
    entry_finder = {}
    dist = defaultdict(lambda: float("inf"))
    dist[src] = 0
    prev = defaultdict(tuple)
    queue = []
    for vertex in data:
        add_task(queue, entry_finder, vertex, dist[vertex])
    
    while len(entry_finder) > 0:
        node = pop_task(queue, entry_finder)
        neighbors = get_neighbors(node, data)
        for neighbor in neighbors:
            path = dist[node] + data[neighbor]
            if path < dist[neighbor]:
                dist[neighbor] = path
                prev[neighbor] = node
                add_task(queue, entry_finder, neighbor, path)
    return dist[dest]

def main():
    t = "test.txt"
    in1 = "input.txt"
    data, dest = read_input(in1)
    data2, dest2 = read_input2(in1)
    print(part1(data, dest))
    print(part1(data2, dest2))

main()