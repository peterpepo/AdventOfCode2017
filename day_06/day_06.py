from puzzle_commons.puzzle_commons import read_puzzle_input
import os

def solve():
    """Advent Of Code 2017 - Day 06 Solution.
    :return: tuple(part_a_result[int], part_b_result[int])
    """
    puzzle_input = [int(puzzle_input) for puzzle_input in
                          read_puzzle_input(os.path.dirname(os.path.abspath(__file__)), "day_06_input.txt")[0].split("	")]

    class MemoryBank:
        def __init__(self, memory_bank_state):
            self.memory_bank_state = memory_bank_state[:]
            self.seen_states = []

        def redistribute_fullest_block(self):
            fullest_block_index = None

            # Find fullest memory block
            for i in range(len(self.memory_bank_state)):
                if fullest_block_index is None or self.memory_bank_state[i] > self.memory_bank_state[fullest_block_index]:
                    fullest_block_index = i

            # Clear out fullest block
            amount_to_redistribute = self.memory_bank_state[fullest_block_index]
            self.memory_bank_state[fullest_block_index] = 0

            # Redistribute amount to other blocks
            next_register_index = fullest_block_index + 1

            while amount_to_redistribute > 0:
                self.memory_bank_state[next_register_index%len(self.memory_bank_state)] += 1
                next_register_index += 1
                amount_to_redistribute -= 1

        def reallocate(self):
            total_steps = 0

            while tuple(self.memory_bank_state) not in self.seen_states:
                self.seen_states.append(tuple(self.memory_bank_state))
                self.redistribute_fullest_block()
                total_steps += 1

            return total_steps

        def distance_from_state_to_state(self):

            return len(self.seen_states) - self.seen_states.index(tuple(self.memory_bank_state))

    memory_bank_one = MemoryBank(puzzle_input)

    return memory_bank_one.reallocate(), memory_bank_one.distance_from_state_to_state()
