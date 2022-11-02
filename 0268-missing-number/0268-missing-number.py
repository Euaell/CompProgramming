class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        
        total = 0
        missed = n
        
        for i in range(n):
            missed ^= i
            total ^= nums[i]
        
        return total ^ missed
    