# Problem link - https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums, target):
        n = len(nums)
        indexDict = {}
        for i in range(n):
            val = nums[i]
            if val in indexDict and val*2 == target:
                return [indexDict[val], i]
            indexDict[val] = i
            
        for i in range(n):
            x = target - nums[i]
            if indexDict.get(x) and x*2 != target:
                return [indexDict[nums[i]], indexDict[x]]    