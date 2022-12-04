import aocd
from os.path import exists

year = 2022
day = 2

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

scores1 = {
    'A': {'X': 1 + 3, 'Y': 2 + 6, 'Z': 3 + 0},
    'B': {'X': 1 + 0, 'Y': 2 + 3, 'Z': 3 + 6},
    'C': {'X': 1 + 6, 'Y': 2 + 0, 'Z': 3 + 3}
    }
scores2 = {
    'A': {'Y': 1 + 3, 'Z': 2 + 6, 'X': 3 + 0},
    'B': {'X': 1 + 0, 'Y': 2 + 3, 'Z': 3 + 6},
    'C': {'Z': 1 + 6, 'X': 2 + 0, 'Y': 3 + 3}
    }

for s in data:
    if len(s) > 0:
        game = s.split(' ')
        result1 += scores1[game[0]][game[1]]
        result2 += scores2[game[0]][game[1]]


######################################################
# Output the results
######################################################
print(f'Results - {year}/{day:02d}:')
print(f"Result 1 - {result1}")
print(f"Result 2 - {result2}")
