import pytest
from day_05 import part1, part2

@pytest.fixture()
def testData():
    return '''[   [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2'''.split('\n')
    
def test_1_1(testData):
    assert part1(testData) == 'CMZ'

def test_2_1(testData):
    assert part2(testData) == 'MCD'
