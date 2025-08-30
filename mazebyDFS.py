maze = [[1,1,1,1,1,1,1],
        [1,0,0,0,0,0,1],
        [1,0,0,1,1,0,1],
        [1,0,1,0,0,0,1],
        [1,0,1,1,1,1,1],
        [1,0,0,0,0,0,1],
        [1,1,1,1,1,1,1]
        ]
sr=[0]
sc=[0]
r=1
c=1
while (r!=5 or c!=5) and (len(sr)!=0):
    maze[r][c]=1
    if maze[r][c+1]==0:
        sr.append(r)
        sc.append(c)
        c=c+1
    elif maze[r+1][c]==0:
        sr.append(r)
        sc.append(c)
        r=r+1
    elif maze[r][c-1]==0:
        sr.append(r)
        sc.append(c)
        c=c-1
    elif maze[r-1][c]==0:
        sr.append(r) # push
        sc.append(c)
        r=r-1
    else:
        r = sr.pop()
        c = sc.pop()
    # print(r,c)
    # print(sr)
    # print(sc)
    # for i in range(7):
    #     print(maze[i])
    # s = input()
if len(sr)==0:
    print("No Path")
else:
    print(sr)
    print(sc)