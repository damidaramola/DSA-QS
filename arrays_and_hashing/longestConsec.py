class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        # input = list , output len of final output
        #brute force would be to sort it and count nums that have a diff of 1
        # no repreating chars
        #use a set to get rid of duplicates, check that
        # create a counter to increment every time you meet a

        charSet = set(nums)
        longest = 0 

        for num in nums:
            if (num-1) not in charSet:
                len = 0 
                while (num +len) in charSet:
                    len +=1
                longest = max(len,longest)
        return longest

nums = [100,5,700,3,2,4]
nums = [100,6,70,5,2,4]
test = Solution()
call = test.longestConsecutive(nums)
print(call)