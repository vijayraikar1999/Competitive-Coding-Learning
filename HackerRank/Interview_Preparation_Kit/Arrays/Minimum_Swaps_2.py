#Problem link - https://www.hackerrank.com/challenges/minimum-swaps-2/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays

arr = [4, 3, 1, 2]
indexDict = {}
n = len(arr)
count = 0
for index, value in enumerate(arr):
    indexDict[value] = index
for i in range(n): 
    if arr[i] != i+1:
        print(i+1, arr[i],'are swapped')
        idx = indexDict[i+1]
        indexDict[arr[i]] = indexDict[i+1]
        arr[idx] = arr[i]
        arr[i] = i+1
        count += 1
        print(arr)

print(count)        