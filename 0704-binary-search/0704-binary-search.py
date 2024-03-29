class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        n = len(nums)
        left = 0
        right = n - 1
        
        while left <= right:
            mid = (right + left) // 2
            
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return mid
        
        return -1