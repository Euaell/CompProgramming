class Solution:
    def numberOfWays(self, s: str) -> int:
        n = len(s)
        z = 0
        o = 0
        
        tmp = [0] * n
        
        for i in range(n - 1, -1, -1):
            
            if s[i] == '1':
                tmp[i] = z
                o += 1
            else:     
                tmp[i] = o
                z += 1
        
        zo = 0
        oz = 0
        
        ans = 0
        for i in range(n - 1, -1, -1):
            if s[i] == '1':
                oz += tmp[i]
                ans += zo
            else:
                zo += tmp[i]
                ans += oz
        return ans
    