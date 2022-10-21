class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        n = len(nums)
        
        nums.sort()
        
        maxDiff = nums[-1] - nums[0]
        minDiff = inf
        for i in range(n - 1):
            minDiff = min(minDiff, nums[i + 1] - nums[i])
        
        # binary search
        left = minDiff
        right = maxDiff
        ans = right
        while left <= right:
            mid = (right + left) // 2
            
            # count the number of pair that have distance less or equal to mid
            greater = 0
            l = 0
            for r in range(n):
                
                while nums[r] - nums[l] > mid:
                    l += 1
                
                # A single "l" can form l - r pairs, meaning with every element in the window except itself
                greater += (r - l)
            
            if greater >= k:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return ans