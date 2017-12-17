from puzzle_commons.puzzle_commons import read_puzzle_input
import os


def solve():
    """Advent Of Code 2017 - Day 15 Solution.
    :return: tuple(part_a_result[int], part_b_result[int])
    """

    def generate_value_with_criteria(initial_value, factor, criteria=1):
        """Gets next value for iterator, which fits condition new_value%criteria == 0.
        """
        # Repeat, until suitable value is found
        while True:
            initial_value = (initial_value * factor) % 2147483647

            if (initial_value % criteria) == 0:
                return initial_value

    def solve_puzzle(generator_one, generator_two, iterations):
        matches_found = 0

        for i in range(iterations):
            # Compare last 16 bits of each generator
            if generator_one[0] & 0xFFFF == generator_two[0] & 0xFFFF:
                matches_found += 1

            generator_one[0] = generate_value_with_criteria(*generator_one)
            generator_two[0] = generate_value_with_criteria(*generator_two)

        return matches_found

    # Read puzzle input
    generator_initial_values = [int(initial_value[24:]) for initial_value in
                                read_puzzle_input(os.path.dirname(os.path.abspath(__file__)), "day_15_input.txt")]
    generator_one = [generator_initial_values[0]] + [16807]  # Value read from input + step size from requirements
    generator_two = [generator_initial_values[1]] + [48271]  # Value read from input + step size from requirements

    def solve_a():
        """Advent Of Code 2017 - Day 15 - Part A Solution.
        """
        puzzle_a_generators = (generator_one[:], generator_two[:])  # Copy generators read from puzzle
        return solve_puzzle(*puzzle_a_generators, 40000000)

    def solve_b():
        """Advent Of Code 2017 - Day 15 - Part B Solution.
        """
        # Copy generators read from puzzle input and add conditions given by requirements
        puzzle_b_generators = (generator_one[:] + [4], generator_two[:] + [8])
        return solve_puzzle(*puzzle_b_generators, 5000000)

    return solve_a(), solve_b()
