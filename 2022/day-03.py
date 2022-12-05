import aocd
from os.path import exists

year = 2022
day = 3

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

count = 1
parts = []
for s in data:
    l = len(s)
    if l > 0:
        h = int(l/2)
        for c in s[0:h]:
            if c in s[h:]:
                result1 += calcPriority(c)
                break
        if count == 1:
            parts = list(s)
        else:
            newParts = []
            for c in parts:
                if c in s:
                    newParts.append(c)
            if (count == 3):
                result2 += calcPriority(newParts[0])
                count = 0
            else:
                parts = newParts
        count += 1
        
######################################################
# Output the results
######################################################
print(f'Results - {year}/{day:02d}:')
print(f"Result 1 - {result1}")
print(f"Result 2 - {result2}")
