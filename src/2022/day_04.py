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

def part1(data):
    result = 0
    for s in data:
        l = len(s)
        if l > 0:
            pairs = re.split(',|-', s)
            if (int(pairs[0]) >= int(pairs[2]) and int(pairs[1]) <= int(pairs[3])) or \
                (int(pairs[2]) >= int(pairs[0]) and int(pairs[3]) <= int(pairs[1])) :
                result += 1
            ####################################################################
            # After consideration the following would be a cleaner way to do it
            ####################################################################
            # set1 = range(int(pairs[0]), int(pairs[1]) + 1)
            # set2 = range(int(pairs[2]), int(pairs[3]) + 1)
            # if int(pairs[0]) in set2 and int(pairs[1]) in set2 or \
            #     int(pairs[2]) in set1 and int(pairs[3]) in set1:
            #     result += 1
            ####################################################################
    return result

def part2(data):
    result = 0
    for s in data:
        l = len(s)
        if l > 0:
            pairs = re.split(',|-', s)
            if (int(pairs[0]) >= int(pairs[2]) and int(pairs[0]) <= int(pairs[3])) or \
                (int(pairs[1]) >= int(pairs[2]) and int(pairs[1]) <= int(pairs[3])) or \
                (int(pairs[2]) >= int(pairs[0]) and int(pairs[2]) <= int(pairs[1])) or \
                (int(pairs[3]) >= int(pairs[0]) and int(pairs[3]) <= int(pairs[1])):
                result += 1
            ####################################################################
            # After consideration the following would be a cleaner way to do it
            ####################################################################
            # set1 = range(int(pairs[0]), int(pairs[1]) + 1)
            # set2 = range(int(pairs[2]), int(pairs[3]) + 1)
            # if int(pairs[0]) in set2 or int(pairs[1]) in set2 or \
            #     int(pairs[2]) in set1 or int(pairs[3]) in set1:
            #     result += 1
            ####################################################################
    return result

if __name__ == '__main__':
    year = 2022
    day = 4
    data = getData(year, day)
    result1 = part1(data)              
    result2 = part2(data)              

    print(f'Results - {year}/{day:02d}:')
    print(f"Result 1 - {result1}") # 448
    print(f"Result 2 - {result2}") # 794
