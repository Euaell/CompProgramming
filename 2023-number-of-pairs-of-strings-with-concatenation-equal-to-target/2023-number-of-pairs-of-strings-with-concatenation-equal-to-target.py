class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        n = len(nums)
        
        ans = 0
        
        for i in range(n):
            
            for j in range(n):
                if j == i:
                    continue
                if nums[i] + nums[j] == target:
                    ans += 1
                
        return ans
        