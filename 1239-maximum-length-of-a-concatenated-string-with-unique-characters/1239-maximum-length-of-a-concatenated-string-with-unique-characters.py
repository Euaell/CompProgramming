class Solution:
    def concat(self, s1, s2):
        vis = set(s1)
        for c in s2:
            if c not in vis:
                vis.add(c)
            else: return ""
        
        return s1 + s2            
    
    def backTrack(self, s: str, ind: int, arr: List[str]) -> int:
        ans = 0
        for i in range(ind, len(arr)):
            tmp = self.concat(s, arr[i])
            ans = max(ans, len(tmp))
            if len(tmp) > 0:
                tmp2 = self.backTrack(tmp, i + 1, arr)
                ans = max(ans, tmp2)
         
        
        return ans
    
    def maxLength(self, arr: List[str]) -> int:
        
        return self.backTrack("", 0, arr)
                    
        