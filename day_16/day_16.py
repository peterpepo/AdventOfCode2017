from puzzle_commons.puzzle_commons import read_puzzle_input, char_range
import os


class DancingList:
    def __init__(self, init_values):
        self.values = init_values[:]

    def spin(self, amount):
        self.values = self.values[-amount:] + self.values[:-amount]

    def swap_index(self, idx_a, idx_b):
        self.values[idx_a], self.values[idx_b] = self.values[idx_b], self.values[idx_a]

    def swap_member(self, member_a, member_b):
        idx_a = self.values.index(member_a)
        idx_b = self.values.index(member_b)

        self.swap_index(idx_a, idx_b)

    def get_values(self):
        return self.values


def solve():
    """Advent Of Code 2017 - Day 16 Solution.
    :return: tuple(part_a_result[int], part_b_result[int])
    """
    def dance_n_times(dance_moves, times):
        programs_init = [char for char in char_range('a', 'p')]
        seen_states = []

        dlist = DancingList(programs_init)

        for time in range(times):

            seen_hash = ''.join(dlist.get_values())

            if seen_hash in seen_states:
                return (seen_states[times % time])
            seen_states.append(seen_hash)

            for dance_move in dance_moves:
                if dance_move.startswith("s"):
                    dance_move = dance_move[1:]
                    dlist.spin(int(dance_move))

                elif dance_move.startswith("x"):
                    dance_move = dance_move[1:]
                    idx_a, idx_b = map(int, dance_move.split("/"))
                    dlist.swap_index(idx_a, idx_b)

                elif dance_move.startswith("p"):
                    dance_move = dance_move[1:]
                    member_a, member_b = dance_move.split("/")
                    dlist.swap_member(member_a, member_b)

        return ''.join(dlist.get_values())

    puzzle_input = read_puzzle_input(os.path.dirname(os.path.abspath(__file__)), "day_16_input.txt")[0].split(",")

    return dance_n_times(puzzle_input, 1), dance_n_times(puzzle_input, 1000000000)
