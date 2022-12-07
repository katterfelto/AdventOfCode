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

def addToStack(stacks, s):
    #[B] [Z] [Z] [H] [L] [P] [L] [J] [N]
    i = 1
    j = 1
    while i < len(s):
        if s[i] != ' ':
            stacks[j].insert(0, s[i])
        i += 4
        j += 1
    return stacks

def moveCrates1(stacks, s):
    #move 4 from 9 to 1
    parts = re.split('move | from | to ', s.strip())
    count = int(parts[1])
    src = int(parts[2])
    dest = int(parts[3])
    while count > 0:
        stacks[dest].append(stacks[src].pop())
        count -= 1
    return stacks

def moveCrates2(stacks, s):
    #move 4 from 9 to 1
    parts = re.split('move | from | to ', s.strip())
    count = int(parts[1])
    src = int(parts[2])
    dest = int(parts[3])
    while count > 0:
        stacks[dest].append(stacks[src].pop(-count))
        count -= 1
    return stacks

def generateResults(stacks):
    result = ''
    for i in range(1, 10):
        if len(stacks[i]) > 0:
            result += stacks[i].pop()
    return result

def part1(data):
    stacks = {1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[],9:[]}
    for s in data:
        if len(s) > 0:
            if s[0] == '[':
                stacks = addToStack(stacks, s)
            elif s[0:4] == 'move':
                stacks = moveCrates1(stacks, s)
    return generateResults(stacks)

def part2(data):
    stacks = {1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[],9:[]}
    for s in data:
        if len(s) > 0:
            if s[0] == '[':
                stacks = addToStack(stacks, s)
            elif s[0:4] == 'move':
                stacks = moveCrates2(stacks, s)
    return generateResults(stacks)

if __name__ == '__main__':
    year = 2022
    day = 5
    data = getData(year, day)
    result1 = part1(data)              
    result2 = part2(data)              

    print(f'Results - {year}/{day:02d}:')
    print(f"Result 1 - {result1}") # JDTMRWCQJ
    print(f"Result 2 - {result2}") # VHJDDCWRD
