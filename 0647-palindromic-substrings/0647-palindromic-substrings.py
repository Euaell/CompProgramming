class Solution:
    def counter(self, left: int, right: int, s: str) -> int:
        count = 0
        
        while left >= 0 and right < len(s) and s[left] == s[right]:
            count += 1
            left -= 1
            right += 1
        
        return count
        
    def countSubstrings(self, s: str) -> int:
        ans = 0
        
        for i in range(len(s)):
            ans += self.counter(i, i, s) + self.counter(i, i + 1, s)
        
        return ans