from puzzle_commons.puzzle_commons import read_puzzle_input
import os


def solve():
    """Advent Of Code 2017 - Day 05 Solution.
    :return: tuple(part_a_result[int], part_b_result[int])
    """

    # Read puzzle input, cast to integer and store in list
    input_instructions = [int(puzzle_input) for puzzle_input in
                          read_puzzle_input(os.path.dirname(os.path.abspath(__file__)), "day_05_input.txt")]

    def steps_required_to_reach_exit(jump_instructions, offset_adjustment_fn):
        """Returns number of steps required to exit from list of offset / instructions.
        :param jump_instructions: list([integer]) list of instructions / offsets
        :param offset_adjustment_fn: function accepting single [integer] offset, returning [integer] value to be added to index in each step
        :return: [integer] number of instructions
        """
        # Create copy of instructions list in order to avoid modifying input list directly
        jump_instructions = jump_instructions[:]

        steps_to_exit_instructions = 0
        i = 0

        # Loop until instruction index is inside range of instructions
        while i < len(jump_instructions):
            # Load this instruction / offset
            offset = jump_instructions[i]

            # Modify current offset using the offset adjustment function
            jump_instructions[i] += offset_adjustment_fn(offset)

            # Adjust index by current offset
            i += offset

            steps_to_exit_instructions += 1

        return steps_to_exit_instructions

    return steps_required_to_reach_exit(input_instructions, lambda x: 1), \
           steps_required_to_reach_exit(input_instructions, lambda x: -1 if x >= 3 else 1)
