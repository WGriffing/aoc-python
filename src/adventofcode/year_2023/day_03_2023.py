import re

from adventofcode.util.exceptions import SolutionNotFoundError
from adventofcode.registry.decorators import register_solution
from adventofcode.util.input_helpers import get_input_for_day


class Match:
    def __init__(self, line_num: int, line: str, match: re.Match):
        self.line: str = line
        self.line_num: int = line_num
        self.start: int = match.start()
        self.end: int = match.end() - 1


class Number(Match):
    def __init__(self, line_num: int, line: str, match: re.Match):
        super().__init__(line_num, line, match)
        self.value: int = int(match.group(1))


class Symbol(Match):
    def __init__(self, line_num: int, line: str, match: re.Match):
        super().__init__(line_num, line, match)
        self.value: str = str(match.group(1))


def find_matches(line: str, pattern) -> list[Match]:
    pattern = re.compile(pattern)
    matches = pattern.finditer(line)

    return matches


def find_numbers(line_num: int, line: str) -> list[Number]:
    numbers: [Number] = []

    matches = find_matches(line, r'(\d+)')

    for match in matches:
        number = Number(line_num, line, match)
        numbers.append(number)

    return numbers


def find_symbols(line_num: int, line: str) -> list[Symbol]:
    symbols: [Symbol] = []

    # regex pattern that excludes digits and periods
    pattern = r'([^0-9.])'
    matches = find_matches(line, pattern)

    for match in matches:
        symbol = Symbol(line_num, line, match)
        symbols.append(symbol)

    return symbols


def find_gears(line_num: int, line: str) -> list[Symbol]:
    gears: [Symbol] = []

    # regex pattern that excludes digits and periods
    pattern = r'(\*)'
    matches = find_matches(line, pattern)

    for match in matches:
        gear = Symbol(line_num, line, match)
        gears.append(gear)

    return gears


def range_check(number: Number, symbol: Symbol) -> bool:
    return (symbol.start in range(number.start-1, number.end+2) and
            symbol.line_num-1 <= number.line_num <= symbol.line_num+1)


def is_valid_number(number: Number, symbols: [Symbol]) -> bool:
    for symbol in symbols:
        if range_check(number, symbol):
            return True

    return False


@register_solution(2023, 3, 1)
def part_one(input_data: list[str]):

    numbers = []
    symbols = []
    for line_num, line in enumerate(input_data):
        numbers.extend(find_numbers(line_num, line))
        symbols.extend(find_symbols(line_num, line))

    answer = 0
    for number in numbers:
        if is_valid_number(number, symbols):
            answer += number.value

    if not answer:
        raise SolutionNotFoundError(2023, 3, 1)

    return answer


@register_solution(2023, 3, 2)
def part_two(input_data: list[str]):

    numbers = []
    gears = []

    for line_num, line in enumerate(input_data):
        numbers.extend(find_numbers(line_num, line))
        gears.extend(find_gears(line_num, line))

    answer = 0
    for g, gear in enumerate(gears):
        gear_num = -1
        number_1 = number_2 = None
        for number in numbers:
            pass_gear_check = range_check(number, gear)
            if pass_gear_check and gear_num < 0:
                gear_num = g
                if not number_1:
                    number_1 = number.value
            elif pass_gear_check and gear_num >= 0:
                if gear_num == g and not number_2:
                    number_2 = number.value
                else:
                    number_1 = number_2 = None
                    gear_num = -1

            if number_1 and number_2:
                answer += number_1 * number_2
                break

    if not answer:
        raise SolutionNotFoundError(2023, 3, 2)

    return answer


if __name__ == '__main__':
    data = get_input_for_day(2023, 3)
    part_one(data)
    part_two(data)
