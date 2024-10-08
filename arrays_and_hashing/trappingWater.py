class Solution:
    def trap(self, height: List[int]) -> int:
        #calc maxright and maxleft array
        # get min between MaxLeft,MaxRight -> subtract, height[i]
        # count += difference btw max and height

        if len(height) == 0:
            return 0 

        water = 0
        max_left = [0] * len(height)
        max_right = [0]*len(height)
        
        #loop through maxL and fill in max values 
        max_left[0] = height[0]
        for i in range(1, len(height)):
            max_left[i] = max(max_left[i-1],height[i])

        max_right[len(height)-1] = height[len(height)-1]
        for i in range(len(height)-2,-1,-1):
            max_right[i] = max(max_right[i+1],height[i])
        
        for i in range(len(height)):
            trapped = min(max_right[i],max_left[i]) - height[i]
            if trapped > 0:
                water += trapped
        return water
    
# Time complexity - O(n)
#Space complexity - O(n)