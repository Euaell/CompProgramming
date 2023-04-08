"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        
        visited = {}
        
        def dfs(t):
            if not t:
                return None
            
            if t.val in visited:
                return visited[t.val]
            
            visited[t.val] = Node(t.val)
            
            arr = []
            
            for ne in t.neighbors:
                tmp = dfs(ne)
                if tmp:
                    arr.append(tmp)            
            
            visited[t.val].neighbors = arr
            return visited[t.val]
            # return Node(t.val, arr)
        
        return dfs(node)
    