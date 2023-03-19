#backtracking algorithm

import time 

# constrains: A > B, B != C, A != C

def backTrack(A, B, C):
    exitFlag = False
    i = 0
    j = 0
    k = 0    
    while (i < len(A) and not exitFlag):        
        S[0] = A[i]
        print('for1:\tA', S[0],'\tB', S[1],'\tC',S[2])
        j = 0          
        while (j < len(B) and (not exitFlag)):
            S[1] = B[j]         
            print('for2:\tA', S[0],'\tB', S[1],'\tC',S[2])        
            if (S[0] > S[1]):                            
                k = 0
                while (k < len(C) and (not exitFlag)):
                    S[2] = C[k]
                    print('for3:\tA', S[0],'\tB', S[1],'\tC',S[2])  
                    if((S[1] != S[2]) and (S[0] != S[2])):                
                        print('no backtracking here as\t A', S[0],'> B', S[1],'OK','\tC',S[2])  
                        exitFlag = True
                        break
                    k += 1
            j += 1                                        
        i += 1


A = [3,4,5,6,7,8]
B = [8,7,6,5,4,3]
C = [3,4,5,6,7,8]

S = [0,0,0]
        
start = time.time() ## точка отсчета времени   

S = backTrack(A,B,C)
print(S)

end = time.time() - start ## собственно время работы программы
print(end) ## вывод времени



