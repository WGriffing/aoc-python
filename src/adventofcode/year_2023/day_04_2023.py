import re

from adventofcode.util.exceptions import SolutionNotFoundError
from adventofcode.registry.decorators import register_solution
from adventofcode.util.input_helpers import get_input_for_day


def parse_line(line: str):
    card_pattern = r'Card\s+(\d+): '
    card_num = re.search(card_pattern, line).group(1)

    groups = re.sub(card_pattern, '', line).split(' | ')

    winning = [int(x) for x in groups[0].split()]
    mine = [int(y) for y in groups[1].split()]

    return int(card_num), winning, mine


def calculate_number_of_cards(winning: list[int], mine: list[int]) -> int:
    wins = set(winning) & set(mine)

    win_count = len(wins)

    return win_count


def calculate_points(winning: list[int], mine: list[int]) -> int:
    win_count = calculate_number_of_cards(winning, mine)

    if win_count:
        return 2**(win_count - 1)

    return 0


@register_solution(2023, 4, 1)
def part_one(input_data: list[str]):
    answer = 0

    for line in input_data:
        _c, winning, mine = parse_line(line)
        answer += calculate_points(winning, mine)

    if not answer:
        raise SolutionNotFoundError(2023, 4, 1)

    return answer


@register_solution(2023, 4, 2)
def part_two(input_data: list[str]):
    answer = 0

    cards = {}
    for line in input_data:
        card_num, winning, mine = parse_line(line)
        cards[card_num] = cards[card_num] + 1 if card_num in cards else 1
        multiplier = cards[card_num]
        new_win_count = calculate_number_of_cards(winning, mine)

        for c in range(card_num + 1, card_num + new_win_count + 1):
            cards[c] = cards[c] + 1*multiplier if c in cards else 1*multiplier

    for _k, v in cards.items():
        answer += v

    if not answer:
        raise SolutionNotFoundError(2023, 4, 2)

    return answer


if __name__ == '__main__':
    data = get_input_for_day(2023, 4)
    part_one(data)
    part_two(data)
