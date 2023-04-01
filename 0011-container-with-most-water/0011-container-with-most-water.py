class Solution:    
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        
        left = 0
        right = n - 1
        
        ans = min(height[left], height[right]) * (right - left)
        while left < right:
            ans = max(ans, min(height[left], height[right]) * (right - left))
            if height[left] > height[right]:
                right -= 1
            else: 
                left += 1
            
        
        return ans