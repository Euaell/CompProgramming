class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        totSum = sum(nums)
        
        Max = -inf
        Sum = 0
        for i in range(n):
            Sum += nums[i]
            Max = max(Max, Sum)
            if Sum < 0:
                Sum = 0
        
        # now figure out the inner min
        Min = inf
        Sum = 0
        for i in range(n):
            Sum += nums[i]
            Min = min(Min, Sum)
            if Sum > 0:
                Sum = 0
        
        ans = max(Max, totSum - Min)
        if ans == 0:
            return Max
        return ans