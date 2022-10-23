class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        dict = {'a': 0, 'b': 0, 'c': 0}
        
        ans = 0
        
        left = 0
        for i in range(n):
            dict[s[i]] += 1
            
            while dict['a'] >= 1 and dict['b'] >= 1 and dict['c'] >= 1:
                ans += n - i
                dict[s[left]] -= 1
                left += 1
        
        return ans