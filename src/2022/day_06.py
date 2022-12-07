import aocd
from os.path import exists

year = 2022
day = 6

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

def codeFound(letters):
    for c in letters:
        if letters.count(c) > 1:
            return False
    return True

def part1(data):    
    buffer = []
    for i in range(len(data) - 1):
        buffer.insert(0, data[i])
        if len(buffer) == 4:
            if codeFound(buffer):
                return i + 1
            buffer.pop()
    return -1

def part2(data):    
    buffer = []
    for i in range(len(data) - 1):
        buffer.insert(0, data[i])
        if len(buffer) == 14:
            if codeFound(buffer):
                return i + 1
            buffer.pop()
    return -1

######################################################
# Output the results
######################################################
result1 = part1(data[0])              
result2 = part2(data[0])              

print(f'Results - {year}/{day:02d}:')
print(f"Result 1 - {result1}") # 1965
print(f"Result 2 - {result2}") # 2773
