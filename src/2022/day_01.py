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

def calculateCalories(data):
    result = []
    calories = 0
    for s in data:
        s = s.strip()
        if len(s) == 0:
            result.append(calories)
            calories = 0
        else:
            calories += int(s)
    if (calories > 0):
        result.append(calories)
    return result

def part1(data):
    result = calculateCalories(data)
    result.sort(reverse=True)
    return result[0]

def part2(data):
    result = calculateCalories(data)
    result.sort(reverse=True)
    return result[0] + result[1] + result[2]

######################################################
# Output the results
######################################################
result1 = part1(data)              
result2 = part2(data)              

print(f'Results - {year}/{day:02d}:')
print(f"Result 1 - {result1}") # 69836
print(f"Result 2 - {result2}") # 207968