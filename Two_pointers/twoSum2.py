#r, left pointers, increment,decrement

class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        # input = 1 indexed [array of ascending nums]
        # out uput (1 indexed) of both numbers adding to target 

        # my solution
        # create hshmap to store key and value
        # loop through enumerate, range(1,len + 1)
        # check for difference
        # if its in the hashmap , append i to a list and diff[]
        # return the list

        # actual solution
        # if in contant time we use 2 pointers
        # i is at beginning, is at end
        # increase/decrease pointers - if value is to small/big
        
        i = 0
        j = len(numbers) - 1

        while i < j :
            if numbers[i] + numbers[j] < target:
                i +=1
            elif numbers[i] + numbers[j] > target:
                j -=1
            else:
                return [i + 1,j + 1]
            
            
numbers = [1, 2, 3, 4, 6]
target = 6
numbers = [2, 3, 4, 10, 20]
target = 14
test = Solution()
run = test.twoSum(numbers,target)
print(run)