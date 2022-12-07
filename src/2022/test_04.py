import pytest
from day_04 import part1, part2

@pytest.fixture()
def testData():
    return '''2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8'''.split('\n')
    
def test_1_1(testData):
    assert part1(testData) == 2

def test_2_1(testData):
    assert part2(testData) == 4
