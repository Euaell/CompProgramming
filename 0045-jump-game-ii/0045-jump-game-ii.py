class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        memo = [0] * n
        
        for i in range(n - 2, -1, -1):
            Min = 100_000_000
            j = i + 1
            while j <= i + nums[i] and j < n:
                Min = min(Min, memo[j])
                j += 1
            
            memo[i] = Min + 1;
        
        return memo[0]
        