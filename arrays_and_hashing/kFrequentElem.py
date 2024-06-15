#sort,descending order, len(res) == k:


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        #initial approach
        # count each occurance of num in hashmap
        #emoty array
        #iterate through keys return k values with most occurences
        #append the empty array with those values 
        #return 
        #how do I get k most values?, sort by descendng order
        # [2,3,2,2,7,2,7,5]
        # hmap[num] >
        # append k + 1
        # return the k keys with the values that have the highest count

        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            count[num] = count.get(num,0) + 1
        
        for num,c in count.items():
            freq[c].append(num)
        res = []

        for i in range(len(freq) -1,0,-1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res 

    #Time complexity = O(n)
    #Space complextity = O(n)

# nums = [1,2,3,4,4,1,1,4,5] 
# k=3
nums = [1,2,3,7,7,1,3,4,5] 
k=2

test = Solution()
run = test.topKFrequent(nums,k)
print(run)