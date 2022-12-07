class Solution:
    def minimizeTheDifference(self, mat: List[List[int]], target: int) -> int:
        
        self.answer = inf
        @lru_cache(None)
        def dp(row,total):
                
            if row == len(mat):
                
                if abs(self.answer - target ) > abs(total - target):
                    self.answer = total
                return
            
            for col in set(mat[row]):
                if total + col > target and abs(target-self.answer) <= abs(total+col - target):
                    continue
                dp(row+1,total+col)
                
        dp(0,0)
        return abs(self.answer - target)
            