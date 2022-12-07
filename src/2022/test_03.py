import pytest
from day_03 import part1, part2

@pytest.fixture()
def testData():
    return '''vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw'''.split('\n')
    
def test_1_1(testData):
    assert part1(testData) == 157

def test_2_1(testData):
    assert part2(testData) == 70
