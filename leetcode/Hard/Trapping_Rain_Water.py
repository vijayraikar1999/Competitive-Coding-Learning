# Problem link - https://leetcode.com/problems/trapping-rain-water/


# Code in the comment section is O(n2) algorithm for the problem

# class Solution:
#     def trap(self, height: List[int]) -> int:
        
#         ansSum = 0
#         n = len(height)
#         for i in range(n-2):
#             x = height[i]
#             maxValue = 0
#             for j in range(i+2,n):
#                 diff = j - i - 1
#                 minValue = min(x, height[j])
#                 maxValue = max(maxValue,height[j-1])
#                 factor = minValue - maxValue
#                 if factor < 0:
#                     factor = 0
#                 ansSum += factor * diff    
                
#         return ansSum   


class Solution:
    def trap(self, height):
        
        ansSum = 0
        n = len(height)
        if n == 1 or n == 2:
            return 0
        
        leftMax = [0] * n
        rightMax = [0] * n
        maxValue = 0
        for i in range(1,n-1):
            maxValue = max(maxValue, height[i-1])
            leftMax[i] = maxValue
            
        maxValue = 0
        for i in range(n-2, 0, -1):
            maxValue = max(maxValue, height[i+1])
            rightMax[i] = maxValue
            
            
        for i in range(1,n-1):
            factor = min(leftMax[i], rightMax[i])
            if factor > height[i]:
                ansSum += factor - height[i] 
            
            
        return ansSum   