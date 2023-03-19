import random
import numpy as np

defRow = [1,2,3,4,5,6,7,8,9]
shiftRow = list(range(0,9,3))
global grid
grid = list()

######################################################################################
# function def
######################################################################################  


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

#shifting segments
def shiftSegmsInGrid(grid,shiftRow):
    shiftGrid = [0,1,2]
    random.shuffle(shiftGrid)
    i = 0
    while i < 3:                  
        buf0 = grid[shiftRow[i]]
        buf1 = grid[shiftRow[i] + 1]        
        buf2 = grid[shiftRow[i] + 2]        
        grid[shiftRow[i] + 0] = grid[shiftRow[i] + 0 - 3]
        grid[shiftRow[i] + 1] = grid[shiftRow[i] + 1 - 3]
        grid[shiftRow[i] + 2] = grid[shiftRow[i] + 2 - 3]
        grid[shiftRow[i] + 0 - 3] = buf0
        grid[shiftRow[i] + 1 - 3] = buf1
        grid[shiftRow[i] + 2 - 3] = buf2
        i += 1
        return(grid)

# transpose main grid         
def grid_transpose(grid):
    grid = [[grid[j][i] for j in range(len(grid))] for i in range(len(grid[0]))]
    return(grid)

# sudoku mixing
def sudoku_mix(grid,n):    
    
    # for i in range(n):
        # grid = shiftRowsInSeg(grid, shiftRow)
        # grid = grid_transpose(grid)    
        # grid = shiftRowsInSeg(grid, shiftRow)         
    
    
    # shiftRowsInSeg(grid, shiftRow)
    # shiftSegmsInGrid(grid,shiftRow)
    
    mix_func = ['shiftRowsInSeg(grid, shiftRow)', 'shiftSegmsInGrid(grid,shiftRow)']
    for i in range(1,n):
        id_func = random.randrange(0,len(mix_func),1)
        grid = eval(mix_func[id_func])       
        grid = grid_transpose(grid)    
    return(grid)

# adress generator
# adr = list()
# for i in range(9):
#     for j in range(9):    
#         adr.append([i,j])
# random.shuffle(adr)    

# d - sudoku difficulty - must be less then 81 
def sudoku_zero(grid,d,adr):
    i = 0
    while(i < d):                
        grid[adr[i][0]][adr[i][1]] = 0            
        i += 1
    return

# Check if Number n can be in row i column j
# x - row, y - column, n - supposed number
def possible(grid,x,y,n):
    for i in range(9):
        if (grid[x][i] == n or grid[i][y] == n):
            return False
    x0 = (x//3)*3                    
    y0 = (y//3)*3                            
    for i in range(3):
        for j in range(3):
            if(grid[x0 + i][y0 + j] == n):
                return False
    return True                


def next_empty(grid):
    for i in range(9):
        for j in range(9):
            if (grid[i][j] == 0):
                grid[i][j] = -1
                return(i,j)                     


