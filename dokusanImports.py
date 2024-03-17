from io import StringIO
import sys
import numpy as np
from dokusan import generators

output = StringIO()
sys.stdout = output

sudoku_str = str(generators.random_sudoku(avg_rank=55))

sudoku_numbers = [int(char) for char in sudoku_str if char.isdigit()]

sudoku = np.array(sudoku_numbers).reshape(9, 9)

def format_row(row):
    formatted_row = ', '.join(map(str, row))
    return f"[{formatted_row}],"

formatted_sudoku = ''
for i, row in enumerate(sudoku):
    if i < len(sudoku) - 1:
        formatted_sudoku += format_row(row)
    else:
        formatted_sudoku += f"[{', '.join(map(str, row))}],"


sys.stdout = sys.__stdout__


captured_output = output.getvalue()
print(formatted_sudoku)