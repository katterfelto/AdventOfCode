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

def sumTotalAtMost(limit, struct):
    result = 0
    if struct['total'] < limit:
        result += struct['total']
    for k in struct['children'].keys():
        result += sumTotalAtMost(limit, struct['children'][k])
    return result

def dirWithSmallestTotalAbove(required, name, struct):
    result = ''
    size = 0
    if struct['total'] > required:
        result = name
        size = struct['total']
    for k in struct['children'].keys():
        (newName, newSize) = dirWithSmallestTotalAbove(required, k, struct['children'][k])
        if len(newName) > 0 and (newSize <= size or size == 0):
            result = newName
            size = newSize
    return result, size

def createStructure(data, i):
    result = {
        'size': 0,
        'total': 0,
        'children': {}
    }
    goUp = False
    while i < len(data) and not goUp:
        if data[i] == '$ cd ..':
            i += 1
            goUp = True
        elif data[i].startswith('$ cd '):
            name = data[i][5:]
            (child, i) = createStructure(data, i + 1)
            result['children'][name] = child
            result['total'] += child['total']
            if result['total'] == 0:
                pass
        elif data[i].startswith('$ ls'):
            i += 1
            while i < len(data) and not data[i].startswith("$"):
                if data[i].startswith("dir"):
                    pass
                else:
                    j = data[i].index(' ')
                    fSize = int(data[i][0:j])
                    result['size'] += fSize
                    result['total'] += fSize
                i += 1
    return (result, i)

def totalDiskUsage(data):
    total = 0
    for s in data:
        if s[0] in '1234567890':
            j = s.index(' ')
            total += int(s[0:j])
    return total


def part1(data):
    (struct, i) = createStructure(data, 1)
    return sumTotalAtMost(100000, struct)

def part2(data):
    (struct, i) = createStructure(data, 1)
    free = 70000000 - struct['total']
    required = 30000000 - free
    (name, size) = dirWithSmallestTotalAbove(required, '/', struct)
    return size

if __name__ == '__main__':
    year = 2022
    day = 7
    data = getData(year, day)
    result1 = part1(data)              
    result2 = part2(data)              

    print(f'Results - {year}/{day:02d}:')
    print(f"Result 1 - {result1}") # 1391690
    print(f"Result 2 - {result2}") # 5469168
