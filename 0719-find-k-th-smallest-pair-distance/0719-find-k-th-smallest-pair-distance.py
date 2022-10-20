class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        
        # get the min and max difference between all the pairs
        minDiff = inf
        maxDiff = nums[n - 1] - nums[0]
        for i in range(0, n - 1):
            diff = nums[i + 1] - nums[i]
            minDiff = min(minDiff, diff)
        
        # binary search  
        left = minDiff
        right = maxDiff
        while left <= right:
            mid = (right + left) // 2
            
            greater = 0
            
            # sliding window
            l = 0
            for r in range(n):
                while nums[r] - nums[l] > mid:
                    l += 1
                
                greater += (r - l)
            
            if greater >= k:
                right = mid - 1
            else:
                left = mid + 1
        
        return left
        
       
            