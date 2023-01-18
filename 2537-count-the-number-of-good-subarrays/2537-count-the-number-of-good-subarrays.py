
class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dict = defaultdict(int)
        
        pairs = 0
        ans = 0
        
        left = 0
        for i in range(n):
            c = nums[i]
            dict[c] += 1
            if dict[c] > 1:
                pairs += dict[c] - 1
            
            while pairs >= k:
                ans += n - i
                pairs -= dict[nums[left]] - 1
                dict[nums[left]] -= 1
                left += 1               
                
        return ans