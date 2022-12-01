class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        n = len(s)
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        
        vowelCount = [0, 0]
        half = n//2
        
        for i in range(n):
            if s[i] in vowels:
                vowelCount[i//half] += 1
        
        return vowelCount[0] == vowelCount[1]