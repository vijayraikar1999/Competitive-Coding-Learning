# Problem link - https://www.hackerrank.com/challenges/repeated-string/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup

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
