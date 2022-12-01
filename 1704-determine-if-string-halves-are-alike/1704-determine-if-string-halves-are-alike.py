class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        n = len(s)
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        
        firstHalf = 0
        secondHalf = 0
        
        for i in range(n//2):
            if s[i] in vowels:
                firstHalf += 1
        
        for i in range(n//2, n):
            if s[i] in vowels:
                secondHalf += 1
        
        return firstHalf == secondHalf