def read_puzzle_input(path, file_name):
    import os
    os.chdir(path)

    input_file = open(file_name, "r")
    input_lines = input_file.readlines()
    input_file.close()
    return input_lines


def memoize(f):
    """Memoize function results.
    Memoization - https://en.wikipedia.org/wiki/Memoization

    :param f:
    :return:
    """
    cache = {}

    def decorated_function(*args):
        if args in cache:
            return cache[args]
        else:
            cache[args] = f(*args)
            return cache[args]

    return decorated_function