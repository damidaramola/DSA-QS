# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
       

        # check if when we swap the left side that it is the same as thr right side of the tree
        # return True or False if so 
        
        def dfs(left,right):
            if not left and not right :
                return True
            if not left or not right:
                return False
            
            return (left.val == right.val and 
            dfs(left.left,right.right) and 
            dfs(right.left,left.right))
        return dfs(root.left,root.right)
    
# TC - O(N)
# SC - O(H)