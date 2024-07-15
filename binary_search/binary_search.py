class Solution:
    def search(self, nums: list[int], target: int) -> int:
      left = 0 
      right = len(nums) -1 

      while left <= right:
        midpoint = (left + right) //2
        if target < nums[midpoint]:
            right  = midpoint -1
        elif target > nums[midpoint]:
            left = midpoint + 1
        else:
            return midpoint
      return -1


        #[-1,0,3,9,12]
      # left  = 0 
      # right = len(nums) -1
      # while left < = right
      # midpoint = (left + right) //2 
      # if nums[midpoint] == target:
      # return midpoint 
      # elif target < nums[midpoint]:
      # right  = midpoint -1 
      # elif target > nums[midpoint]:
      # left = midpoint + 1 
      # else:
      # return -1 
# Time complexity , O(logn)
# space complexity O(1)


#nums = [[1, 3, 5, 7, 9, 11, 13, 15, 17, 19]]
#target = 7

nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
target = 5
test = Solution()     
run = test.search(nums,target)
print(run)