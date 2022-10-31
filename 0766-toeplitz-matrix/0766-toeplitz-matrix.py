class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        m = len(matrix[0])
        
        dict = {}
        
        for i in range(n):
            for j in range(m):
                key = j - i
                if key not in dict:
                    dict[key] = matrix[i][j]
                elif dict[key] != matrix[i][j]:                    
                    return False
        
        return True