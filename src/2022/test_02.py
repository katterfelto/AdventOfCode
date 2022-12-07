import pytest
from day_02 import part1, part2

@pytest.fixture()
def testData():
    return '''A Y
B X
C Z'''.split('\n')
    
def test_1_1(testData):
    assert part1(testData) == 15

def test_2_1(testData):
    assert part2(testData) == 12
