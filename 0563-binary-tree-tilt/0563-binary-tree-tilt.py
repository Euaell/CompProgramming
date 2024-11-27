# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        
        def rec(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            
            left = rec(node.left)
            right = rec(node.right)
            s = left + right + node.val
            node.val = abs(left - right)
            
            return s
        
        rec(root)
        
        def calc(node: Optional[TreeNode]):
            if not node:
                return 0
            
            left = calc(node.left)
            right = calc(node.right)
            
            return node.val + left + right
        
        return calc(root)
