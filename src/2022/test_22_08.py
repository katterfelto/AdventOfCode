import pytest
from day_08 import part1, part2, calculateScenicScore

@pytest.fixture()
def testData():
    return '''30373
25512
65332
33549
35390'''.split('\n')
    
def test_1_1(testData):
    assert part1(testData) == 21

def test_2_1(testData):
    assert calculateScenicScore(testData, 1, 2) == 4

def test_2_2(testData):
    assert calculateScenicScore(testData, 3, 2) == 8

def test_2_3(testData):
    assert part2(testData) == 8