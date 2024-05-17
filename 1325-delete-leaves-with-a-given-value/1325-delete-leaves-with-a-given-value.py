# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        if not root:
            return root
        
        # Call on the left child
        root.left = self.removeLeafNodes(root.left, target)
        
        # Call on the right child
        root.right = self.removeLeafNodes(root.right, target)
        
        # Check if the value is target and that it has no child
        if root.val == target and not root.left and not root.right:
            return None
        
        return root
        