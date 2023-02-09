class Solution:
    def valid(self, s, start, length):
        return length == 1 or (s[start] != '0' and (length < 3 or s[start : start + length] <= "255"))
    
    def backTrack(self, s, startIndex, dots, ans):
        remLen = len(s) - startIndex
        remNo = 4 - len(dots)
        if remLen > remNo * 3 or remLen < remNo:
            return
        if len(dots) == 3:
            if self.valid(s, startIndex, remLen):
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
            # Append a dot at the current position.
            dots.append(curPos)
            # Try making all combinations with the remaining string.
            if self.valid(s, startIndex, curPos):
                self.backTrack(s, startIndex + curPos, dots, ans)
            # Backtrack, i.e. remove the dot to try placing it at the next position.
            dots.pop()
    
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []
        self.backTrack(s, 0, [], ans)
        return ans