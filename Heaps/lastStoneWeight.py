class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # choosing 2 heaviest stones
        # convert the min heap to a max heap
        # heappop x2
        # compare both numbers and do if checks
        # enumerate nums -1 

        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            if second > first:
                heapq.heappush(stones, first-second)
        stones.append(0)
        return abs(stones[0])


# TC - O(nlogn)
# SC - O(n)