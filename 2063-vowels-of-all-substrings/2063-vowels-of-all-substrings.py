class Solution:    
    def countVowels(self, word: str) -> int:
        n = len(word)
        
        vowel = set(['a', 'e', 'i', 'o', 'u'])
        
        ans = 0
        for i in range(n):
            c = word[i]
            
            # check if it's vowel
            if c in vowel:
                # basically add all the substrings this character forms in front of it (n - i),
                # plus all the substrings it can form with all the characters before it (n - i) * i
                # total = (n - i) + (n - i) * i
                
                ans += (n - i) * (i + 1)
        
        return ans