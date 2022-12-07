import aocd

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

def part1(data):
    scores = {
        'A': {'X': 1 + 3, 'Y': 2 + 6, 'Z': 3 + 0},
        'B': {'X': 1 + 0, 'Y': 2 + 3, 'Z': 3 + 6},
        'C': {'X': 1 + 6, 'Y': 2 + 0, 'Z': 3 + 3}
        }
    result = 0
    for s in data:
        if len(s) > 0:
            game = s.split(' ')
            result += scores[game[0]][game[1]]
    return result

def part2(data):
    scores = {
        'A': {'Y': 1 + 3, 'Z': 2 + 6, 'X': 3 + 0},
        'B': {'X': 1 + 0, 'Y': 2 + 3, 'Z': 3 + 6},
        'C': {'Z': 1 + 6, 'X': 2 + 0, 'Y': 3 + 3}
        }
    result = 0
    for s in data:
        if len(s) > 0:
            game = s.split(' ')
            result += scores[game[0]][game[1]]
    return result

if __name__ == '__main__':
    year = 2022
    day = 2
    data = getData(year, day)
    result1 = part1(data)              
    result2 = part2(data)              

    print(f'Results - {year}/{day:02d}:')
    print(f"Result 1 - {result1}") # 10994
    print(f"Result 2 - {result2}") # 12526
