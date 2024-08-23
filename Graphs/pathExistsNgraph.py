class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # use depth first search and backtracking to
        # count different paths
        # set base case 
        # do recursion
        # loop through neighbours of source
        # return True or False if a valid path exists

        if source == destination:
            return True 
        
        graph = defaultdict(list)

        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        seen = set()
        seen.add(source)
        
        def dfs(i):
            if i == destination:
                return True
            for neighbour in graph[i]:
                if neighbour not in seen:
                    seen.add(neighbour)
                    if dfs(neighbour):
                        return True

            return False
        return dfs(source)

# TC - O(v + e)
# SP -O(V+E)