class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        n = len(nums)
        arr = [-nums[i] for i in range(n)]
        
        heapq.heapify(arr)
        score = 0
        
        while k > 0:
            tmp = -heapq.heappop(arr)
            score += tmp
            heapq.heappush(arr, -ceil(tmp/3))
            k -= 1
            
        return score