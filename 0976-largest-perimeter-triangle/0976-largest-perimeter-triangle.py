class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        
        for c in range(n - 1, 1, -1):
            if nums[c - 1] + nums[c - 2] <= nums[c]: continue
            
            return nums[c - 1] + nums[c - 2] + nums[c]
        return 0
            