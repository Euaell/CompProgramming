class Solution:
    def checkPref(self, pref, word) -> bool:
        n = len(pref)
        if len(word) < n:
            return False
        for i in range(n):
            if pref[i] != word[i]:
                return False
        return True
    
    def prefixCount(self, words: List[str], pref: str) -> int:
        
        ans = 0
        for word in words:
            if self.checkPref(pref, word):
                ans += 1
            
        return ans
    