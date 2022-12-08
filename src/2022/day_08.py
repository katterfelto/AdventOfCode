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

def calculateScenicScore(data, r, c):
    maxHeight = data[r][c]
    up = 0
    i = r
    while i > 0 and data[i][c] <= maxHeight:
        i -= 1
        up += 1
        if data[i][c] >= maxHeight:
            break
        
    left = 0
    i = c
    while i > 0 and data[r][i] <= maxHeight:
        i -= 1
        if i > 0:
            left += 1
        if data[r][i] >= maxHeight:
            break
    right = 0
    i = c
    while i < len(data[0]) - 1 and data[r][i] <= maxHeight:
        i += 1
        right += 1
        if data[r][i] >= maxHeight:
            break
    down = 0
    i = r
    while i < len(data) - 1 and data[i][c] <= maxHeight:
        down += 1
        i += 1
        if data[i][c] >= maxHeight:
            break
    return up * left * right * down

def part1(data):
    visible = []
    width = len(data[0])
    # Check each row
    for r in range(1, len(data) - 1):
        # left to right
        highest = data[r][0]
        for c in range(1, width - 1):
            if (data[r][c] > highest):
                highest = data[r][c]
                coords = f'{c},{r}'
                if not coords in visible:
                    visible.append(coords)
        # right to left
        highest = data[r][width - 1]
        for c in range(width - 2, 0, -1):
            if (data[r][c] > highest):
                highest = data[r][c]
                coords = f'{c},{r}'
                if not coords in visible:
                    visible.append(coords)
    
    # Check each column
    for c in range(1, width - 1):
        # top to bottom
        highest = data[0][c]
        for r in range(1, len(data) - 1):
            if (data[r][c] > highest):
                highest = data[r][c]
                coords = f'{c},{r}'
                if not coords in visible:
                    visible.append(coords)
        # bottom to top
        highest = data[len(data) - 1][c]
        for r in range(len(data) - 2, 0, -1):
            if (data[r][c] > highest):
                highest = data[r][c]
                coords = f'{c},{r}'
                if not coords in visible:
                    visible.append(coords)
    return len(visible) + ((width + len(data)) * 2) - 4

def part2(data):
    bestScore = 0
    # Check each row
    for r in range(len(data)):
        for c in range(len(data[0])):
            bestScore = max(bestScore, calculateScenicScore(data, r, c))
    return bestScore

if __name__ == '__main__':
    year = 2022
    day = 8
    data = getData(year, day)
    result1 = part1(data)              
    result2 = part2(data)              

    print(f'Results - {year}/{day:02d}:')
    print(f"Result 1 - {result1}") # 1676
    print(f"Result 2 - {result2}") # 
