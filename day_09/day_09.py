from puzzle_commons.puzzle_commons import read_puzzle_input
import os


def solve():
    """Advent Of Code 2017 - Day 09 Solution.
    :return: tuple(part_a_result[int], part_b_result[int])
    """

    puzzle_input = read_puzzle_input(os.path.dirname(os.path.abspath(__file__)), "day_09_input.txt")[0]

    def solve_a():
        """Advent Of Code 2017 - Day 09 - Part A Solution.
        """
        total_score = 0
        score_multipler = 0
        inside_junk = False

        i = 0
        while i < len(puzzle_input):
            if not inside_junk:
                if puzzle_input[i] == "{":
                    score_multipler += 1

                elif puzzle_input[i] == "}":
                    total_score += score_multipler
                    score_multipler -= 1

                elif puzzle_input[i] == "<":
                    inside_junk = True

            elif inside_junk:
                if puzzle_input[i] == ">":
                    inside_junk = False

                elif puzzle_input[i] == "!":
                    i += 1
            i += 1
        return total_score

    def solve_b():
        """Advent Of Code 2017 - Day 10 - Part B Solution.
        """
        garbage_count = 0
        inside_junk = False

        i = 0
        while i < len(puzzle_input):
            if not inside_junk and puzzle_input[i] == "<":
                inside_junk = True
            elif inside_junk:
                if puzzle_input[i] == ">":
                    inside_junk = False

                elif puzzle_input[i] == "!":
                    i += 1

                else:
                    garbage_count += 1
            i += 1
        return garbage_count

    return solve_a(), solve_b()