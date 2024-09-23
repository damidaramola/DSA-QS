class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        #dfs function
        # check if rows and cols are outside of bounds or if its not a 1
        # return if so 
        # if it is a 1 change it to a #
        # call dfs on all directions 

        # main function 
        # loop through rows and cols
        # if num =1 , call dfs on the row and col to find the rest of the island
        # increment the island count

        if not grid:
            return 0

        islands = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '1':
                    self.dfs(grid,r,c)

                    islands +=1
        return islands 

    def dfs(self,grid,r,c):

        if r<0 or c<0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] != '1':
            return

            

        grid[r][c] = '#'

        self.dfs(grid,r+1,c)
        self.dfs(grid,r-1,c)
        self.dfs(grid,r,c+1)
        self.dfs(grid,r,c-1)

#Time Complexity: O(M * N), where 𝑀 M is the number of rows and N is the number of columns.
#Space Complexity: O(M * N) due to the recursion stack in DFS.