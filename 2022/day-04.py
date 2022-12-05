import aocd
from os.path import exists

year = 2022
day = 4

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

import re

for s in data:
    l = len(s)
    if l > 0:
        pairs = re.split(',|-', s)
        if (int(pairs[0]) >= int(pairs[2]) and int(pairs[1]) <= int(pairs[3])) or \
            (int(pairs[2]) >= int(pairs[0]) and int(pairs[3]) <= int(pairs[1])) :
            result1 += 1
        if (int(pairs[0]) >= int(pairs[2]) and int(pairs[0]) <= int(pairs[3])) or \
            (int(pairs[1]) >= int(pairs[2]) and int(pairs[1]) <= int(pairs[3])) or \
            (int(pairs[2]) >= int(pairs[0]) and int(pairs[2]) <= int(pairs[1])) or \
            (int(pairs[3]) >= int(pairs[0]) and int(pairs[3]) <= int(pairs[1])):
            result2+= 1
        ####################################################################
        # After consideration the following would be a cleaner way to do it
        ####################################################################
        # set1 = range(int(pairs[0]), int(pairs[1]) + 1)
        # set2 = range(int(pairs[2]), int(pairs[3]) + 1)
        # if int(pairs[0]) in set2 and int(pairs[1]) in set2 or \
        #     int(pairs[2]) in set1 and int(pairs[3]) in set1:
        #     result1 += 1
        # if int(pairs[0]) in set2 or int(pairs[1]) in set2 or \
        #     int(pairs[2]) in set1 or int(pairs[3]) in set1:
        #     result2 += 1
        ####################################################################
        
######################################################
# Output the results
######################################################
print(f'Results - {year}/{day:02d}:')
print(f"Result 1 - {result1}")
print(f"Result 2 - {result2}")
