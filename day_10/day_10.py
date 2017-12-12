from puzzle_commons.puzzle_commons import read_puzzle_input
import os


def knot_hash(input_array, offset, length):
    """
    Returns knot hash of array passed as input.
    """
    hashed_array = list(input_array)

    for i in range(length):
        replaced_position = (offset + i) % len(input_array)
        replaced_by_position = (offset + length - i - 1) % len(input_array)
        hashed_array[replaced_position] = input_array[replaced_by_position]

    return hashed_array


def knot_hash_n_times(input_array, lengths, times):
    """
    Applies knot hash of [lengths] lengths [n] times on input and returns result.
    Skip size and current position variables are preserved between applications of knot hash.
    """
    current_position = 0
    skip_size = 0

    for n in range(times):
        for length in lengths:
            input_array = knot_hash(input_array, current_position, length)
            current_position += length
            current_position += skip_size
            skip_size += 1

    return input_array


def dense_hash(input_array, base):
    """
    Returns dense hash of input array.
    Input array is split into [input_array//base] parts.
    Members of each part are xor-ed and added to result.
    """
    dense_hash_result = []

    for i in range(len(input_array) // base):
        xor_result = 0
        numbers_to_xor = input_array[i * base:(i + 1) * base]

        for number_to_xor in numbers_to_xor:
            xor_result = xor_result ^ number_to_xor

        dense_hash_result.append(xor_result)

    return dense_hash_result


def solve():
    puzzle_input = read_puzzle_input(os.path.dirname(os.path.abspath(__file__)), "day_10_input.txt")[0].strip()
    puzzle_knots = [i for i in range(256)]

    part_a_input = tuple(int(input_number) for input_number in puzzle_input.split(","))
    part_a_hashed = knot_hash_n_times(puzzle_knots, part_a_input, 1)
    part_a_result = part_a_hashed[0] * part_a_hashed[1]

    part_b_lengths = tuple(ord(char) for char in puzzle_input) + (17, 31, 73, 47, 23)
    part_b_knot_hash = knot_hash_n_times(puzzle_knots, part_b_lengths, 64)
    part_b_dense_hash = dense_hash(part_b_knot_hash, 16)
    part_b_result = ''.join(['{:02x}'.format(num_to_hex) for num_to_hex in part_b_dense_hash])

    return part_a_result, part_b_result
