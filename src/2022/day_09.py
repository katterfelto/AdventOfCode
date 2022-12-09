import aocd
from os.path import exists

######################################################
# Get the Input data
######################################################
def getData(year, day):
    data = None
    if not exists(f'./inputData/{year}/{day:02d}.txt'):
        with open(f'./inputData/{year}/{day:02d}.txt', 'w') as f:
            f.write(aocd.get_data(day=day, year=year))
    with open(f'inputData/{year}/{day:02d}.txt', 'r') as f:
        data = f.read().split('\n')
    return data

######################################################
# The solution
######################################################

def visitLocation(grid, tail):
    r = tail[0]
    c = tail[1]
    if r in grid.keys():
        if c in grid[r].keys():
            grid[r][c] += 1
        else:
            grid[r][c] = 1
    else:
        grid[r] = { c : 1 }
    return grid

def adjustTail(head, tail):
    vert = head[0] - tail[0]
    horz = head[1] - tail[1]
    if vert > 1:
        tail[0] += 1
        if abs(horz) == 1:
            tail[1] += horz
    elif vert < -1:
        tail[0] -= 1
        if abs(horz) == 1:
            tail[1] += horz
    if horz > 1:
        tail[1] += 1
        if abs(vert) == 1:
            tail[0] += vert
    elif horz < -1:
        tail[1] -= 1
        if abs(vert) == 1:
            tail[0] += vert
    return tail

def processCommand1(grid, head, tail, command):
    for i in range(int(command[1])):
        if command[0] == 'U':
            head[0] += 1
        elif command[0] == 'D':
            head[0] -= 1
        elif command[0] == 'R':
            head[1] += 1
        elif command[0] == 'L':
            head[1] -= 1
        tail = adjustTail(head, tail)
        grid = visitLocation(grid, tail)
    return (grid, head, tail)



def processCommand10(grid, head, knots, command):
    for i in range(int(command[1])):
        if command[0] == 'U':
            head[0] += 1
        elif command[0] == 'D':
            head[0] -= 1
        elif command[0] == 'R':
            head[1] += 1
        elif command[0] == 'L':
            head[1] -= 1
        knots[0] = adjustTail(head, knots[0])
        for i in range(1, len(knots)):
            knots[i] = adjustTail(knots[i-1], knots[i])
        grid = visitLocation(grid, knots[-1])
    return (grid, head, knots)
    
def countLocations(grid):
    result = 0
    for k in grid.keys():
        result += len(grid[k])
    return result

def part1(data):
    grid = { 0: { 0: 1 } }
    head = [0, 0]
    tail = [0, 0]
    for d in data:
        (grid, head, tail) = processCommand1(grid, head, tail, d.split(' '))
    return countLocations(grid)

def part2(data):
    grid = { 0: { 0: 1 } }
    head = [0, 0]
    knots = []
    for i in range(9):
        knots.append([0,0])
    for d in data:
        (grid, head, knots) = processCommand10(grid, head, knots, d.split(' '))
    return countLocations(grid)

if __name__ == '__main__':
    year = 2022
    day = 9
    data = getData(year, day)
    result1 = part1(data)              
    result2 = part2(data)              

    print(f'Results - {year}/{day:02d}:')
    print(f"Result 1 - {result1}") # 6243
    print(f"Result 2 - {result2}") # 2630