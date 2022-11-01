class Solution:
    def isValid(self, grid: List[List[int]], row: int, col: int, last):
        return 0 <= row < len(grid) and 0 <= col < len(grid[0]) and grid[row][col] == last
    
    def findExit(self, grid: List[List[int]], row: int, col: int) -> int:
        if row == len(grid):
            return col

        if grid[row][col] == -1:
            # go left
            if self.isValid(grid, row, col - 1, -1):
                return self.findExit(grid, row + 1, col - 1)
            return -1
        else:
            # go right
            if self.isValid(grid, row, col + 1, 1):
                return self.findExit(grid, row + 1, col + 1)
            return -1    
    
    def findBall(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        m = len(grid[0])
        
        answer = [-1] * m
        for i in range(m):
            answer[i] = self.findExit(grid, 0, i)
        
        return answer