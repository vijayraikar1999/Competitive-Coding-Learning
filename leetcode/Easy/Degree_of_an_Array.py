class Solution:
    def findShortestSubArray(self, nums) -> int:
        degree = 1
        ansDict = {}
        indexDict = {}
        for i in range(len(nums)):
            ele = nums[i]
            if ele in ansDict:
                ansDict[ele] += 1
                indexDict[ele][1] = i
            else:
                ansDict[ele] = 1
                indexDict[ele] = [i,i]
                
        for ele in ansDict.values():
            if ele > degree:
                degree = ele
                
        minLength = float('inf')      
        for ele in ansDict:
            if ansDict[ele] == degree:
                length = indexDict[ele][1] - indexDict[ele][0] + 1
                if length < minLength:
                    minLength = length
                
                
                
        return minLength