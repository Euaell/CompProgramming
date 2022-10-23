class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        
        left = 1
        right = n - 1
        
        while left <= right:
            # guess the answer
            mid = (right + left) // 2
            
            # count the number of element less and greater than mid
            l = 0
            g = 0
            for i in range(n):
                if nums[i] > mid:
                    g += 1
                if nums[i] < mid:
                    l += 1
            
            # expected number of elements to be greater than mid = (n - 1) - mid,
            # the last number in the list minus mid.
            # This can also be done by using elements less than mid
            
            if g > (n - 1) - mid:
                left = mid + 1
            else:
                right = mid - 1
        
        return left