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
        d={}
        
        d[None] = None
        
        tmp=head
        while tmp:
            x = Node(tmp.val)
            d[tmp] = x
            tmp = tmp.next
        
        tmp = head
        
        while tmp:
            d[tmp].random = d[tmp.random]
            d[tmp].next = d[tmp.next]
            tmp = tmp.next
        
        return d[head]