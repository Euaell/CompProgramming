class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        n = len(nums)
        
        ans = 0
        nums.sort()
        
        last = 0
        
        for i in range(n):
            if nums[i] != last:
                ans += 1
                last = nums[i]
            
        return ans