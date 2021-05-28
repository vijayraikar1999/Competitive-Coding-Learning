from bisect import bisect_left, bisect_right

n, k = map(int, input().split())
li = [int(ele) for ele in input().split()]

li.sort()
ans = 0
for i, ele in enumerate(li):
    value = ele + k
    left = bisect_left(li, value, lo=i+1)
    if left != n:
        ans += n - left
print(ans) 