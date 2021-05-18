# Problem link - https://leetcode.com/problems/maximum-product-subarray/


class Solution:
    def maxProduct(self, nums):
        maxP = float('-inf')
        currPP = None
        currNP = None
        flag = 0

        for ele in nums:
            newNP = None
            newPP = None
            if ele > 0:
                if currPP is None:
                    newPP = ele
                else:
                    newPP = currPP * ele

                if currNP is None:
                    newNP = None
                else:
                    newNP = currNP * ele

            elif ele < 0:
                if currPP is None:
                    newNP = ele
                else:
                    newNP = currPP * ele

                if currNP is None:
                    newPP = None
                else:
                    newPP = currNP * ele

            else:
                flag = 1
                newPP = None
                newNP = None

            currPP = newPP
            currNP = newNP

            if currPP is None and (currNP is not None) and currNP > maxP:
                maxP = currNP
            if currPP is not None and currPP > maxP:
                maxP = currPP

        if flag == 1 and maxP < 0:
            maxP = 0

        return maxP
