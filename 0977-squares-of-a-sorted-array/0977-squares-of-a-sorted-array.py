class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        nums = list(map(abs, nums))
        
        ans = [0] * n
        i = n - 1
        
        left = 0
        right = n - 1
        while left <= right:
            if nums[left] < nums[right]:
                ans[i] = nums[right] ** 2
                right -= 1
            else:
                ans[i] = nums[left] ** 2
                left += 1
            
            i -= 1
        
        return ans
        