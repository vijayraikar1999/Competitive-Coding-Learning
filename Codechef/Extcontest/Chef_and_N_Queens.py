n = int(input())
count = 0
dLeft = [True]*(2*n)
dRight = [True]*(2*n)
column = [True] * n

def nQueen(i):
    if i == n:
        global count
        count += 1
        return
    for j in range(n):
        if column[j] == True and dLeft[i+j] == True and dRight[n-j+i] == True:
            column[j] = False
            dLeft[i+j] = False
            dRight[n-j+i] = False
            nQueen(i+1)
            column[j] = True
            dLeft[i+j] = True
            dRight[n-j+i] = True

nQueen(0)
print(count)