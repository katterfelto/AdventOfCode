# import aocd
# from os.path import exists

######################################################
# Get the Input data
######################################################
# def getData(year, day):
#     data = None
#     if not exists(f'./inputData/{year}/{day:02d}.txt'):
#         with open(f'./inputData/{year}/{day:02d}.txt', 'w') as f:
#             f.write(aocd.get_data(day=day, year=year))
#     with open(f'inputData/{year}/{day:02d}.txt', 'r') as f:
#         data = f.read().split('\n')
#     return data

######################################################
# The solution
######################################################
import hashlib

def part1(data):
    i = 0
    while True:
        md5 = hashlib.md5(f"{data}{i}".encode('utf-8')).hexdigest()
        if md5.startswith('00000'):
            break
        i += 1
    return i

def part2(data):
    i = 0
    while True:
        md5 = hashlib.md5(f"{data}{i}".encode('utf-8')).hexdigest()
        if md5.startswith('000000'):
            break
        i += 1
    return i

if __name__ == '__main__':
    year = 2015
    day = 4
    data = 'bgvyzdsv' # getData(year, day)
    result1 = part1(data)              
    result2 = part2(data)              

    print(f'Results - {year}/{day:02d}:')
    print(f"Result 1 - {result1}") # 254575
    print(f"Result 2 - {result2}") # 1038736