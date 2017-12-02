RESULT_PRINT_FORMAT = "Day {day_number}, part A: {solution[0]}\nDay {day_number}, part B: {solution[1]}"

# Run day_01
from day_01 import day_01
print(RESULT_PRINT_FORMAT.format(day_number = "01", solution = day_01.solve()))