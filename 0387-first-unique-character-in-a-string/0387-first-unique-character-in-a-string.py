class Solution:
    def firstUniqChar(self, s: str) -> int:        
        n = len(s)
        count = {}
        
        for i in range(n):
            if s[i] not in count:
                count[s[i]] = 0
            count[s[i]] += 1
        
        for i in range(n):
            if count[s[i]] == 1:
                return i
        
        return -1
            