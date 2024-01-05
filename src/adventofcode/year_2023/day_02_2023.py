import re

from adventofcode.util.exceptions import SolutionNotFoundError
from adventofcode.registry.decorators import register_solution
from adventofcode.util.input_helpers import get_input_for_day


def parse_reveals(inp: str):  # -> tuple[int, int, int]:

    red = re.search(r'(\d+) red', inp)
    green = re.search(r'(\d+) green', inp)
    blue = re.search(r'(\d+) blue', inp)

    return (int(red.group(1)) if red else 0,
            int(green.group(1)) if green else 0,
            int(blue.group(1)) if blue else 0)


class Reveal:
    def __init__(self, inp: str, turn: int):
        red, green, blue = parse_reveals(inp)

        self.turn = turn
        self.red = red
        self.green = green
        self.blue = blue


def split_line(line: str):
    # locate a string that looks like "Game 1: " and keep only the 1 using regex
    game_number = re.search(r'Game (\d+):', line).group(1)

    color_string = re.search(r': (.*)', line).group(1)

    reveal_strs = color_string.split('; ')
    reveals: [Reveal] = []
    for index, reveal in enumerate(reveal_strs):
        reveals.append(Reveal(reveal, index))

    return int(game_number), reveals


def is_possible(line: str, red_lim: int, green_lim: int, blue_lim: int) -> int:

    game_number, reveals = split_line(line)

    if all(reveal.red <= red_lim and reveal.green <= green_lim and reveal.blue <= blue_lim for reveal in reveals):
        return game_number

    return 0


def find_power(line: str) -> int:
    _game_number, reveals = split_line(line)

    red = max(reveal.red for reveal in reveals)
    green = max(reveal.green for reveal in reveals)
    blue = max(reveal.blue for reveal in reveals)

    return red * green * blue


@register_solution(2023, 2, 1)
def part_one(input_data: list[str]):

    answer = sum(is_possible(x, 12, 13, 14) for x in input_data)

    if not answer and answer != 0:
        raise SolutionNotFoundError(2023, 2, 1)

    return answer


@register_solution(2023, 2, 2)
def part_two(input_data: list[str]):
    answer = sum(find_power(x) for x in input_data)

    if not answer:
        raise SolutionNotFoundError(2023, 2, 2)

    return answer


if __name__ == '__main__':
    data = get_input_for_day(2023, 2)
    part_one(data)
    part_two(data)
