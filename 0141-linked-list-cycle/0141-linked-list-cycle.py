# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        path = set()
        while head:
            if head in path:
                return True
            path.add(head)
            head = head.next
            
        return False
    