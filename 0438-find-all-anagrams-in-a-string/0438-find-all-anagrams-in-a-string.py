class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n = len(p)
        
        # count the characters in the given string
        pDict = defaultdict(int)
        for c in p:
            pDict[c] += 1
        
        ans = []
        
        sDict = defaultdict(int)
        
        left = 0
        for right in range(len(s)):
            c = s[right]
            
            sDict[c] += 1
            
            while sDict[c] > pDict[c]:
                sDict[s[left]] -= 1
                left += 1
            
            if right - left + 1 == n:
                ans.append(left)
            
        return ans