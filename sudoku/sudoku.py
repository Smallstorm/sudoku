import sudoku_func
import random
import sys

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

print('sudoku mixed')
grid = sudoku_func.sudoku_mix(grid,20000)
print('\n') 
for j in range(0,9): print(grid[j])

# adress generator
adr = list()
for i in range(9):
    for j in range(9):    
        adr.append([i,j])
random.shuffle(adr)        

difficulty = 40
sudoku_func.sudoku_zero(grid,difficulty,adr)

print('\n','sudoku zeroed')
for j in range(0,9): print(grid[j])

# zero addresses
zeroes = list()
for i in range(difficulty,):
    zeroes.append(sudoku_func.next_empty(grid))

print('before\n')
for j in range(9): print(grid[j])

def solve(grid):    
    d = 0
    while(d < difficulty):
        n = 1   
        got_answer = False            
        print('\nd = ',d)
        while(not got_answer): 
            print('got answer =',got_answer)  
            while(0 < n < 10):
                print(n)
                if(sudoku_func.possible(grid,zeroes[d][0],zeroes[d][1],n)):
                    grid[zeroes[d][0]][zeroes[d][1]] = n 
                    print('possible  : ','n = ',n,'d = ',d)                     
                    got_answer = True
                    d += 1
                    skip = n
                    break  # to next d from while
                n += 1      

            else:
                grid[zeroes[d][0]][zeroes[d][1]] = -1                                                  
                print('backtrack from','d = ',d,'\nTo row = ', zeroes[d-1][0],'col = ',zeroes[d-1][1],'d = ',d-1)
                print('n from else = ',skip)
                d -= 1
            break  # previous d from while else  

solve(grid)

print('\n after\n')
for j in range(9): print(grid[j])
    