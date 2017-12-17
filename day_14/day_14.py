from puzzle_commons.puzzle_commons import read_puzzle_input
import os
from day_10 import day_10


def solve():
    """Advent Of Code 2017 - Day 14 Solution.
    :return: tuple(part_a_result[int], part_b_result[int])
    """
    puzzle_input = read_puzzle_input(os.path.dirname(os.path.abspath(__file__)), "day_14_input.txt")[0]

    C_FULL = "1"  # Constant for full disk block
    C_EMPTY = "0"  # Constant for empty disk block

    def get_knot_hash(input_string):
        # Initialize 256 knots, just like on day_10 part-B
        puzzle_knots = [i for i in range(256)]

        # Calculate lengths based on input + (17, 31, 73, 47, 23), just like on day_10 part-B
        lengths = tuple(ord(char) for char in input_string) + (17, 31, 73, 47, 23)

        # Get knot hash, by applying 64 transformations, just like on day_10 part-B
        knot_hash = day_10.knot_hash_n_times(puzzle_knots, lengths, 64)

        # Get dense hash of length 16, just like on day_10 part-B
        dense_hash = day_10.dense_hash(knot_hash, 16)

        # Transform dense hash into string of hexadecimal characters, just like on day_10 part-B
        hex_hash = ''.join(['{:02x}'.format(num_to_hex) for num_to_hex in dense_hash])

        return hex_hash

    def convert_hex_to_bin(hash_hex):
        binary_string = ""

        for char in hash_hex:
            binary_string += "{:04b}".format(int(char, base=16))

        return binary_string

    # Store disk representation in memory - disk_rows
    disk = []

    for row in range(0, 128):
        current_row_hash = get_knot_hash(puzzle_input + "-" + str(row))
        current_row_bin = convert_hex_to_bin(current_row_hash)
        disk.append(list(current_row_bin))

    def solve_a():
        """Advent Of Code 2017 - Day 14 - Part A Solution.
        """
        space_used = 0  # Answer for part-A

        for row in range(len(disk)):
            for col in range(len(disk[row])):
                if disk[row][col] == C_FULL:
                    space_used += 1

        return space_used

    def solve_b():
        """Advent Of Code 2017 - Day 14 - Part A Solution.
        """
        regions = 0  # Answer for part-B

        def clean_block(row, col):
            # Empty out current block and all adjacent blocks (if current block isn't empty)
            if disk[row][col] == C_FULL:
                disk[row][col] = C_EMPTY

                # Empty out block on same Y-position, on previous row (if we're not at top edge)
                if row > 0:
                    clean_block(row - 1, col)

                # Empty out block on same Y-position, on following row (if we're not at bottom edge)
                if row < len(disk) - 1:
                    clean_block(row + 1, col)

                # Empty out block on X-1 position of the same row (if we're not at left edge)
                if col > 0:
                    clean_block(row, col - 1)

                # Empty out block on X+1 position of the same row (if we're not at right edge)
                if col < len(disk[row]) - 1:
                    clean_block(row, col + 1)

        for row in range(len(disk)):
            for col in range(len(disk[row])):
                # If the block is full, increase number of regions and nuke the whole region
                if disk[row][col] == C_FULL:
                    regions += 1
                    clean_block(row, col)

        return regions

    return solve_a(), solve_b()
