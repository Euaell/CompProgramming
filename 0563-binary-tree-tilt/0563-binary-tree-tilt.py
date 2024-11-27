# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.sum = 0

    def calc(self, node: Optional[TreeNode]) -> int:
        if not node:
            return 0
        
        left = self.calc(node.left)
        right = self.calc(node.right)
        
        self.sum += abs(left - right)
        
        return left + right + node.val
        
    def findTilt(self, root: Optional[TreeNode]) -> int:
        self.calc(root)
        
        return self.sum
