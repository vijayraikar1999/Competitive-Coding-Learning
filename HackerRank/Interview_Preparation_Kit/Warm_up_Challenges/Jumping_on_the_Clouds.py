# Problem link - https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup

def jumpingOnClouds(c):
    jumps = 0
    i = 0
    n = len(c)
    while i < n-1:
        if c[i+2] == 0 and i+2 <= n-1:
            jumps += 1
            i += 2
        elif c[i+1] == 0:
            jumps += 1
            i += 1
    return jumps                    
        