from puzzle_commons.puzzle_commons import read_puzzle_input
import os

def solve():
    """Advent Of Code 2017 - Day 17 Solution.
    :return: tuple(part_a_result[int], part_b_result[int])
    """
    puzzle_input = int(read_puzzle_input(os.path.dirname(os.path.abspath(__file__)), "day_17_input.txt")[0])

    def solve_a():
        """Advent Of Code 2017 - Day 17 - Part A Solution.
        """
        buffer = [0]
        current_position = 0
        loop_times = 2017

        part_a_result = 0

        # Calculate all values in buffer
        for i in range(1, loop_times+1):
            current_position = ((current_position + puzzle_input) % len(buffer)) + 1
            buffer.insert(current_position, i)

        # Get value immediate following one, which has been populated last
        for j in range(len(buffer)):
            if buffer[j] == loop_times:
                part_a_result = buffer[j+1]
                break

        return part_a_result

    def solve_b():
        """Advent Of Code 2017 - Day 17 - Part B Solution.
        """
        current_position = 0
        buffer_length = 1
        loop_times = 50000000

        part_b_result = 0

        # Calculated values are not stored, since we are interested in one on 1st position only
        for i in range(1, loop_times+1):
            current_position = ((current_position + puzzle_input) % buffer_length) + 1
            buffer_length += 1

            # Remember iteration, which caused value to be written to position 1
            if current_position == 1:
                part_b_result = i

        return part_b_result

    return solve_a(), solve_b()