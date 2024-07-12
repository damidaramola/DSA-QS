#two pointers, while loop


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        maxProf = 0
        left = 0
        right = 1
        
        while right < len(prices):
            if prices[left] < prices[right]:
                diff = prices[right] - prices[left]
                maxProf = max(maxProf, diff)
            else:
                left = right
            right += 1
        return maxProf

prices = [7,2,2,15,3]  
# prices = [1,2,42,17,3]  
test = Solution()     
run = test.maxProfit(prices)
print(run)

#Time complexity 
# O(n)
# Space complexity 
#O(1)