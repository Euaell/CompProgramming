# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        
        vis = set() 
        
        def inOrd(node):
            if not node: 
                return False
            
            ans = k - node.val in vis
            vis.add(node.val)
            ans |= inOrd(node.left)
            ans |= inOrd(node.right)
            
            return ans
        
        return inOrd(root)
            