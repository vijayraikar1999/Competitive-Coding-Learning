# Problem link - https://leetcode.com/problems/counting-bits/

class Solution:
    def countBits(self, n: int):
        nearest = 0
        ansList = [-1]*(n+1)
        for i in range(n+1):
            if i == 0 or i == 1:
                ansList[i] = i
            elif i & (i-1) == 0:
                ansList[i] = 1
                nearest = i
            elif i & 1 != 0:
                ansList[i] = ansList[i-1] + 1
            else:
                ansList[i] = ansList[nearest] + ansList[i-nearest]
        
        return ansList