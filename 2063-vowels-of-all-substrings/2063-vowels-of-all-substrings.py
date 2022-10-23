class Solution:
    def check(self, dict):
        for k, v in dict.items():
            if v == 0:
                return False
        
        return True
    
    def countVowels(self, word: str) -> int:
        n = len(word)
        
        dict = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
        
        ans = 0
        for i in range(n):
            c = word[i]
            
            # check if it's vowel
            if c in dict:
                ans += (n - i) * (i + 1)
        
        return ans