# Problem link - https://www.hackerrank.com/challenges/new-year-chaos/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays

def minimumBribes(q):
    indexDict = {}
    n = len(q)
    bribeCount = 0
    for i in range(n):
        indexDict[i+1] = i
    for i in range(n):
        if indexDict[q[i]] - i > 2:
                print('Too chaotic')
                return
        elif indexDict[[i]] - i <= 0:
            pass
        else:
            bribeCount += indexDict[q[i]] - i
    print(bribeCount)        
