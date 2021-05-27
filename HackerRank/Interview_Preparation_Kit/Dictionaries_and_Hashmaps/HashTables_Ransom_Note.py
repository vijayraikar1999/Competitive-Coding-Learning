# Problem link - https://www.hackerrank.com/challenges/ctci-ransom-note/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps

def checkMagazine(magazine, note):
    magazineIndex = {}
    noteIndex = {}
    for ele in magazine:
        magazineIndex[ele] = magazineIndex.get(ele, 0) + 1
    for ele in note:
        noteIndex[ele] = noteIndex.get(ele, 0) + 1
    for ele in noteIndex:
        if noteIndex[ele] > magazineIndex.get(ele, 0):
            print('No')
            return
        if noteIndex[ele] <= magazineIndex[ele]:
            pass
    print('Yes')    