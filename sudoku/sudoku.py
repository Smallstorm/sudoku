import random
import numpy as np

defRow = [1,2,3,4,5,6,7,8,9]
shiftRow = list(range(0,9,3))
grid = list()

#random.shuffle(shiftRow)                   # + random (optional)

                                            # shifting elements in the row -->3<--
print('\t shifting elements in the row --> forming base grid\n')

j = 0                                           
while j < 3:    
    i = 0
    while i < 3:                   
        row = defRow[shiftRow[i] + j:] + defRow[:shiftRow[i] + j]
        grid.append(row)    
        i += 1
    j += 1


for i in range(0,9): print(grid[i])
print('\n')

                                                        #shifting rows(cols) in the segment

def shiftRowsInSeg(grid, shiftRow):
    shiftGrid = [0,1,2]
    random.shuffle(shiftGrid)
    j = 0
    while j < 3:
        i = 0
        while i < 3:                  
            buf = grid[shiftRow[j] + shiftGrid[i]]        
            grid[shiftRow[j] + shiftGrid[i]] = grid[shiftRow[j] + shiftGrid[i-1]]
            grid[shiftRow[j] + shiftGrid[i-1]] = buf
            i += 1
        j += 1
    return(grid)

         
def grid_transpose(TrGrid):                                       # transpose main grid
    grid = [[TrGrid[j][i] for j in range(len(TrGrid))] for i in range(len(TrGrid[0]))]
    return(grid)



grid = grid_transpose(grid)
for i in range(0,9): print(grid[i])
print('\n')


j = 0
while j < 3:
    shiftRowsInSeg(grid, shiftRow)   
    for i in range(0,9): print(grid[i])
    print('\n')
    j += 1

grid = grid_transpose(grid)
for i in range(0,9): print(grid[i])
print('\n')


