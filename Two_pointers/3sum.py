class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        #input = array
        # output = 1 or multiple arrays
        #brute force
        # loop 3 times?
        # if nums[i] + nums[j] + nums[k] = 0
        # arr.append[[nums[i] , nums[j] , nums[k]]]
        # else return arr

        # arr = []
        # seen = set()

        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         for k in range(j+ 1,len(nums)):
        #             if nums[i] + nums[j] + nums[k] == 0:
                        
        #                 triplet = sorted([nums[i],nums[j],nums[k]])
        #                 triplet_tuple = tuple(triplet)

        #                 if triplet_tuple not in seen:
        #                     seen.add(triplet_tuple)
        #                     arr.append(triplet)
        # return arr            

        nums.sort()
        
        res = []

        for i in range(len(nums)-2):# we need 3 nums so we need to leavea at least 2 spots for the 3sum
            #let's do some duplicate checks for nums[i]!
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left = i + 1
            right = len(nums) - 1

            while left < right:
                curSum = nums[i] + nums[left] + nums[right]
                if curSum < 0:
                    left +=1
                elif curSum > 0:
                    right -=1
                else:
                    triplet = [nums[i],nums[left],nums[right]]
                    res.append(triplet)
                    #let's do some duplicate checks for left and right pointers!
                    while left < right and nums[left] == triplet[1]:
                        left +=1
                    while left < right and nums[right] == triplet[2]:
                        right -=1
        return res
nums = [-2, 0, 1, 1, 2, 3, -3, -2, -1, 4]
nums = [1, 2, 3, 4, 5]
test = Solution()      
run = test.threeSum(nums)          
print(run)


