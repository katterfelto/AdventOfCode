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

import re

def turnOn1(grid, x1, y1, x2, y2):
    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            grid[x][y] = 1
    return grid

def turnOff1(grid, x1, y1, x2, y2):
    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            grid[x][y] = 0
    return grid

def toggle1(grid, x1, y1, x2, y2):
    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            if grid[x][y] == 0:
                grid[x][y] = 1
            else:
                grid[x][y] = 0
    return grid

def countActiveLights1(grid):
    result = 0
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if grid[x][y] == 1:
                result += 1
    return result

def part1(data):
    grid = []
    for x in range(1000):
        grid.append([])
        for y in range(1000):
            grid[x].append(0)
    for s in data:
        if s.startswith('turn on '):
            p = re.split(',| through ', s[8:])
            grid = turnOn1(grid, int(p[0]), int(p[1]), int(p[2]), int(p[3]))
        elif s.startswith('turn off '):
            p = re.split(',| through ', s[9:])
            grid = turnOff1(grid, int(p[0]), int(p[1]), int(p[2]), int(p[3]))
        elif s.startswith('toggle '):
            p = re.split(',| through ', s[7:])
            grid = toggle1(grid, int(p[0]), int(p[1]), int(p[2]), int(p[3]))
    return countActiveLights1(grid)

def turnOn2(grid, x1, y1, x2, y2):
    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            grid[x][y] += 1
    return grid

def turnOff2(grid, x1, y1, x2, y2):
    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            grid[x][y] = max(0, grid[x][y] - 1)
    return grid

def toggle2(grid, x1, y1, x2, y2):
    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            grid[x][y] += 2
    return grid

def countActiveLights2(grid):
    result = 0
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            result += grid[x][y]
    return result

def part2(data):
    grid = []
    for x in range(1000):
        grid.append([])
        for y in range(1000):
            grid[x].append(0)
    for s in data:
        if s.startswith('turn on '):
            p = re.split(',| through ', s[8:])
            grid = turnOn2(grid, int(p[0]), int(p[1]), int(p[2]), int(p[3]))
        elif s.startswith('turn off '):
            p = re.split(',| through ', s[9:])
            grid = turnOff2(grid, int(p[0]), int(p[1]), int(p[2]), int(p[3]))
        elif s.startswith('toggle '):
            p = re.split(',| through ', s[7:])
            grid = toggle2(grid, int(p[0]), int(p[1]), int(p[2]), int(p[3]))
    return countActiveLights2(grid)

if __name__ == '__main__':
    year = 2015
    day = 6
    data = getData(year, day)
    result1 = part1(data)              
    result2 = part2(data)              

    print(f'Results - {year}/{day:02d}:')
    print(f"Result 1 - {result1}") # 569999
    print(f"Result 2 - {result2}") # 17836115