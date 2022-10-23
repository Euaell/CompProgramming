class Solution:
    def check(self, dict):
        for k, v in dict.items():
            if v == 0:
                return False
        
        return True
    
    def countVowels(self, word: str) -> int:
        n = len(word)
        
        vowel = set(['a', 'e', 'i', 'o', 'u'])
        
        ans = 0
        for i in range(n):
            c = word[i]
            
            # check if it's vowel
            if c in vowel:
                
                ans += (n - i) * (i + 1)
        
        return ans