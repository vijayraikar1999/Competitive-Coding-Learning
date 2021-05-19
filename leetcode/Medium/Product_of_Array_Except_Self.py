# Problem link - https://leetcode.com/problems/product-of-array-except-self/

nums = [1, 2, 3, 4]
productArray = []
n = len(nums)
prevProduct = 1
for i in range(n):
    productArray.append(prevProduct)
    prevProduct *= nums[i]

prevProduct = 1
for i in range(n - 1, -1, -1):
    productArray[i] = productArray[i] * prevProduct
    prevProduct *= nums[i]

print(productArray)
