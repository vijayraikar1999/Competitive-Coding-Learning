# Problem link - https://www.hackerrank.com/challenges/ctci-array-left-rotation/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays

def rotLeft(a, d):
    rightPart = a[0:d]
    leftPart = a[d:]
    ans = leftPart + rightPart
    return ans