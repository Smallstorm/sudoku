import random
import numpy as np
defRow = [1,2,3,4,5,6,7,8,9]
shiftRow = list(range(0,9))
grid = list()

random.shuffle(shiftRow)  
i = 0
while i < 9:                    #shifting elements in the row 
    row = defRow[-shiftRow[i]:] + defRow[:-shiftRow[i]]
    grid.append(row)    
    i += 1

print('\t shifting elements in the row \n')
for i in range(0,9): print(grid[i])
print('\n')

print(shiftRow,'\n')

i = 0
while i < 5:                    #shifting rows in the main grid
    buf = grid[shiftRow[i]]
    grid[shiftRow[i]] = grid[shiftRow[-i]]
    grid[shiftRow[-i]] = buf
    i += 1

print('\t shifting rows in the main grid \n')
for i in range(0,9): print(grid[i])
print('\n')

trGrid = np.array(grid)         # transpose main grid
trGrid = trGrid.transpose()
for i in range(0,9): print(trGrid[i])
print('\n')

i = 0
while i < 5:                    #shifting rows(cols) in the main grid
    buf = trGrid[shiftRow[i]]
    trGrid[shiftRow[i]] = trGrid[shiftRow[-i]]
    trGrid[shiftRow[-i]] = buf
    i += 1

print('\t shifting rows(cols) in the main grid \n')
for i in range(0,9): print(trGrid[i])
print('\n')