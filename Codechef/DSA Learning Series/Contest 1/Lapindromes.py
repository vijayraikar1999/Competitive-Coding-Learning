t = int(input())

for i in range(t):
    s = input()
    n = len(s)
    s1map = {}
    s2map = {}

    if n % 2 == 0:
        s1 = s[0:n // 2]
        s2 = s[n // 2:]
    else:
        s1 = s[0:n // 2]
        s2 = s[n // 2 + 1:]

    for char in s1:
        s1map[char] = s1map.get(char, 0) + 1
    for char in s2:
        s2map[char] = s2map.get(char, 0) + 1

    if s1map == s2map:
        print('YES')
    else:
        print('NO')
