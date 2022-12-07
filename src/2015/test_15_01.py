import pytest
from day_01 import part1, part2
    
def test_1_1():
    assert part1('()()') == 0
    
def test_1_2():
    assert part1('(())') == 0
    
def test_1_3():
    assert part1('(((') == 3
    
def test_1_4():
    assert part1('(()(()(') == 3
    
def test_1_5():
    assert part1('))(((((') == 3
    
def test_1_6():
    assert part1('())') == -1
    
def test_1_7():
    assert part1('))(') == -1
    
def test_1_8():
    assert part1(')))') == -3
    
def test_1_9():
    assert part1(')())())') == -3

def test_2_1():
    assert part2(')') == 1

def test_2_2():
    assert part2('()())') == 5
