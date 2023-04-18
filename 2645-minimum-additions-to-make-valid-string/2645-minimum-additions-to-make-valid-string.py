class Solution:
    def addMinimum(self, word: str) -> int:
        n = len(word)
        target = "abc"
        i = 0
        
        ans = 0
        for j in range(n):
            while target[i] != word[j]:
                ans += 1
                i = (i + 1) % 3
            
            if target[i] == word[j]:
                i = (i + 1) % 3
        
        ans += (3 - i) % 3
        
        return ans        
        