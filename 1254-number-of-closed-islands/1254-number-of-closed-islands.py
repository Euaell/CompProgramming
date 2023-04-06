class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        
        directions = {(0, 1), (1, 0), (-1, 0), (0, -1)}
        visited = {}
        
        def rec(i, j):
            if i < 0 or j < 0 or j >= m or i >= n:
                return False
            if grid[i][j] == 1:
                return True
            
            if (i, j) not in visited:
                
                visited[(i, j)] = True
                if grid[i][j] == 0:
                    for r, c in directions:
                         visited[(i, j)] =  visited[(i, j)] and rec(i + r, j + c)
            
            return visited[(i, j)]
        
        count = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0 and (i, j) not in visited and rec(i, j):
                    count += 1
        
        return count