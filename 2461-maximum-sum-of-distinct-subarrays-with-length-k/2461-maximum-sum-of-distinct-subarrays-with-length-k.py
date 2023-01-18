class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        
        enc = defaultdict(int)
        
        ans = 0
        Sum = 0        
        
        left = 0
        for i in range(n):
            Sum += nums[i]
            enc[nums[i]] += 1
            
            if i - left + 1 == k:
                if len(enc) == k and Sum > ans:
                    ans = Sum
                
                Sum -= nums[left]
                enc[nums[left]] -= 1
                if enc[nums[left]] == 0:
                    enc.pop(nums[left])
                left += 1
        
        return ans
    