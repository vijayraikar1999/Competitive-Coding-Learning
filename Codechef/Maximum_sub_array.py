# cook your dish here

t = int(input())

for i in range(t):
    n = int(input()) + 1
    li = list(map(int, input().split()))
    li.append(-1)
    
    ansList = []
    currSum = 0
    currStart = -1
    flag = 0
    for j in range(n):
        if li[j] >= 0:
            if flag == 0:
                currStart = j
                currSum = li[j]
                flag = 1
            else:
                currSum += li[j]
        else:
            if flag == 0:
                continue
            else:
                length = j - currStart
                ansList.append((currSum, length, n-currStart, j-1))
                flag = 0
                currSum = 0

    ansList.sort()

    start = n - ansList[-1][2]
    end = ansList[-1][3]

    for j in range(start, end + 1):
        print(li[j], end = " ")
                
            
        
        
            
