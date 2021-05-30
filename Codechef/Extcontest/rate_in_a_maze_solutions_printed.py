maze = [
    [1,1,0],
    [1,1,1],
    [1,1,1]
]

n = len(maze)
count = 0

visited = [[[False, ' '] for j in range(n)] for i in range(n)]
def printSolution():
    for i in range(n):
        for j in range(n):
            print('(' + str(int(visited[i][j][0])) + ',' + visited[i][j][1] + ')', end='  ')
        print()
    print()        

def solveMaze(i, j):
    if maze[i][j] == 0:
        return
    if (i == n-1 and j == n-1):
        global count
        count += 1
        visited[i][j][0] = True
        print('Solution: ', count)
        printSolution()
        visited[i][j][0] = False
        return
    visited[i][j] = [True, ' ']
    if i < n and j < n and i >= 0 and j >= 0:

        if j+1 < n and visited[i][j+1][0] == False:
            visited[i][j][1] = 'r'
            solveMaze(i, j+1)

        if i+1 < n and visited[i+1][j][0] == False:
            visited[i][j][1] = 'd'
            solveMaze(i+1, j, )

        if j-1 > 0 and visited[i][j-1][0] == False:
            visited[i][j][1] = 'l'
            solveMaze(i, j-1)

        if i-1 > 0 and visited[i-1][j][0] == False:
            visited[i][j][1] = 'u'
            solveMaze(i-1, j)

        visited[i][j] = [False, ' ']             

solveMaze(0, 0)