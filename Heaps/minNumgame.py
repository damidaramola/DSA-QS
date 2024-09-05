import heapq
class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        # import heapq
        # sort the nums by heapifying it 
        # create empty array
        # alice= she is the first removal and second to append to arr
        # bob is the second removal and first to append his num to arr
        heapq.heapify(nums)
        arr= []

        while nums: # while nums not empty
            alice = heapq.heappop(nums)
            bob = heapq.heappop(nums)

            arr.append(bob)
            arr.append(alice)
        return arr

        

