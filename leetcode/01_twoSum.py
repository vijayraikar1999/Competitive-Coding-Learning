class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexDict = {}
        for index, num in enumerate(nums):
            if (target - num) in indexDict:
                return [indexDict[target - num], index]
            else:
                indexDict[num] = index
    
