class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n + 1):
                if s[i] != s[j - 1]:
                    dp[i][j] = max(dp[i][j - 1], dp[i + 1][j])
                else:
                    dp[i][j] = dp[i + 1][j - 1] + (1 if i == j - 1 else 2)
        
        return dp[0][n]