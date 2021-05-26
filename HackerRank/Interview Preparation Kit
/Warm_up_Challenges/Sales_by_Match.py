def sockMerchant(n, ar):
    countDict = {}
    ans = 0
    for ele in ar:
        countDict[ele] = countDict.get(ele, 0) + 1
    for value in countDict.values():
        ans += value >> 1
    return ans    
