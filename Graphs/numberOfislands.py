class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # set up our queue
        # set up our rows and columns
        # set data structure - visit
        # number of islands count

        # bfs search
        # deque the first row and col - popleft
        # set up 4 directions
        # loop through directions and add to row and col to traverse up, down , left, right 
        # check if the r,c is in the range, is == 1 and is not in the visted set
        # if so, add it to the set and appened to the queue

        # function 
        # loop through rows and cols in the grid and if its ==1 and not visited,
        # call bfs 
        # increment number of island 
        # return the number of islands 

        if not grid:
            return 0 
        
        rows, cols = len(grid), len(grid[0])
        
        visited = set()
        numbIslands = 0 

        def bfs(r, c):
            q = deque()
            q.append((r,c))
            visited.add((r,c))

            while q:
                row, col = q.popleft()
                directions = [[1,0],[0,1],[-1,0],[0,-1]]

                for dr,dc in directions:
                    r, c = row + dr , col + dc

                    if (r in range(rows) and c in range(cols) and grid[r][c] == "1" and (r,c) not in visited):
                        q.append((r,c))
                        visited.add((r,c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visited:
                    bfs(r,c)
                    numbIslands +=1
        return numbIslands
                

# TC  = O(r xc)
# SC = O(r x c)