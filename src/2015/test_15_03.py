import pytest
from day_03 import part1, part2
    
def test_1_1():
    assert part1('>') == 2
    
def test_1_2():
    assert part1('^>v<') == 4
    
def test_1_3():
    assert part1('^v^v^v^v^v') == 2
    
def test_2_1():
    assert part2('^v') == 3
    
def test_2_2():
    assert part2('^>v<') == 3
    
def test_2_3():
    assert part2('^v^v^v^v^v') == 11
    
