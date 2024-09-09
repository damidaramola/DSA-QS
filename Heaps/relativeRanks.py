class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        # turn a min heap into a max heap
        # for the first 3 times you pop, you give it a place
        # other times you give it the positions of its index + 1
        N = len(score)
        
        # Create a max-heap using negative scores
        heap = []
        for idx, s in enumerate(score):  # Use `idx` for index and `s` for score
            heapq.heappush(heap, (-s, idx))

        # Initialize rank placement
        place = 1
        positions = ["" for _ in range(N)]  # List to store the results

        while heap:
            _, indexing = heapq.heappop(heap)  # Extract the index
            if place == 1:
                positions[indexing] = 'Gold Medal'
            elif place == 2:
                positions[indexing] = 'Silver Medal'
            elif place == 3:
                positions[indexing] = 'Bronze Medal'
            else:
                positions[indexing] = str(place)
            place += 1
        
        return positions


# Time complexity O(n log n) - due to Heap operations
# Space complexity O(n) - Due to heap storage