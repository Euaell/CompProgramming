# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        
        l = []
        while node:
            if node.val == 0:
                sum = 0
                tmp = node.next
                while tmp and tmp.val != 0:
                    sum += tmp.val
                    tmp = tmp.next
                if sum != 0: l.append(sum)
                node = tmp
        
        root = ListNode()
        node = root
        for i in l:
            node.next = ListNode(i)
            node = node.next
        
        return root.next