import sudoku_func
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


print('sudoku mixed')
sudoku_func.sudoku_mix(grid,2000)

# adress generator
adr = list()
for i in range(9):
    for j in range(9):    
        adr.append([i,j])
random.shuffle(adr)        

difficulty = 50
sudoku_func.sudoku_zero(grid,difficulty,adr)

print('\n','sudoku zeroed')
for j in range(0,9): print(grid[j])


# zero addresses
zeroes = list()
for i in range(difficulty,):
    zeroes.append(sudoku_func.next_empty(grid))


def solve(grid):
    for d in range(difficulty):
        n = 1   
        got_answer = False    
        while(not got_answer): 
            print('got answer =',got_answer)  
            while(0 < n < 10):
                print(n)
                if(sudoku_func.possible(grid,zeroes[d][0],zeroes[d][1],n)):
                    grid[zeroes[d][0]][zeroes[d][1]] = n 
                    print('possible  : row = ',zeroes[d][0],'col = ',zeroes[d][1],'n = ',n,'d = ',d)                     
                    got_answer = True
                    break  
                n += 1
            if(got_answer):
                print('got answer',got_answer, 'for','row = ', zeroes[d][0],'col = ',zeroes[d][1],'d = ',d)
                break
            else:
                grid[zeroes[d][0]][zeroes[d][1]] = -1                  
                d -= 1
                print('backtrack for','row = ', zeroes[d][0],'col = ',zeroes[d][1],'d = ',d)
            break    

solve(grid)


for j in range(9): print(grid[j])
    