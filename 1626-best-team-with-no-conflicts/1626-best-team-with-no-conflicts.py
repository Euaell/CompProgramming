class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        n = len(scores)
        memo = {}
        scoreAge = list(zip(ages, scores))
        
        scoreAge.sort()
        
#         @lru_cache(None)
#         def rec(index, lastInd):
#             if index >= n:
#                 return 0
            
#             dontPick = rec(index + 1, lastInd)
#             pick = 0
#             if lastInd == -1 or scoreAge[index][0] == scoreAge[lastInd][0] or scoreAge[index][1] >= scoreAge[lastInd][1]:
#                 pick = scoreAge[index][1] + rec(index + 1, index)
                        
#             return max(pick, dontPick)
        
#         return rec(0, -1)   

        dp = [scoreAge[i][1] for i in range(n)]
        ans = max(scores)
        
        for i in range(n):
            for j in range(i - 1, -1, -1):
                if scoreAge[i][1] >= scoreAge[j][1]:
                    dp[i] = max(dp[i], scoreAge[i][1] + dp[j])
            
            ans = max(ans, dp[i])
        
        return ans
            
            