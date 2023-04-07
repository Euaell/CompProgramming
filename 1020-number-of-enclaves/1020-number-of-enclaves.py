class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        
        dirs = {(-1, 0), (1, 0), (0, -1), (0, 1)}
        
        def makeZero(i, j):
            if i < 0 or j < 0 or i >= n or j >= m:
                return
            
            if grid[i][j] == 1:
                grid[i][j] = 0
                for r, c in dirs:
                    makeZero(i + r, j + c)
        
        for j in range(m):
            makeZero(0, j)
            makeZero(n - 1, m - 1 - j)
        
        for i in range(n):
            makeZero(i, 0)
            makeZero(n - 1 - i, m - 1)
          
        count = 0
        for i in range(n):
            for j in range(m):
                count += grid[i][j]
            
        return count
                    
            