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

def visitHouse(grid, delivery):
    r = delivery[0]
    c = delivery[1]
    if r in grid.keys():
        if c in grid[r].keys():
            grid[r][c] += 1
        else:
            grid[r][c] = 1
    else:
        grid[r] = { c : 1 }
    return grid

def processDirection(grid, delivery, direction):
    if direction == '^':
        delivery[0] += 1
    elif direction == 'v':
        delivery[0] -= 1
    elif direction == '>':
        delivery[1] += 1
    elif direction == '<':
        delivery[1] -= 1
    grid = visitHouse(grid, delivery)
    return (grid, delivery)
    
def countHouses(grid):
    result = 0
    for k in grid.keys():
        result += len(grid[k])
    return result

def part1(data):
    grid = { 0: { 0: 1 } }
    santa = [0, 0]
    for d in data:
        (grid, santa) = processDirection(grid, santa, d)
    return countHouses(grid)

def part2(data):
    grid = { 0: { 0: 2 } }
    santa = [0, 0]
    roboS = [0, 0]
    for i in range(len(data)):
        if i % 2 == 0:
            (grid, santa) = processDirection(grid, santa, data[i])
        else:
            (grid, roboS) = processDirection(grid, roboS, data[i])
    return countHouses(grid)

if __name__ == '__main__':
    year = 2015
    day = 3
    data = getData(year, day)
    result1 = part1(data[0])              
    result2 = part2(data[0])              

    print(f'Results - {year}/{day:02d}:')
    print(f"Result 1 - {result1}") # 2081
    print(f"Result 2 - {result2}") # 