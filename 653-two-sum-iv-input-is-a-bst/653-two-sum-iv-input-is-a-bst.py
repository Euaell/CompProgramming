# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        
        dict = {}
        
        def inOrd(node):
            if not node: 
                return False
            
            dict[node.val] = node
            ans = False
            ans |= inOrd(node.left)
            ans |= inOrd(node.right)
            
            return ans or (k - node.val in dict and dict[k - node.val] != node)
        
        return inOrd(root)
            