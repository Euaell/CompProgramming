class Solution:
    def maximumTop(self, nums: List[int], k: int) -> int:
        n = len(nums)
        
        if k > n:
            # edge case
            if n == 1 and k % 2 == 1:
                return -1                
            return max(nums)
        
        nums = nums + [-1]      
        
        left = [-1]
        if k - 1 > 0:
            left = nums[:k - 1]
        
        return max(max(left), nums[k])
        