class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        n = len(nums)
        mod = 1_000_000_007
        
        heapq.heapify(nums)
        
        while k > 0:
            heapq.heappush(nums, heapq.heappop(nums) + 1)
            k -= 1
        
        ans = 1
        for num in nums:
            ans = (ans * num) % mod
        
        return ans