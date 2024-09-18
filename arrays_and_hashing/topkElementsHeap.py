class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # use a hashmap to store the count of each value 
        # create a heap, and - the index values /counts 
        # and the max values from the heap into the ans array
        # loop through range k and append those values to an empty array

        
        hmap = {}
        heap = []

        for i in nums:
            hmap[i] = hmap.get(i,0) +1
        
        for key, val in hmap.items():
            heapq.heappush(heap,(-val,key))
        

        ans = []
        
        for _ in range(k):
            ans.append(heapq.heappop(heap)[1])
        return ans 
#TC- O(n log n)
#SC O(n)