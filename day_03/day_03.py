from puzzle_commons.puzzle_commons import read_puzzle_input, memoize
import os


def solve():
    puzzle_input = read_puzzle_input(os.path.dirname(os.path.abspath(__file__)), "day_03_input.txt")[0]
    puzzle_input = int(puzzle_input)

    def nth_member_pos_on_spiral(member_order, center_align=False):
        """Returns (x,y) position of a n-th member on number spiral.
        Number spiral: https://en.wikipedia.org/wiki/Ulam_spiral.
        Example of number spiral:
        17  16  15  14  13
        18  5   4   3   12
        19  6   1   2   11
        20  7   8   9   10  ...
        21  22  23  24  25  26

        :param member_order: [int] order of member, which coordinations are returned
        :param center_align: [boolean] centers first element (1) to [0,0] in a grid
        :return: (x,y) position of n-th number in a spiral
        """

        def member_order_on_square(edge_length, member_order):
            """Finds order of element [member_order] in spiral with edge of [edge_length] length.
            Spiral starts in lower bottom corner; y-1

            :param edge_length:
            :param member_order:
            :return:
            """
            minimum_value_on_square = (edge_length) ** 2 - 4 * (edge_length - 1) + 1
            order_on_square = member_order - minimum_value_on_square + 1

            return order_on_square

        def find_square_edge_length(number_to_acomodate):
            """Finds edge_length of square on which [number_to_acomodate] lies.
            :param number_to_acomodate:
            :return:
            """
            square_edge = 1

            while square_edge ** 2 < number_to_acomodate:
                square_edge += 2

            return square_edge

        edge_length = find_square_edge_length(member_order)

        order_on_square = member_order_on_square(edge_length, member_order)

        # Number lies on first edge (from initial point to upper-right corner)
        if order_on_square <= (edge_length - 1):
            pos_x = edge_length
            pos_y = order_on_square + 1
        # Number lies on second edge (from upper-right to upper-left corner)
        elif order_on_square <= 2 * (edge_length - 1):
            pos_x = edge_length - (order_on_square - (edge_length - 1))
            pos_y = edge_length
        # Number lies on third edge (from upper-left to bottom-left corner)
        elif order_on_square <= 3 * (edge_length - 1):
            pos_x = 1
            pos_y = edge_length - (order_on_square - 2 * (edge_length - 1))
        # Number lies on fourth edge (from bottom-left to bottom-right corner)
        else:
            pos_x = (order_on_square - 3 * (edge_length - 1)) + 1
            pos_y = 1

        # Optionally align first element to [0,0]
        if center_align:
            pos_x -= edge_length // 2 + 1
            pos_y -= edge_length // 2 + 1

        return pos_x, pos_y

    def manhattan_distance(point_a, point_b):
        """Calculates Manhattan distance between two points.
        :param point_a:
        :param point_b:
        :return:
        """
        return abs(point_a[0] - point_b[0]) + abs(point_a[1] - point_b[1])

    def order_based_on_position(point):
        """Returns order of member in number spiral, based on (x,y) position.
        Number spiral: https://en.wikipedia.org/wiki/Ulam_spiral.
        Example of number spiral:
        17  16  15  14  13
        18  5   4   3   12
        19  6   1   2   11
        20  7   8   9   10  ...
        21  22  23  24  25  26

        :param point: (x,y) position in grid
        :return: [int] order of a member
        """

        if point == (0, 0):
            return 1
        edge_length = max(abs(point[0]), abs(point[1])) * 2 + 1

        edge_radius = edge_length // 2

        starting_point = (edge_radius, -edge_radius + 1)

        x, y = point

        # Number lies on first edge (from initial point to upper-right corner)
        if x == starting_point[0] and y >= starting_point[1]:
            distance = manhattan_distance(starting_point, point)
        # Number lies on second edge (from upper-right to upper-left corner)
        elif x <= starting_point[0] and y == edge_radius:
            distance = manhattan_distance(starting_point, (edge_radius, edge_radius)) + \
                       manhattan_distance((edge_radius, edge_radius), point)
        # Number lies on third edge (from upper-left to bottom-left corner)
        elif x == -edge_radius and y >= starting_point[1]:
            distance = manhattan_distance(starting_point, (edge_radius, edge_radius)) + \
                       manhattan_distance((edge_radius, edge_radius), (-edge_radius, edge_radius)) + \
                       manhattan_distance((-edge_radius, edge_radius), point)
        # Number lies on fourth edge (from bottom-left to bottom-right corner)
        else:
            distance = manhattan_distance(starting_point, (edge_radius, edge_radius)) + \
                       manhattan_distance((edge_radius, edge_radius), (-edge_radius, edge_radius)) + \
                       manhattan_distance((-edge_radius, edge_radius), (-edge_radius, -edge_radius)) + \
                       manhattan_distance((-edge_radius, -edge_radius), point)

        distance += (edge_length - 2) ** 2

        return distance + 1

    """Memoize function values to avoid repeated calculation of recursive elements.
    For example: In order to calculate 5th element, we need to calculate value of 1st, 2nd, 3rd and 4th.
    To calculate 4th we need to calculate 1st, 2nd and 3rd.
    In order to calculate 3rd, we need to calculate value of 1st and 2nd.
    To calculate 2nd, we need to calculate 1st. 
    In this example, value of 1st would be calculated 4 times, 2nd - 3 times, 3rd - times, 4th and 5th one time.
    By memoizing, each value is calculated only once and returned from cache for subsequent calls.
    """
    @memoize
    def get_puzzle_b_sequence_value(point):
        """Returns puzzle-B value of (x,y) member, as a sum of adjacent cells in a grid.
        :param point: (x,y) position in a grid
        :return: [int] value
        """
        total_value = 0

        # Value of first element
        if point == (0, 0):
            total_value += 1
        # Value of 2nd and further element
        else:
            # Order of current point on a spiral
            current_point_order = order_based_on_position(point)

            # Try all adjacent cells ( x-1 and x+1 )
            for x in range(point[0] - 1, point[0] + 2):
                # Try all adjacent cells ( y-1 and y+1 )
                for y in range(point[1] - 1, point[1] + 2):
                    # If the adjacent cell == current cell, don't add it to the total
                    if (x, y) == point:
                        continue
                    else:
                        # Order of adjacent cell on a spiral
                        other_point_order = order_based_on_position((x, y))

                        # Check if adjacent cell has lower order on spiral (otherwise, it cannot be added to total)
                        if other_point_order < current_point_order:
                            total_value += get_puzzle_b_sequence_value((x, y))

        return total_value

    # Solution of day_03 - puzzle A
    def solve_puzzle_a():
        # Find manhattan distance between n-th member and center (0,0) of the grid
        return manhattan_distance(nth_member_pos_on_spiral(puzzle_input, True), (0, 0))

    # Solution of day_03 - puzzle B
    def solve_puzzle_b():
        member_order = 1

        # Loop through spiral members, until value > puzzle_input is found
        while True:
            puzzle_b_value = get_puzzle_b_sequence_value(nth_member_pos_on_spiral(member_order, True))
            if puzzle_b_value > puzzle_input:
                return puzzle_b_value

            member_order += 1

    return solve_puzzle_a(), solve_puzzle_b()
