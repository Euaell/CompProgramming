# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isValid(self, row, col, matrix):
        
        return 0 <= row < len(matrix) and 0 <= col < len(matrix[0]) and matrix[row][col] == -1
    
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        
        matrix = [[-1 for col in range(n)] for row in range(m)]
        direction = {0 : (0, 1), 1 : (1, 0), 2: (0, -1), 3 : (-1, 0)}
        
        return self.rec(0, 0, matrix, head, 0, direction)
    
    def rec(self, row, col, matrix, head, arrow, direction):
       
        matrix[row][col]=head.val
        
        if head.next == None:
            return matrix
        
        if self.isValid(row + direction[arrow][0], col + direction[arrow][1], matrix):
            
            return self.rec(row + direction[arrow][0], col + direction[arrow][1], matrix, head.next, arrow, direction)
        
        new_arrow = ( arrow + 1)%4
        
        return self.rec(row + direction[new_arrow][0], col + direction[new_arrow][1], matrix, head.next, new_arrow, direction)
        
        
        