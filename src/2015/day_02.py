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

def part1(data):
    result = 0
    for s in data:
        parts = s.split('x')
        s1 = int(parts[0]) * int(parts[1])
        s2 = int(parts[0]) * int(parts[2])
        s3 = int(parts[1]) * int(parts[2])
        result += (s1 + s2 + s3) * 2
        result += min(s1, min(s2, s3))
    return result

def part2(data):
    result = 0
    for s in data:
        parts = s.split('x')
        s1 = int(parts[0])
        s2 = int(parts[1])
        s3 = int(parts[2])
        result += s1 * s2 * s3
        
        result += (s1 + s2 + s3 - max(s1, max(s2, s3))) * 2
    return result

if __name__ == '__main__':
    year = 2015
    day = 2
    data = getData(year, day)
    result1 = part1(data)              
    result2 = part2(data)              

    print(f'Results - {year}/{day:02d}:')
    print(f"Result 1 - {result1}") # 1606483
    print(f"Result 2 - {result2}") # 3842356