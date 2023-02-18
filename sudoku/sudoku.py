import sudoku
import random

defRow = [1,2,3,4,5,6,7,8,9]
shiftRow = list(range(0,9,3))
grid = list()

#grid init
j = 0                                           
while j < 3:    
    i = 0
    while i < 3:                   
        row = defRow[shiftRow[i] + j:] + defRow[:shiftRow[i] + j]
        grid.append(row)    
        i += 1
    j += 1

print('base grid')
for i in range(0,9): print(grid[i])
print('\n')

# sudoku mixing
def sudoku_mix(n):    
    mix_func = ['sudoku.grid_transpose(grid)', 'sudoku.shiftRowsInSeg(grid, shiftRow)', 'sudoku.shiftSegmsInGrid(grid,shiftRow)']
    for i in range(1,n):
        id_func = random.randrange(0,len(mix_func),1)
        grid = eval(mix_func[id_func])       
    for j in range(0,9): print(grid[j])
    return


print('sudoku mixed')
sudoku_mix(2000)

# adress generator
adr = list()
for i in range(9):
    for j in range(9):    
        adr.append([i,j])
random.shuffle(adr)        

sudoku.sudoku_zero(grid,50,adr)

print('\n','sudoku zeroed')
for j in range(0,9): print(grid[j])

A = sudoku.possible(grid,1,2,1)
print(A)