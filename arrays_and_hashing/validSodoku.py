class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        #check if string has duplicates across or down in 9x9 or 3x3
        #return True/False if so or not
        #dfs bfs algo?

        #Set up 3 arrays, each of which contain 9 arrays
        rows = [[] for _ in range(9)]
        cols = [[] for _ in range(9)]
        boxes = [[] for _ in range(9)]

        # a loop for the rows and an inner-loop for the columns:
        #to access the top left Sudoku cell, the co-ordinates would be 0,0 and the bottom right cell co-ordinates would be 8,8
        #we’re checking first if cell has a value, then we’re checking if the value already exists in our arrays. If a duplicate is found, 
        #we return false without running through the rest of the code, otherwise, we keep going
        for i in range(len(board)):
            for j in range(len(board)):
                cell = board[i][j]
                if cell != ".":
                    if cell in rows[i]:
                        return False
                    else:
                        rows[i].append(cell)

                    if cell in cols[j]:
                        return False
                    else:
                        cols[j].append(cell)
                
                    box_index = (i//3)*3+(j//3)

                    if cell in boxes[box_index]:
                        return
                    else:
                
                        boxes[box_index].append(cell)
        return True
    
# board = [["5","3",".",".","9",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","9",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]

board = [["5","3",".",".","4",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
test = Solution()
run = test.isValidSudoku(board)
print(run)

#Time complexity O(n^2) looing through values in rows and cols
# Space complexity O(1) constant space independant of the input size