class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        
        left = nums[:n]
        right = nums[n:]
        
        ans = [0] * (2 * n)
        
        for i in range(n):
            ans[i * 2] = left[i]
            ans[i * 2 + 1] = right[i]
        
        return ans