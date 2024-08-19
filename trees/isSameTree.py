# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # p and q are the whole tree 
        # check if the values in the left and right branches are the same 
        # if so return true 
        # else False 
        # recursion then apply it to the left and right of each tree?

        if not p and  not q:
            return True

        if not p or not q:
            return False

        if p.val == q.val:
            return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
        return False
    
# time complexity - O(N,M)
# space complexity - O(H1,H2)