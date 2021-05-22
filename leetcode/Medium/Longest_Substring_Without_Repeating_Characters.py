# Problem link - https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        indexDict = {}
        count = 0
        maxLength = 0
        currLength = 0
        p = 0
        for index, ele in enumerate(s):
            idx = indexDict.get(ele)
            if idx is None or ((idx is not None) and (idx < p)):
                indexDict[ele] = index
                currLength += 1
                if currLength > maxLength:
                    maxLength = currLength
            else:
                indexDict[ele] = index
                p = idx
                currLength = index - p
                if currLength > maxLength:
                    maxLength = currLength
                    
                    
        return maxLength