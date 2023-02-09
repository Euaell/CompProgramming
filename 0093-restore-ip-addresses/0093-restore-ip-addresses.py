class Solution:
    def valid(self, s, start, length):
        return length == 1 or (s[start] != '0' and (length < 3 or s[start : start + length] <= "255"))
    
    def backTrack(self, s, startIndex, dots, ans):
        rLen = len(s) - startIndex
        rNo = 4 - len(dots)
        
        if rLen > rNo * 3 or rLen < rNo:
            return
        
        if len(dots) == 3:
            if self.valid(s, startIndex, rLen):
                sb = []
                last = 0
                for dot in dots:
                    sb.append(s[last: last + dot])
                    last += dot
                    sb.append('.')
                sb.append(s[startIndex:])
                ans.append("".join(sb))
            return
        
        for curPos in range(1, 3 + 1):
            
            dots.append(curPos)
            
            if self.valid(s, startIndex, curPos):
                self.backTrack(s, startIndex + curPos, dots, ans)
                
            dots.pop()
    
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []
        self.backTrack(s, 0, [], ans)
        return ans