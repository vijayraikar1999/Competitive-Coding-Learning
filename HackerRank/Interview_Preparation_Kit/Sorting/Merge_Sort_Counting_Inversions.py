# Problem link - https://www.hackerrank.com/challenges/ctci-merge-sort/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=sorting

def merge(li, low, mid, high):
    i = low
    j = mid + 1
    inversionCount = 0
    ansList = []

    while i <= mid and j <= high:
        if li[i] <= li[j]:
            ansList.append(li[i])
            i += 1
        else:
            ansList.append(li[j])
            j += 1
            inversionCount += mid - i + 1

    if i <= mid:
        ansList.extend(li[i:mid+1])
    if j <= high:
        ansList.extend(li[j:high+1])

    li[low:high+1] = ansList

    return inversionCount


def mergeSort(li, low, high):
    if low >= high:
        return 0
    mid = low + ((high - low) >> 1)
    inversionCount = 0

    inversionCount += mergeSort(li, low, mid)
    inversionCount += mergeSort(li, mid + 1, high)
    inversionCount += merge(li, low, mid, high)

    return inversionCount

def countInversions(arr):
    li = arr.copy()
    return mergeSort(arr, 0, len(arr)-1)