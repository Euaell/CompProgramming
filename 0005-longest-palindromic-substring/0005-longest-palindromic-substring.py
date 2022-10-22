class Solution:
    def counter(self, left: int, right: int, s: str) -> str:
        count = 0
        
        while left >= 0 and right < len(s) and s[left] == s[right]:
            count += 1
            left -= 1
            right += 1
        
        return s[(left+1):right]
    
    def longestPalindrome(self, s: str) -> str:
        
        ans = ""
        
        for i in range(len(s)):
            # ans = max(ans, self.counter(i, i, s), self.counter(i, i + 1, s))
            s1 = self.counter(i, i, s)
            if len(s1) > len(ans):
                ans = s1
            
            s2 = self.counter(i, i + 1, s)
            if len(s2) > len(ans):
                ans = s2
        
        return ans