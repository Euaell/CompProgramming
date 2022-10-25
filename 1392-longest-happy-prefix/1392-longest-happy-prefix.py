class Solution:
    def longestPrefix(self, s: str) -> str:
        n = len(s)
        
        lps = [0] * n
        
        i = 0
        for j in range(1, n):
            if s[j] == s[i]:
                lps[j] = i + 1
                i += 1
            else:
                while i != 0 and s[i] != s[j]:
                    i = lps[i - 1]
                
                if s[i] == s[j]:
                    lps[j] = i + 1
                    i += 1
        print(lps)
        return s[n - lps[-1]:]