# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = k
        self.ans = 0
        
        def rec(node):
            if not node: return
            
            rec(node.left)
            
            self.count -= 1
            if self.count == 0: 
                self.ans = node.val
                return
            
            rec(node.right)
        
        rec(root)
        
        return self.ans