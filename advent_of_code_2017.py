RESULT_PRINT_FORMAT = "Day {day_number}, part A: {solution[0]}\nDay {day_number}, part B: {solution[1]}"

# Run day_01
from day_01 import day_01
print(RESULT_PRINT_FORMAT.format(day_number = "01", solution = day_01.solve()))

# Run day_02
from day_02 import day_02
print(RESULT_PRINT_FORMAT.format(day_number = "02", solution = day_02.solve()))

# Run day_03
from day_03 import day_03
print(RESULT_PRINT_FORMAT.format(day_number = "03", solution = day_03.solve()))

# Run day_04
from day_04 import day_04
print(RESULT_PRINT_FORMAT.format(day_number = "04", solution = day_04.solve()))