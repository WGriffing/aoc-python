from adventofcode.year_2023.day_03_2023 import part_two, part_one


test_input = [
    '467..114..',
    '...*......',
    '..35..633.',
    '......#...',
    '617*......',
    '.....+.58.',
    '..592.....',
    '......755.',
    '...$.*....',
    '.664.598..'
]


def test_part_one():
    assert part_one(test_input) == 4361


def test_part_two():
    assert part_two(test_input) == 467835
