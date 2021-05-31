# cook your dish here

n = int(input())
maze = [ [int(ele) for ele in input().split()] for i in range(n)]
count = 0

visited = [[False for j in range(n)] for i in range(n)]

def solveMaze(i, j):
    if maze[i][j] == 1:
        return
    if (i == n-1 and j == n-1):
        global count
        count += 1
        return
    visited[i][j] = True
    if i < n and j < n and i >= 0 and j >= 0:

        if j+1 < n and visited[i][j+1] == False:
            solveMaze(i, j+1)

        if i+1 < n and visited[i+1][j] == False:
            solveMaze(i+1, j, )

        if j-1 > 0 and visited[i][j-1] == False:
            solveMaze(i, j-1)

        if i-1 > 0 and visited[i-1][j] == False:
            solveMaze(i-1, j)

        visited[i][j] = False         

solveMaze(0, 0)
print(count)
