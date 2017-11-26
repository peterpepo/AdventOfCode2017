def read_puzzle_input(path, file_name):
    import os
    os.chdir(path)

    input_file = open(file_name, "r")
    input_lines = input_file.readlines()
    input_file.close()
    return input_lines