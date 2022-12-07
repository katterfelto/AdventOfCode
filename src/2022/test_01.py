import pytest
from day_01 import part1, part2

@pytest.fixture()
def testData():
    return '''1000
2000
3000

4000

5000
6000

7000
8000
9000

10000'''.split('\n')
    
def test_1_1(testData):
    assert part1(testData) == 24000

def test_2_1(testData):
    assert part2(testData) == 45000
