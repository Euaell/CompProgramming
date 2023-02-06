class Solution:
    def racecar(self, target: int) -> int:
        memo = {}
        def dp(t):
            if t in memo: return memo[t]
            n = t.bit_length()
            if t == (1<<n) - 1:
                memo[t] = n
            else:
                memo[t] = dp((1<<n) - 1 - t) + n + 1
                for m in range(n-1):
                    memo[t] = min(memo[t], dp(t - (1<<(n-1)) + (1<<m)) + n-1+m+2)
            return memo[t]
        return dp(target)