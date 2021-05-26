# Problem link - https://www.hackerrank.com/challenges/counting-valleys/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup

def countingValleys(steps, path):
    level = 0
    valleyCount = 0

    for step in path:
        if step == 'U':
            level += 1
        else:
            level -= 1

        if level == 0 and step == 'U':
            valleyCount += 1

    return valleyCount        
        