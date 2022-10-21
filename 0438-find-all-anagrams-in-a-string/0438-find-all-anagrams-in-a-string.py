class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n = len(p)
        pDict = defaultdict(int)
        for c in p:
            pDict[c] += 1
        
        ans = []
        
        left = 0
        sDict = defaultdict(int)
        for i in range(len(s)):
            c = s[i]
            
            sDict[c] += 1
            
            while sDict[c] > pDict[c] and left <= i:
                sDict[s[left]] -= 1
                left += 1
        
            if i - left + 1 == n:
                ans.append(left)
        
        return ans