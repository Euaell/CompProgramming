class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        n = len(s)
        vowels = {'a', 'e', 'i', 'o', 'u'}
        
        ans = 0
        count = 0
        
        left = 0
        for i in range(n):
            if s[i] in vowels:
                count += 1
            
            if i - left + 1 == k:
                ans = max(ans, count)
                
                if s[left] in vowels:
                    count -= 1
                
                left += 1
        
        return ans