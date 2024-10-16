class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # starts,(0,0)
        #ends len(grid)-1,len(grid)-1
        # path is 0's
        # 8 directionally , 
        # keep track of distance
        # create the lens and cols 
        # first r and c is 0,0 
        # append that to a queue, also mark as visited 
        # if row,col == len(grid)-1,len(grid)-1, return count
        # start search in bfs, pop the first coordinates
        # do check in of bounds
        #if number == 0
        # check all 8 directions 
        # append then mark as visited 
        #increment the count

        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1

        rows, cols = len(grid), len(grid[0])
        q = deque()
        visited = set()
        q.append((0,0,1))
        visited.add((0,0))

        
        directions = [
            (-1,0),(1,0),(0,-1),(0,1),
            (-1,-1),(-1,1),(1,-1),(1,1)
        ]
        while q:
            r, c, distance = q.popleft()

            if (r,c) == (rows -1, cols-1):
                return distance

            

            for dr, dc in directions:
                new_r,new_c = r + dr ,c + dc 
                if (new_r < rows and new_c < cols and new_r >= 0 and new_c >= 0 and (new_r,new_c) not in visited and grid[new_r][new_c] == 0):
                    q.append((new_r,new_c,distance+1))
                    visited.add((new_r,new_c))
        return -1
    
# TC - O(mxn), worst case visit all cells in grid
# SC - O(mxn), adding cells to queue and set