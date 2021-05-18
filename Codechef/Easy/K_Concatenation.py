def kadne_sum(arr, n ):
    currSum = 0
    maxSum = float('-inf')
    for i in range(n):
        currSum += arr[i]
        if maxSum < currSum:
            maxSum = currSum

        if currSum < 0:
            currSum = 0

    return maxSum


def max_subarray_sum(arr, n, k):
    kadne_sum_value = kadne_sum(arr, n)
    if k == 1:
        return kadne_sum_value

    curr_prefix_sum = 0
    curr_suffix_sum = 0
    prefix_sum = float('-inf')
    suffix_sum = float('-inf')

    for i in range(n):
        curr_prefix_sum += arr[i]
        prefix_sum = max(curr_prefix_sum, prefix_sum)
        
    li_sum = curr_prefix_sum    

    for i in range(n-1, -1, -1):
        curr_suffix_sum += arr[i]
        suffix_sum = max(suffix_sum, curr_suffix_sum)

    

    ans = 0
    if li_sum < 0:
        ans = max((suffix_sum + prefix_sum), kadne_sum_value)
    else:
        ans = max((suffix_sum + prefix_sum + ((k - 2) * li_sum)), kadne_sum_value)

    return ans


t = int(input())

for i in range(t):
    n, k = map(int, input().split())
    li = list(map(int, input().split()))
    
    print(max_subarray_sum(li, n, k))