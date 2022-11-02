class Solution:
    def isValid(self, grid, row, col):
        return 0 <= row < len(grid) and 0 <= col < len(grid[0]) and grid[row][col] != -1
    
    def backTrack(self, grid, directions, path, row, col, target) -> int:
        if grid[row][col] == 2:
            if 0 == target - 1:
                return 1
            else: 
                return 0
        
        path.add((row, col))
        ans = 0
        for r, c in directions:
            nR, nC = row + r, col + c
            if self.isValid(grid, nR, nC) and (nR, nC) not in path:
                ans += self.backTrack(grid, directions, path, nR, nC, target - 1)
        
        path.remove((row, col))
        return ans
        
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        
        startRow, startCol = 0, 0
        target = n * m
        # iterate through the grid to get the total number of non-obstacle cells and start cell
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    startRow, startCol = i, j
                elif grid[i][j] == -1:
                    target -= 1
        # print((startRow, startCol), target)
        return self.backTrack(grid, directions, set(), startRow, startCol, target)