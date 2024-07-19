class Solution:
    def mySqrt(self, x: int) -> int:
        # we are working with integers not floating points 
        # round down to nearest integer - so use // not /
        #  0 + 
        # binary search , discretely 
        #  4 
        # in between 0 and x 
        # low = 0
        # right = x 
        # use for loop 
        # get the mid ponter of x , do division // 2
        # root = none
        # sqaure_mid = mid **2
        
        # use range(x) 0,1,2,3,4,5,6,7,8    ,9
        # for i in range(x)
        #  midpoint = low + high // 2 
        # if sqaure_mid < x:
            # low = mid
        #if sqaure_mid > x:
            #high = mid
        #else:
            #mid = mid
    #return mid 
        low = 0
        high = x

        while low <=high:
            mid = (low + high) // 2
            square_mid  = mid**2
            if square_mid < x:
                low = mid + 1
            elif square_mid > x:
                high = mid - 1
            else:
                return mid
        return high 
x = 10
x= 6
# Time complexity - O(log n)
# space complexity - O(1)

test = Solution()     
run = test.mySqrt(x)
print(run)