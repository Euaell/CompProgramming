class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        
        # top-down approach
#         def rec(i, j):
#             if i > j:
#                 return 0
            
#             if s[i] != s[j]:
#                 return max(rec(i, j - 1), rec(i + 1, j))
            
#             if i == j:
#                 return 1
            
#             return 2 + rec(i + 1, j - 1)
        
#         return rec(0, n - 1)
        
        # bottom-up approach
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n + 1):
                if s[i] != s[j - 1]:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
                else:
                    dp[i][j] = dp[i + 1][j - 1] + (1 if i + 1 == j else 2)
        
        return dp[0][n]
    
        