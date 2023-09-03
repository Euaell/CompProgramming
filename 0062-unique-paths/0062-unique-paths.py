class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        directions = [(0, 1), (1, 0)]
        
        def IsValid(i, j) -> bool:
            return 0 <= i < m and 0 <= j < n
        
        @lru_cache(None)
        def backTrack(i: int, j: int) -> int:
            if i == m - 1 and j == n - 1:
                return 1
            if not IsValid(i, j):
                return 0
            
            ret = 0
            for r, c in directions:
                ret += backTrack(i + r, j + c)
                
            return ret
          
        ans = backTrack(0, 0)
        
        return ans
        
        