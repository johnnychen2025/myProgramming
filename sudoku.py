sudoku=[[0,0,0,0,3,0,6,4,0],
        [0,3,0,7,0,5,8,0,0],
        [8,2,0,0,9,6,0,7,0],
        [0,0,0,0,7,0,2,9,6],
        [0,0,3,4,2,9,0,1,0],
        [2,9,8,5,6,1,4,0,7],
        [7,0,2,9,0,0,0,0,0],
        [0,0,0,0,0,0,0,6,4],
        [4,5,9,0,0,0,7,0,0]]
def isValid(r,c,v):
    if v > 9:
        return False
    for i in range(9):
        if v == sudoku[r][i]:
            return False
        if v == sudoku[i][c]:
            return False
        if v == sudoku[r//3*3+i//3][c//3*3+i%3]:
            return False
    return True
def Next(r,c):
    while sudoku[r][c]!=0:
        if c==8:
            if r==8:
                return 8,8
            c = 0
            r = r + 1
        else:
            c = c + 1
    return r,c

r,c=Next(0,0)
v = 1
sr=[]
sc=[]
while True:
    if r==8 and c==8 and sudoku[r][c]!=0:
        for i  in range(9):
            print(sudoku[i])
        break
    if isValid(r,c,v):
        sudoku[r][c]=v
        sr.append(r)
        sc.append(c)
        v = 1
        r,c=Next(r,c)
    else:
        if v>=9:
            sudoku[r][c]=0
            if len(sr)==0:
                print("No solution")
                break
            else:
                r=sr.pop()
                c=sc.pop()
                v=sudoku[r][c]+1
        else:
            v = v + 1