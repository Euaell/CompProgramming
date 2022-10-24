class Solution:
    def count(self, s: str):
        count = 0
        for c in s:
            if c == '1':
                count += 1
        
        return count
    
    def numberOfBeams(self, bank: List[str]) -> int:
        ans = 0
        lastCount = -1
        for s in bank:
            count = self.count(s)
            if count == 0: continue
            
            if lastCount == -1:
                lastCount = count
            else:
                ans += lastCount * count
                lastCount = count
        
        return ans