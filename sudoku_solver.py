#!/usr/bin/python3


def sudoku(M, i=0, j=0):
    if solvable(M):
        return solve_grid(M)
    else:
        return False
    
def solvable(M):
    for i in range(9):
        nums = [False for _ in range(9)]
        for j in range(9):
            if M[i][j] != None:
                if nums[M[i][j]-1] == True:
                    return False
                else:
                    nums[M[i][j]-1] = True
    for i in range(9):
        nums = [False for _ in range(9)]
        for j in range(9):
            if M[j][i] != None:
                if nums[M[j][i]-1] == True:
                    return False
                else:
                    nums[M[j][i]-1] = True
    return True

def solve_grid(M,i=0,j=0):
    S=None
    if i==j==9:
        if check_result(M)==True:
            S = M.copy()
            #for ind in range(9):
                #print(M[ind])
        return S
    i_next,j_next=next_index(i,j)
    if M[i][j]!=None:
        S=solve_grid(M,i_next,j_next)
    else:
        valori = allowed_values(M,i,j,i//3,j//3)
        if len(valori)==0: 
            return
        for elemento in valori:
            M_copy = [row[:] for row in M]
            M_copy[i][j]=elemento
            S=solve_grid(M_copy,i_next,j_next)
            if S != None:
                break
    return S
        
def next_index(i,j):
    if i<8:
        if j<8:
            return i,j+1
        else:
            return i+1,0
    elif j<8:
        return i,j+1
    else: return 9,9
            
def allowed_values(M,i,j,x,y):
    v = set()
    for index in range(0,9):
        if M[i][index]!=None:
            v.add(M[i][index])
        if M[index][j]!=None:
            v.add(M[index][j])

    for a in range(x*3,x*3+3):
        for b in range(y*3,y*3+3):
            if M[a][b]!=None:
                v.add(M[a][b])

    return list({1,2,3,4,5,6,7,8,9}.difference(v))

def check_result(M):
    for i in range(9):
        valori = [ False for _ in range(9) ]
        for j in range(9):
            if valori[M[i][j]-1]==True:
                return False
            else:
                valori[M[i][j]-1]=True
    return True

if __name__=="__main__":
    #M=[[None,None,2,None,None,5,None,None,None],
    #   [7,None,3,None,None,None,9,8,5],
    #   [8,None,None,None,None,None,1,None,6],
    #   [None,None,7,None,None,None,None,None,None],
    #   [None,None,None,3,None,8,None,None,None],
    #   [3,1,6,None,4,None,None,None,None],
    #   [None,3,None,8,1,None,7,9,2],
    #   [None,7,8,None,None,2,6,None,None],
    #   [2,None,None,None,None,None,None,None,3]]

    M=[[None,3,None,None,5,8,None,None,None],
    [None,9,None,7,4,3,None,1,None],
    [5,7,2,None,None,None,None,4,None],
    [None,None,None,None,9,None,None,None,5],
    [3,None,None,5,None,1,None,2,None],
    [None,5,7,None,None,None,8,9,None],
    [None,None,5,None,None,None,None,None,9],
    [None,None,6,None,None,5,2,None,None],
    [7,None,None,8,None,None,1,None,None]]

    print(sudoku(M))