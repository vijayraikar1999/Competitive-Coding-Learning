n = int(input())

li = []

for i in range(n):
    li.append(int(input()))

li.sort()

maxValue = 0
for i in range(n):
    currValue = li[i] * (n-i)
    if currValue > maxValue:
        maxValue = currValue
        
print(maxValue)       
