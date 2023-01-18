class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        
        Sum = 0
        Max = -inf
        
        for i in range(n):
            Sum += nums[i]
            
            Max = max(Sum, Max)
            if Sum < 0:
                Sum = 0
            
        return Max