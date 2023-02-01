class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        n = len(mat)
        m = len(mat[0])
        
        preFix = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
        
        for i in range(1, n + 1):
            Sum = 0            
            for j in range(1, m + 1):
                Sum += mat[i - 1][j - 1]
                tmp = preFix[i-1][j]
                preFix[i][j] = Sum + preFix[i - 1][j]
        
        for i in range(n):
            r1 = max(0, i - k) + 1
            r2 = min(i + k, n - 1) + 1
            for j in range(m):
                c1 = max(0, j - k) + 1
                c2 = min(j + k, m - 1) + 1
                
                mat[i][j] = preFix[r2][c2] - preFix[r1 - 1][c2] - preFix[r2][c1 - 1] + preFix[r1 - 1][c1 - 1]
        
        return mat
    