import random
import sudoku_func

# constrains: unique number in sq, line and col
sudoku_func.sudoku_zero(grid,50,adr)

print('\n','sudoku zeroed')
for j in range(0,9): print(grid[j])

A = sudoku_func.possible(grid,1,2,1)
print(A)
