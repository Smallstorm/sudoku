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

                                        
#shiftGrid = [0,1,2]
#random.shuffle(shiftGrid)

def shift_rows(grid, shiftRow):                     #shifting rows(cols) in the segment
    shiftGrid = [0,1,2]
    random.shuffle(shiftGrid)
    j = 0                                           
    while j < 3:    
        i = 0
        #print('shiftGrid = ',shiftGrid,'\n', 'shiftRow = ',shiftRow,'\n')
        while i < 3:                  
            buf = grid[shiftRow[j] + shiftGrid[i]]
            grid[shiftRow[j] + shiftGrid[i]] = grid[shiftRow[j] + shiftGrid[i-1]]
            grid[shiftRow[j] + shiftGrid[i-1]] = buf
            i += 1                
        j += 1
    return(grid)

def grid_transpose(grid):                                       # transpose main grid
    grid = np.array(grid)         
    grid = grid.transpose()
    return(grid)

print('shifting rows in the segment \n')
shift_rows(grid, shiftRow)
for i in range(0,9): print(grid[i])
print('\n')

print('transpose main grid \n')
grid_transpose(grid)
for i in range(0,9): print(grid[i])

print('shifting rows in the segment \n')
shift_rows(grid, shiftRow)
for i in range(0,9): print(grid[i])
print('\n')

#i = 0                                                           #shifting rows(cols) in the grid 
#while i < 5:                  
#    buf = trGrid[shiftRow[i]]
#    trGrid[shiftRow[i]] = trGrid[shiftRow[-i]]
#    trGrid[shiftRow[-i]] = buf
#    i += 1

#print('\t shifting rows(cols) in the main grid \n')
#for i in range(0,9): print(trGrid[i])
#print('\n')