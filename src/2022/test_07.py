import pytest
from day_07 import part1, part2, totalDiskUsage

@pytest.fixture()
def testData():
    return '''$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k'''.split('\n')

def test_0_0(testData):
    assert totalDiskUsage(testData) == 48381165
    
def test_1_1(testData):
    assert part1(testData) == 95437

def test_2_1(testData):
    assert part2(testData) == 'd'
