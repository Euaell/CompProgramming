# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        dict = {}
        
        def rec(node, col, depth):
            if not node:
                return
            
            if col not in dict:
                dict[col] = []
            
            dict[col].append((depth, node.val))            
            rec(node.left, col - 1, depth + 1)
            rec(node.right, col + 1, depth + 1)
        
        rec(root, 0, 0)
        
        for k, v in dict.items():
            v.sort()
        
        keys = list(dict.keys())
        keys.sort()
        sortedDict = {i: dict[i] for i in keys}
        
        ans = []
        for k, v in sortedDict.items():
            tmp = []
            for v1, v2 in v:
                tmp.append(v2)
            ans.append(tmp)
      
        return ans
            