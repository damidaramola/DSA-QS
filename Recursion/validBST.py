# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# recursion using dfs 
# helper function to check if node is less than max val and < than min val
# call function on left and right nodes of root 
# set boundaries to += infinity 
# call helper function at the end on root and +- inf -> float('inf)

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def valid(node, min_val, max_val):

            if not node:
                return True 
            if not (node.val > min_val and node.val < max_val):
                return False 
        
            return (valid(node.left,min_val,node.val) and valid(node.right,node.val, max_val))

        return valid(root, float('-inf'), float('inf'))
        