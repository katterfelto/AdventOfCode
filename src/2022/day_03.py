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
result1 = 0
result2 = 0

def calcPriority(c):
    ####################################################################
    # The following line check is a cleaner
    ####################################################################
    # if c.islower():
    ####################################################################
    if ord(c) > ord('a'):
        return ord(c) - ord('a') + 1
    else:
        return ord(c) - ord('A') + 27

def part1(data):
    result = 0
    for s in data:
        l = len(s)
        if l > 0:
            h = int(l/2)
            for c in s[0:h]:
                if c in s[h:]:
                    result += calcPriority(c)
                    break
    return result

def part2(data):
    result = 0
    count = 1
    parts = []
    for s in data:
        l = len(s)
        if l > 0:
            if count == 1:
                parts = list(s)
            else:
                newParts = []
                for c in parts:
                    if c in s:
                        newParts.append(c)
                if (count == 3):
                    result += calcPriority(newParts[0])
                    count = 0
                else:
                    parts = newParts
            count += 1
    return result

if __name__ == '__main__':
    year = 2022
    day = 3
    data = getData(year, day)
    result1 = part1(data)              
    result2 = part2(data)              

    print(f'Results - {year}/{day:02d}:')
    print(f"Result 1 - {result1}") # 8153
    print(f"Result 2 - {result2}") # 2342
