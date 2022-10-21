class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        s1Dict = defaultdict(int)
        for c in s1:
            s1Dict[c] += 1
        
        left = 0
        s2Dict = defaultdict(int)
        for i in range(len(s2)):
            c = s2[i]
            
            s2Dict[c] += 1
            
            while s2Dict[c] > s1Dict[c] and left <= i:
                s2Dict[s2[left]] -= 1
                left += 1
        
            if i - left + 1 == n:
                return True
        
        return False