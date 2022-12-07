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

def part1(data):
    plus = data.count('(')
    minus = data.count(')')
    return plus - minus

def part2(data):
    floor = 0
    for i in range(len(data)):
        if data[i] == '(':
            floor += 1
        else:
            floor -= 1
        if floor == -1:
            return i + 1
    return -1

if __name__ == '__main__':
    year = 2015
    day = 1
    data = getData(year, day)
    result1 = part1(data[0])              
    result2 = part2(data[0])              

    print(f'Results - {year}/{day:02d}:')
    print(f"Result 1 - {result1}") # 232
    print(f"Result 2 - {result2}") # 1783