
def repeatedString(s, n):
    count = 0
    length = len(s)
    factor = n // length
    rememder = n % length
    i = 0
    leftCount = 0
    for ele in s:
        if ele == 'a':
            count += 1
        i += 1
        if i == rememder:
            leftCount = count
    ans = factor * count + leftCount
    return ans