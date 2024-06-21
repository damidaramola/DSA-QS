class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:

        # 1. component parts - multiplying nums except interable
        # 2. appending the products to empty array ,returning ans

        #psuedo code
        # for loop, product = 1 , we increment j += 1 
        # as we increment j we multiply it by the next number except nums[i] j!=nums[i]
        #we have to keeop track of the product - prdct= 1
        # at the end of the loop we append it to an empty array then start over again with j = 0
        
        n = len(nums)
        ans = [1] * n

        # Calculate left products
        left_product = 1
        for i in range(n):
            ans[i] = left_product
            left_product *= nums[i]

        # Calculate right products and multiply with left products
        right_product = 1
        for i in range(n-1, -1, -1):
            ans[i] *= right_product
            right_product *= nums[i]

        return ans
    
    # Time and space complexity - 0(n)
#nums = [9,0,4,12]
nums = [3,4,6,8]
test = Solution()
run = test.productExceptSelf(nums)
print(run)


"""      
brute force algorithm 


length = len(nums)
ans = []

# First pass: calculate the total product of all elements
total_product = 1
for num in nums:
    total_product *= num

# Second pass: calculate the result for each index
for i in range(length):
    if nums[i] != 0:
        ans.append(total_product // nums[i])
    else:
        # If the current element is zero, we need a separate handling
        # We can't simply divide by zero, so we calculate the product of the rest of the array
        product = 1
        for j in range(length):
            if i != j:
                product *= nums[j]
        ans.append(product)

return ans   
"""
