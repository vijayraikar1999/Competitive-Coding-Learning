n = int(input())

for t in range(n):
    string = input()
    ansDict = {}
    indexDict = {}
    for idx in range(len(string)):
        char = string[idx]
        ansDict[char] = ansDict.get(char, 0) + 1
        if indexDict.get(char) is None:
            charList = [idx, ]
            indexDict[char] = charList
        else:
            indexDict[char].append(idx)
    oddCount = 0
    oddChar = None
    for char, freq in ansDict.items():
        if freq % 2 != 0:
            oddCount += 1
            oddChar = char

    if oddCount == 0 or oddCount == 1:
        i, j = 0, -1
        ansList = [-1] * len(string)
        for char, value in indexDict.items():
            li = indexDict[char]
            if ansDict[char] % 2 == 0:
                for k in range(0, len(li), 2):
                    ansList[i] = li[k]
                    ansList[j] = li[k+1]
                    i += 1
                    j -= 1
        if oddCount == 1:
            li = indexDict[oddChar]
            for k in range(0, len(li)):
                if ansList[i] == -1:
                    ansList[i] = li[k]
                    i += 1

        for ele in ansList:
            print(ele+1, end=" ")
        print()
    else:
        print(-1)