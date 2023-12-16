class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        m = len(grid[0])
        
        onesRow = [0] * n
        onesCol = [0] * m
        zerosRow = [0] * n
        zerosCol = [0] * m
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    zerosCol[j] += 1
                    zerosRow[i] += 1
                else:
                    onesCol[j] += 1
                    onesRow[i] += 1
        
        ans = [[0 for _ in range(m)] for _ in range(n)]
        
        for i in range(n):
            for j in range(m):
                ans[i][j] = onesRow[i] + onesCol[j] - zerosRow[i] - zerosCol[j]
        
        return ans
