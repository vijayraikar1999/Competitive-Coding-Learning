from bisect import bisect_right

t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    li_left = []
    li_right = []
    for j in range(n):
        l, r = map(int, input().split())
        li_left.append(l)
        li_right.append(r)

    li_left.sort()
    li_right.sort()       
    for j in range(m):
        pi = int(input())
        ans = -1
        index = bisect_right(li_right, pi)
        if index != n:
            if li_left[index] <= pi:
                ans = 0
            elif li_left[index] > pi:
                ans = li_left[index] - pi
        else:
            ans = -1
        print(ans)            






