class Solution:
    
    def isValid(self,row,col,matrix):
        
        return 0 <= row < len(matrix) and 0 <= col < len(matrix[0]) and matrix[row][col]==0
    
    def generateMatrix(self, n: int) -> List[List[int]]:
        
        answer = [[0 for i in range(n)] for i in range(n)]
        direction = {0:(0, 1), 1:(1, 0),2: (0, -1),3: (-1, 0)}
        
        return self.dfs(0, 0,answer, 1,0,direction )
        
    def dfs(self,row,col,matrix,val,arrow,direction):
        
        matrix[row][col]=val
        
        if val == len(matrix)*len(matrix):
            return matrix
        
        
       
        if self.isValid(row+ direction[arrow][0],col+ direction[arrow][1],matrix):
            
            return self.dfs(row + direction[arrow][0],col+direction[arrow][1],matrix,val+1,arrow,direction)
        
        new_arrow = (arrow + 1 )%4
        
        return self.dfs(row + direction[new_arrow][0],col + direction[new_arrow][1],matrix,val+1,new_arrow,direction)