# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        def rec(node: Optional[ListNode], parent: Optional[ListNode]) -> Optional[ListNode]:
            if not node:
                return None
        
            newHead = rec(node.next, node)
            
            node.next = parent
            
            return newHead if newHead else node
        
        return rec(head, None)