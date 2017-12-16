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

def char_range(start_character, end_character):
    """
    Generates a sequence of ascii characters, starting with [start_character] , ending with [end character].
    Based on ascii code of the character.
    """
    for i in range(ord(start_character), ord(end_character)+1):
        yield chr(i)