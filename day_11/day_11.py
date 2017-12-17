from puzzle_commons.puzzle_commons import read_puzzle_input
import os


def hexagrid_distance(point_a, point_b):
    return sum(map((lambda tup: abs(tup[0] - tup[1])), zip(point_a, point_b))) // 2


def solve():
    """Advent Of Code 2017 - Day 11 Solution.
    I suggest to visit https://www.redblobgames.com/grids/hexagons/ for great information on hexagrid and it's representation.
    :return: tuple(part_a_result[int], part_b_result[int])
    """

    # Directions constants
    N = (0, 1, -1)
    S = tuple(-x for x in N)  # Opposite direction to (N)orth
    NE = (1, 0, -1)
    SW = tuple(-x for x in NE)
    SE = (1, -1, 0)
    NW = tuple(-x for x in SE)

    directions = {"n": N, "s": S, "ne": NE, "sw": SW, "se": SE, "nw": NW}

    # Initial point
    initial_point = (0, 0, 0)

    def solve_a():
        """Advent Of Code 2017 - Day 11 - Part A Solution.
        """
        target_point = initial_point[:]

        for direction in read_puzzle_input(os.path.dirname(os.path.abspath(__file__)), "day_11_input.txt")[0].split(
                ","):
            target_point = tuple(a + b for a, b in zip(target_point, directions[direction]))

        return hexagrid_distance(target_point, initial_point)

    def solve_b():
        """Advent Of Code 2017 - Day 11 - Part B Solution.
        """
        target_point = initial_point[:]
        furthest_from_init = 0

        for direction in read_puzzle_input(os.path.dirname(os.path.abspath(__file__)), "day_11_input.txt")[0].split(
                ","):
            target_point = tuple(a + b for a, b in zip(target_point, directions[direction]))

            distance_from_start = hexagrid_distance(target_point, initial_point)
            # Remember distance, if we're further from init than before
            if distance_from_start > furthest_from_init:
                furthest_from_init = distance_from_start

        return furthest_from_init

    return solve_a(), solve_b()
