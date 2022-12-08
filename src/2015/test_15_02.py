import pytest
from day_02 import part1, part2
    
def test_1_1():
    assert part1(['2x3x4']) == 58
    
def test_1_2():
    assert part1(['1x1x10']) == 43

def test_2_1():
    assert part2(['2x3x4']) == 34

def test_2_2():
    assert part2(['1x1x10']) == 14
