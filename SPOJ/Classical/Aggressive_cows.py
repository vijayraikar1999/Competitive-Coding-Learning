# Problem link - https://www.spoj.com/problems/AGGRCOW/

t = int(input())
 
for i in range(t):
    n, c = map(int, input().split())
    li = []
    for j in range(n):
        li.append(int(input()))
 
    li.sort()
    start = 1
    end = li[-1]
    ans = 1
    while start <= end:
        mid = start + (end - start) // 2
        prev_stall = li[0]
        count = 1
        for k in li[1:]:
            if k - prev_stall >= mid:
                count += 1
                prev_stall = k
                if count == c:
                    break
        if count == c:
            ans = mid
            start = mid + 1
        else:
            end = mid - 1
 
    print(ans)