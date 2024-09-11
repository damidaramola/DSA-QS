import heapq
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        # given k 
        # i <j if nums of soldiers is less
        # i == j but i<j
        #heaps
        # use heap sort by number of soldiers in each row 
        #.[1,1,0,0,0]
        #.   ^
        # loop through each row to get num of soldiers
        # create the heap, append the row index along with count of soldiers 
        # loop through the resulting ordered list and stop and len(range(k))
        # return

        



        heap = []
        for i, row in enumerate(mat):
            count = 0
            for r in row:
                if r == 1:
                    count +=1
            heap.append((count, i))
        
        heapq.heapify(heap)



        
        
        ans = []
        j = 0
        while j < k:
                pop = heapq.heappop(heap)
                ans.append(pop[1])
                j +=1
        return ans
                

            






#TC - O(n+k)
#SC - O(n×m+n+k)

#improve this code