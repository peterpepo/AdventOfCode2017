from puzzle_commons.puzzle_commons import read_puzzle_input
import os


def solve():
    """Advent Of Code 2017 - Day 01 Solution.

    :return: tuple(part_a_result[int], part_b_result[int])
    """

    def circular_buffer_position(length, offset, order):
        return (offset + order) % length

    # Read first line from the input file
    try:
        puzzle_input = read_puzzle_input(os.path.dirname(os.path.abspath(__file__)), "day_01_input.txt")[0]
    except IndexError:
        return -1, -1

    # Part-A
    part_a_result = sum(int(puzzle_input[i]) for i in range(len(puzzle_input)) if
                        puzzle_input[i] == puzzle_input[circular_buffer_position(len(puzzle_input), i, 1)])

    # Part-B
    part_b_result = sum(int(puzzle_input[i]) for i in range(len(puzzle_input)) if
                        puzzle_input[i] == puzzle_input[
                            circular_buffer_position(len(puzzle_input), i, len(puzzle_input) // 2)])

    return part_a_result, part_b_result
