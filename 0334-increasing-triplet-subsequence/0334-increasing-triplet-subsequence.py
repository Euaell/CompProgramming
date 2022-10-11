class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        n = len(nums)
        
        left = inf
        mid = inf
        
        for i in range(n):
            if nums[i] > mid: 
                return True
            
            if (left < nums[i] < mid):
                mid = nums[i]
            if (nums[i] < left): 
                left = nums[i]
        
        return False