class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        # always have the first number as the first minimum no matter how big/small
        # get the 2nd and 3rd minimum
        # add them together 

        s = nums[0]
        nums[1:len(nums)] = sorted(nums[1:len(nums)])

        s = s + nums[1] + nums[2]
        return s

#Time comlexity - Olog n
#Space O(1)