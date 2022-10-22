class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        
        # top-down approach
        def rec(i, j):
            if i >= n or j >= m:
                return 0
            
            if text1[i] == text2[j]:
                return 1 + rec(i + 1, j + 1)
            
            return max(rec(i + 1, j), rec(i, j + 1))
        
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i][j + 1], dp[i + 1][j])
        
        return dp[0][0]