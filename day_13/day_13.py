from puzzle_commons.puzzle_commons import read_puzzle_input
import os


def get_scanner_position(scanner_range, seconds_passed):
    """
    Returns scanner position after specified amount of time.
    """
    scanner_range -= 1  # Decrease range by one, e.g if scanner range is 3, it operates on 0, 1, 2 values
    scanner_position = seconds_passed % (
            scanner_range * 2)  # There are 2x scanner_range steps (range forward + range backward)

    if scanner_position > scanner_range:  # Scanner going backwards
        return (scanner_range * 2) - scanner_position
    else:  # Scanner going forwards
        return scanner_position


def solve():
    """Advent Of Code 2017 - Day 13 Solution.
    :return: tuple(part_a_result[int], part_b_result[int])
    """
    scanners = {}

    for puzzle_input in read_puzzle_input(os.path.dirname(os.path.abspath(__file__)), "day_13_input.txt"):
        # Strip whitespace, split by ": ", cast to integer
        scanner_depth, scanner_range = (int(param) for param in puzzle_input.strip().split(": "))

        scanners[scanner_depth] = scanner_range

    # Sort scanner levels
    # 1) Just in case, they came unsorted in input
    # 2) Python doesn't guarantee order of keys()
    scanner_levels = list(scanners.keys())
    scanner_levels.sort()

    def solve_a():

        severity = 0

        for scanner_level in scanner_levels:
            # Packet is falling through 0th position. If it meets with scanner, increase severity.
            if get_scanner_position(scanners[scanner_level], scanner_level) == 0:
                # add up depth * range
                severity += (scanner_level * scanners[scanner_level])

        return severity

    def solve_b():

        initial_delay = 0  # Set initial delay 0

        # Try passing the firewall, until the solution is found
        while True:
            firewall_passed = True

            for scanner in scanner_levels:
                # If the packet is blocked by firewall, increase initial delay and try again
                if get_scanner_position(scanners[scanner], scanner + initial_delay) == 0:
                    initial_delay += 1
                    firewall_passed = False
                    break

            # Break out of outer loop, when the firewall has been passed
            if firewall_passed:
                break

        return initial_delay

    return solve_a(), solve_b()
