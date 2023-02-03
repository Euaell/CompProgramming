class Solution:
    def checkPalindrom(self, s: str, l, r) -> bool:
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True
    def validPalindrome(self, s: str) -> bool:
        n = len(s)
        
        left = 0
        right = n - 1
        count = 0
        while left <= right:
            if s[left] != s[right]:
                return self.checkPalindrom(s, left + 1, right) or self.checkPalindrom(s, left, right - 1)
            
            left += 1
            right -= 1
        
        return count <= 1