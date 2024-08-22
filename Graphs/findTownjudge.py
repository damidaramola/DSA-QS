class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        

        in_trust = [0] * (n+1)
        out_trust = [0] * (n+1)

        for u,v in trust:
            in_trust[v] +=1
            out_trust[u] +=1

    
        for i in range(1,n+1):
            if in_trust[i] == n-1 and out_trust[i] == 0:
                return i
        return -1 

# Time complexity - 0(n+m)
# Space Complexity O(n)