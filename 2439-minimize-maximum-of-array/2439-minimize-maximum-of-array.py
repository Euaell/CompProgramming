class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        n = len(nums)
        
        Sum = 0
        ans = 0
        for i in range(n):
            Sum += nums[i]
            ans = max(ans, ceil(Sum / (i + 1)))
            
        return ans
        