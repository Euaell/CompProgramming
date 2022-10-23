class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        
        minDiff = inf
        maxDiff = nums[-1] - nums[0]
        for i in range(1, n):
            minDiff = min(minDiff, nums[i] - nums[i - 1])
        
        # binary search for the answer from minDiff to maxDiff
        left = minDiff
        right = maxDiff
        while left <= right:
            mid = (right + left) // 2
            
            # count the pairs with distance less or equal to mid,
            # using sliding window
            count = 0
            l = 0
            for i in range(n):
                
                while nums[i] - nums[l] > mid:
                    l += 1
                
                count += (i - l)
            
            # if true try searching for a better answer, 
            # the answer structure will look like "FFFFTTTT" so the right pointer will be
            # the right most position of the last "F" by the time the loop breaks.
            # And left will hold the left most position of the right most true which is the answer.
            if count >= k:
                right = mid - 1
            else: 
                left = mid + 1
        
        return left