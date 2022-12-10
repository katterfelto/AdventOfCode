import pytest
from day_06 import part1, part2
from day_06 import turnOn, turnOff, toggle

@pytest.fixture()
def testData1():
    return '''turn on 0,0 through 9,9
toggle 0,0 through 9,0
turn off 4,4 through 5,5'''.split('\n')

@pytest.fixture()
def testData2():
    return '''turn on 0,0 through 999,999
toggle 0,0 through 999,0
turn off 499,499 through 500,500'''.split('\n')
    
def test_1_1(testData1):
    assert part1(testData1) == 86
    
def test_1_2(testData2):
    assert part1(testData2) == 998996
