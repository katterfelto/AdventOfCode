import aocd
from os.path import exists

year = 2022
day = 5

######################################################
# Get the Input data
######################################################
if not exists(f'./inputData/{year}/{day:02d}.txt'):
    with open(f'./inputData/{year}/{day:02d}.txt', 'w') as f:
        f.write(aocd.get_data(day=day, year=2022))
with open(f'inputData/{year}/{day:02d}.txt', 'r') as f:
    data = f.read().split('\n')

######################################################
# The solution
######################################################
stacks = {1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[],9:[]}

import re

def addToStack(s):
    #[B] [Z] [Z] [H] [L] [P] [L] [J] [N]
    i = 1
    j = 1
    while i < len(s):
        if s[i] != ' ':
            stacks[j].insert(0, s[i])
        i += 4
        j += 1

def moveCrates1(s):
    #move 4 from 9 to 1
    parts = re.split('move | from | to ', s.strip())
    count = int(parts[1])
    src = int(parts[2])
    dest = int(parts[3])
    while count > 0:
        stacks[dest].append(stacks[src].pop())
        count -= 1

def moveCrates2(s):
    #move 4 from 9 to 1
    parts = re.split('move | from | to ', s.strip())
    count = int(parts[1])
    src = int(parts[2])
    dest = int(parts[3])
    while count > 0:
        stacks[dest].append(stacks[src].pop(-count))
        count -= 1

def generateResults():
    result = ''
    for i in range(1, 10):
        if len(stacks[i]) > 0:
            result += stacks[i].pop()
    return result

def part1():
    for s in data:
        if len(s) > 0:
            if s[0] == '[':
                addToStack(s)
            elif s[0:4] == 'move':
                moveCrates1(s)

def part2():
    for s in data:
        if len(s) > 0:
            if s[0] == '[':
                addToStack(s)
            elif s[0:4] == 'move':
                moveCrates2(s)

stacks = {1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[],9:[]}
part1()              
result1 = generateResults()

stacks = {1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[],9:[]}
part2()              
result2 = generateResults()

######################################################
# Output the results
######################################################
print(f'Results - {year}/{day:02d}:')
print(f"Result 1 - {result1}") # JDTMRWCQJ
print(f"Result 2 - {result2}") # VHJDDCWRD
