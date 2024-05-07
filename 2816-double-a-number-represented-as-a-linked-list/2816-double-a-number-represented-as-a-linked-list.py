# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def doub(node: Optional[ListNode]):
            if not node:
                return 0
            
            remainder = doub(node.next)
            
            node.val = node.val * 2 + remainder
            ans = node.val // 10
            
            node.val %= 10
            
            return ans
        
        ans = doub(head)
        
        if ans != 0:
            return ListNode(ans, head)       
        
        
        return head