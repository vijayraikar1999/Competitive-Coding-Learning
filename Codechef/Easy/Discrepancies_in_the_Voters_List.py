# cook your dish here
n1, n2, n3 = [int(ele) for ele in input().split()]
ansDict = {}

for i in range(n1):
    ele = int(input())
    ansDict[ele] = ansDict.get(ele, 0) + 1

for i in range(n2):
    ele = int(input())
    ansDict[ele] = ansDict.get(ele, 0) + 1

for i in range(n3):
    ele = int(input())
    ansDict[ele] = ansDict.get(ele, 0) + 1

cnt = 0
ansList = []
for key, items in ansDict.items():
    if items >= 2:
        cnt += 1
        ansList.append(key)

ansList.sort()
print(cnt)
for ele in ansList:
    print(ele)