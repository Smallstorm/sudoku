import random
import numpy as np

defRow = [1,2,3,4,5,6,7,8,9]
shiftRow = list(range(0,9,3))
grid = list()

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

print('base grid:\n')
for i in range(0,9): print(grid[i])
print('\n')

######################################################################################
# function def
######################################################################################  

#shifting rows(cols) in the segment
def shiftRowsInSeg(Grid, shiftRow):
    shiftGrid = [0,1,2]
    random.shuffle(shiftGrid)
    j = 0
    while j < 3:
        i = 0
        while i < 3:                  
            buf = Grid[shiftRow[j] + shiftGrid[i]]        
            Grid[shiftRow[j] + shiftGrid[i]] = Grid[shiftRow[j] + shiftGrid[i-1]]
            Grid[shiftRow[j] + shiftGrid[i-1]] = buf
            i += 1
        j += 1
    return(Grid)

#shifting segments
def shiftSegmsInGrid(Grid,shiftRow):
    shiftGrid = [0,1,2]
    i = 0
    while i < 3:                  
        buf0 = Grid[shiftRow[i]]
        buf1 = Grid[shiftRow[i] + 1]        
        buf2 = Grid[shiftRow[i] + 2]        
        Grid[shiftRow[i] + 0] = Grid[shiftRow[i] + 0 - 3]
        Grid[shiftRow[i] + 1] = Grid[shiftRow[i] + 1 - 3]
        Grid[shiftRow[i] + 2] = Grid[shiftRow[i] + 2 - 3]
        Grid[shiftRow[i] + 0 - 3] = buf0
        Grid[shiftRow[i] + 1 - 3] = buf1
        Grid[shiftRow[i] + 2 - 3] = buf2
        i += 1
        return(Grid)

# transpose main grid         
def grid_transpose(Grid):                                       
    grid = [[Grid[j][i] for j in range(len(Grid))] for i in range(len(Grid[0]))]
    return(grid)

# sudoku mixing
def sudoku_mix(n):    
    mix_func = ['grid_transpose(grid)', 'shiftRowsInSeg(grid, shiftRow)', 'shiftSegmsInGrid(grid,shiftRow)']
    for i in range(1,n):
        id_func = random.randrange(0,len(mix_func),1)
        grid = eval(mix_func[id_func])    
    print('\n')    
    for j in range(0,9): print(grid[j])
    return

# d - sudoku difficulty - must be less then 81 
def sudoku_zero(d,adr):
    i = 0
    while(i < d):                
        grid[adr[i][0]][adr[i][1]] = 0            
        i += 1
    return


################################################################################################
# function cols
################################################################################################



sudoku_mix(200)

# adress generator
adr = list()
for i in range(9):
    for j in range(9):    
        adr.append([i,j])
random.shuffle(adr)        

sudoku_zero(80,adr)

for j in range(0,9): print(grid[j])



