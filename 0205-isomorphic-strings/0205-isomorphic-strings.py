class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        leaving = {}
        entering = set()
        for idx in range(len(s)):
            if s[idx] in leaving:
                if t[idx] != leaving[s[idx]]:
                    return False
            else:
                if t[idx] in entering:
                    return False
                entering.add(t[idx])
                leaving[s[idx]] = t[idx]
        return True
            
