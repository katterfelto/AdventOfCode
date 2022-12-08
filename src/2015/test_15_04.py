import pytest
from day_04 import part1, part2
    
def test_1_1():
    assert part1('abcdef') == 609043
    
def test_1_2():
    assert part1('pqrstuv') == 1048970
    
