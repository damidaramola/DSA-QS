# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        # 1 - n e.g, 1-6
        # 123456
        # 0 - 5
        # 1.  use while loop , l = 1 , right = n +1
        # <=
        # 1. if num is > pick - right = mid -1, then call  guess(num) -1
        # 2. elif num < pick , left =  mid + 1 ,  1 by calling guess 1
        # 3. else:
        # call guess(i)
        # return mid
        # I dont have pick given to me? do I use guess function to get -1,1 or 0?
        # then if its 0, e.g if guess(mid) == -1:
        # mid + 1, mid -1 

        # for i in range(1,n + 1):
        #     print(guess(i))

        left = 1 
        right = n +1 

        #1 2
        while left <= right:
            mid = (right + left) // 2

            if guess(mid) == 1:
                left = mid + 1
            elif guess(mid) == -1:
                right  = mid -1
            else:
                return mid 

# 30 min
n = 10
n = 5       
#Time complexity - O(log n) - Binary search 
# space complexity - O(1)