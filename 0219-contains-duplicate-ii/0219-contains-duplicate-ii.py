class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        
        left = 0
        counter = defaultdict(int)
        Max = 0
        for right in range(n):
            i = nums[right]
            counter[i] += 1
            
            if right - left > k:
                counter[nums[left]] -= 1
                left += 1
            
            Max = max(Max, counter[i])
        
        return Max > 1