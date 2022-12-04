import aocd
from os.path import exists

year = 2022
day = 1

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
result = []
calories = 0
for s in data:
    s = s.strip()
    if len(s) == 0:
        result.append(calories)
        calories = 0
    else:
        calories += int(s)

result.sort(reverse=True)

######################################################
# Output the results
######################################################
print(f'Results - {year}/{day:02d}:')
print(f'Result 1 - {result[0]}')
print(f'Result 2 - {result[0] + result[1] + result[2]}')