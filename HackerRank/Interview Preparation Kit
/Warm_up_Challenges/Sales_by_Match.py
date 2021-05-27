# Problem link - https://www.hackerrank.com/challenges/sock-merchant/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup

def sockMerchant(n, ar):
    countDict = {}
    ans = 0
    for ele in ar:
        countDict[ele] = countDict.get(ele, 0) + 1
    for value in countDict.values():
        ans += value >> 1
    return ans    
