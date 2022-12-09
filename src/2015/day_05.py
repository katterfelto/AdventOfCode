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

def hasAtLeast3Vowels(s):
    count = s.count('a')
    count += s.count('e')
    count += s.count('i')
    count += s.count('o')
    count += s.count('u')
    return count > 2

def hasCharacterPairs(s):
    count = 0
    for c in range(ord('a'), ord('z')+1):
        if s.count(f'{chr(c)}{chr(c)}') > 0:
            count += 1
    return count > 0

def hasNoBadStrings(s):
    count = 0
    if s.count('ab') > 0:
        count += 1
    if s.count('cd') > 0:
        count += 1
    if s.count('pq') > 0:
        count += 1
    if s.count('xy') > 0:
        count += 1
    return count == 0

def part1(data):
    nice = 0
    for s in data:
        if hasAtLeast3Vowels(s) and hasCharacterPairs(s) and hasNoBadStrings(s):
            nice += 1
    return nice

def containsPairOf2Letters(s):
    for i in range(len(s) - 3):
        if s[i+2:].count(s[i:i+2]) > 0:
            return True
    return False

def containsLetterSeperateBy1(s):
    for i in range(len(s) - 2):
        if s[i] == s[i + 2]:
            return True
    return False

def part2(data):
    nice = 0
    for s in data:
        if containsPairOf2Letters(s) and containsLetterSeperateBy1(s):
            nice += 1
    return nice

if __name__ == '__main__':
    year = 2015
    day = 5
    data = getData(year, day)
    result1 = part1(data)              
    result2 = part2(data)              

    print(f'Results - {year}/{day:02d}:')
    print(f"Result 1 - {result1}") # 
    print(f"Result 2 - {result2}") # 