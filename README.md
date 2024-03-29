# **sudoku**
> головоломка с числами

##### Целью разработки данной программы было разобраться, что такеое Backtracking-алгоритм и как его можно применять

Работу backtracking-алгоритма можно рассмотреть на примере простой задачки.

Допустим, мы хотим подобрать три числа A, B и C так, чтобы выполнялись следующие условия:


###### условие 1:  A > B

###### условие 2:  B != C

###### условие 3:  A != C


В первую очередь мы должны проверить условие 1, найти числа A и B, удовлетворяющие этому условию. Для этого мы фиксируем некоторое значение числа A и проверяем все возможные значения числа B. Если ни одно из значений числа B не удовлетворяет условию 1, то мы откатываемся назад и меняем значение числа A на некоторое следующее значение из возможных. И вновь проверяем все значения B.  

Затем мы подбираем число C таким образом, чтобы выполнялось условие 2. Вновь мы фиксируем найденные на предидущем шаге значения чисел A и B и проверяем все возможные значения числа C. Если ни одно из значений числа C не удовлетворяет условию 2, то мы откатываемся назад и меняем значение числа B на то, которое может удовлетворять условию 1 и вновь проверяем все значения числа C    

Код:

```
exitFlag = False
    i = 0
    j = 0
    k = 0    
    while (i < len(A) and not exitFlag):        
        S[0] = A[i]      
        j = 0          
        while (j < len(B) and (not exitFlag)):
            S[1] = B[j]                     
            if (S[0] > S[1]):                            
                k = 0
                while (k < len(C) and (not exitFlag)):
                    S[2] = C[k]                    
                    if((S[1] != S[2]) and (S[0] != S[2])):                                        
                        exitFlag = True
                        break
                    k += 1
            j += 1                                        
        i += 1

```
