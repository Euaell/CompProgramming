# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def rev(q):
            n = len(q)
            left = 0
            right = n - 1
            
            while left < right:
                q[left].val, q[right].val = q[right].val, q[left].val
                left += 1
                right -= 1
        
        que = deque([root])
        level = 0
        
        while que:
            size = len(que)
            if level % 2 == 1:
                rev(que)
            
            for _ in range(size):
                tmp = que.popleft()
                
                if tmp.left: que.append(tmp.left)
                if tmp.right: que.append(tmp.right)
            level += 1
        return root