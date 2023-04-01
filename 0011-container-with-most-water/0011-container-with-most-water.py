class Solution:
    def calc(self, l, r, height):
        ans = min(height[l], height[r]) * (r - l)
        # print(ans)
        return ans
    
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        
        left = 0
        right = n - 1
        
        ans = self.calc(left, right, height)
        while left < right:
            ans = max(ans, self.calc(left, right, height))
            if height[left] > height[right]:
                right -= 1
            else: 
                left += 1
            
        
        return ans
        # return min(height[left], height[right]) * (right - left)