from puzzle_commons.puzzle_commons import read_puzzle_input
import os
import itertools


def solve():
    """Advent Of Code 2017 - Day 02 Solution.

    :return: tuple(part_a_result[int], part_b_result[int])
    """

    part_a_result = 0
    part_b_result = 0

    INPUT_DELIMITER = "	"

    for puzzle_input in read_puzzle_input(os.path.dirname(os.path.abspath(__file__)), "day_02_input.txt"):
        numbers_on_line = [int(number) for number in puzzle_input.rstrip().split(INPUT_DELIMITER)]

        # Part-A
        part_a_result += max(numbers_on_line) - min(numbers_on_line)

        # Part-B
        part_b_result += sum(
            div_wo_rem[0] // div_wo_rem[1] for div_wo_rem in itertools.permutations(numbers_on_line, 2) if
            div_wo_rem[0] % div_wo_rem[1] == 0)

    return part_a_result, part_b_result
