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