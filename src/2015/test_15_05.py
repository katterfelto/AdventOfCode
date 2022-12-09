import pytest
from day_05 import part1, part2
from day_05 import hasAtLeast3Vowels, hasCharacterPairs, hasNoBadStrings
from day_05 import containsPairOf2Letters, containsLetterSeperateBy1


def test_0_1():
    assert hasAtLeast3Vowels('aeiou') == True

def test_0_2():
    assert hasCharacterPairs('abba') == True

def test_0_3():
    assert hasNoBadStrings('abba') == False

def test_0_4():
    assert containsPairOf2Letters('aaaa') == True
    
def test_0_5():
    assert containsPairOf2Letters('gbbbg') == False
    
def test_0_6():
    assert containsPairOf2Letters('bbxxbb') == True
    
def test_0_7():
    assert containsLetterSeperateBy1('gbbbg') == True
    
def test_0_8():
    assert containsLetterSeperateBy1('xyx') == True

def test_0_9():
    assert containsPairOf2Letters('xyzxy') == True
    
def test_1_1():
    assert part1(['ugknbfddgicrmopn']) == 1
    
def test_1_2():
    assert part1(['aaa']) == 1
    
def test_1_3():
    assert part1(['jchzalrnumimnmhp']) == 0
    
def test_1_4():
    assert part1(['haegwjzuvuyypxyu']) == 0
    
def test_1_5():
    assert part1(['dvszwmarrgswjxmb']) == 0
    
def test_2_1():
    assert part2(['qjhvhtzxzqqjkmpb']) == 1
    
def test_2_2():
    assert part2(['xxyxx']) == 1
    
def test_2_3():
    assert part2(['uurcxstgmygtbstg']) == 0
    
def test_2_4():
    assert part2(['ieodomkazucvgmuy']) == 0
    
