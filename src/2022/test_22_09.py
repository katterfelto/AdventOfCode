import pytest
from day_09 import part1, part2, adjustTail

@pytest.fixture()
def testData1():
    return '''R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2'''.split('\n')

@pytest.fixture()
def testData2():
    return '''R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20'''.split('\n')
    
def test_1_1():
    assert adjustTail([1,0], [0,0]) == [0,0]
    
def test_1_2():
    assert adjustTail([2,0], [0,0]) == [1,0]
    
def test_1_3():
    assert adjustTail([0,0], [0,2]) == [0,1]
    
def test_1_4():
    assert adjustTail([0,0], [2,2]) == [1,1]
    
def test_1_5():
    assert adjustTail([0,0], [2,1]) == [1,0]
    
def test_1_6():
    assert adjustTail([1,4], [0,3]) == [0,3]
    
def test_1_7():
    assert adjustTail([2,4], [0,3]) == [1,4]
    
def test_1_8(testData1):
    assert part1(testData1) == 13
    
def test_2_1(testData1):
    assert part2(testData1) == 1
    
def test_2_2(testData2):
    assert part2(testData2) == 36
    