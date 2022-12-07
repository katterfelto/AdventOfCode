from day_06 import part1, part2

def test_1_1():
    assert part1('mjqjpqmgbljsphdztnvjfqwrcgsmlb') == 7

def test_1_2():
    assert part1('bvwbjplbgvbhsrlpgdmjqwftvncz') == 5

def test_1_3():
    assert part1('nppdvjthqldpwncqszvftbrmjlhg') == 6

def test_1_4():
    assert part1('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg') == 10

def test_1_5():
    assert part1('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw') == 11

def test_2_1():
    assert part2('mjqjpqmgbljsphdztnvjfqwrcgsmlb') == 19

def test_2_2():
    assert part2('bvwbjplbgvbhsrlpgdmjqwftvncz') == 23

def test_2_3():
    assert part2('nppdvjthqldpwncqszvftbrmjlhg') == 23

def test_2_4():
    assert part2('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg') == 29

def test_2_5():
    assert part2('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw') == 26