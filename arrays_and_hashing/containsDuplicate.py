# Contains Duplicate


class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        # create set to store the values in a loop
        # for each loop check if num is already in the set 
        # if yes return true else false and append that num to the set 
        
        store = set()

        for num in nums:
            if num in store:
                return True 
            store.add(num)
        return False
    
    
#nums = [1,2,2,5]
nums =[1,2,3,4,6] 
test = Solution()
ans = test.containsDuplicate(nums)
print(ans)

#Time complexity

#It is O(n) because we are looping through the array where n is number if elements in array
# A set takes up  O(n) space
# optimal solution 
# I think this is the optimal solution

#least efficient O(n^2) using nested loops, O(1) space complexity, no extra space/data structures needed

# class Solution:
#     def containsDuplicate(self, nums: list[int]) -> bool:
#         for i in range(len(nums)):
#             for j in range(i + 1, len(nums)):
#                 if nums[i] == nums[j]:
#                     return True
#         return False
#

# Not optimal solution - sorting 

# class Solution:
#     def containsDuplicate(self, nums: list[int]) -> bool:
#         nums.sort()  # Sort the list, O(n log n) time complexity
#         for i in range(1, len(nums)):  # Iterate through the list starting from the second element
#             if nums[i] == nums[i - 1]:  # Compare current element with the previous one
#                 return True
#         return False

# TC = O(n log n)
#SC = O(1) - sort operation is performed in place, and no additional data structures are used.