"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        visited = {}
        
        def dfs(t):
            if not t:
                return None
            if t in visited:
                return visited[t]
            
            visited[t] = Node(t.val)
            
            if t.next:
                visited[t].next = dfs(t.next)
            
            if t.random:
                visited[t].random = dfs(t.random)       
            
            return visited[t]
        
        return dfs(head)