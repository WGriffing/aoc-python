from adventofcode.util.exceptions import SolutionNotFoundError
from adventofcode.registry.decorators import register_solution
from adventofcode.util.input_helpers import get_input_for_day


DIGITS = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}


def get_calibration_value(inp: str, with_words: bool = False) -> int:
    # replace all words (keys in the DIGITS dict) with their corresponding values
    corrected = inp
    if with_words:
        first = None
        first_index = len(inp)-1
        last = None
        last_index = 0
        for key, _value in DIGITS.items():
            if inp.find(key) < first_index and inp.find(key) != -1:
                first = key
                first_index = inp.find(key)
            if inp.rfind(key) > last_index and inp.rfind(key) != -1:
                last = key
                last_index = inp.rfind(key)

        corrected = corrected.replace(
            first, DIGITS[first]) if first else corrected
        corrected = corrected.replace(
            last, DIGITS[last]) if last else corrected
    # print(corrected)
    digits = [str(x) for x in corrected if x.isdigit()]
    # print(digits)
    return int(digits[0] + digits[-1])


@register_solution(2023, 1, 1)
def part_one(input_data: list[str]):
    answer = sum(get_calibration_value(x, False) for x in input_data)

    if not answer:
        raise SolutionNotFoundError(2023, 1, 1)

    return answer


@register_solution(2023, 1, 2)
def part_two(input_data: list[str]):
    answer = sum(get_calibration_value(x, True) for x in input_data)

    if not answer:
        raise SolutionNotFoundError(2023, 1, 2)

    return answer


if __name__ == '__main__':
    data = get_input_for_day(2023, 1)
    part_one(data)
    part_two(data)
