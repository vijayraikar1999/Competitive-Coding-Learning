# Problem link - https://leetcode.com/problems/maximum-subarray/

class Solution:
    def maxSubArray(self, nums):
        
        currSum  = 0
        maxSum = float('-inf')
        
        for ele in nums:
            currSum += ele
            if currSum > maxSum:
                maxSum = currSum
                
            if currSum < 0:
                currSum = 0
                
        return maxSum