class Solution:
    def reverse(self, x: int) -> int:
        Max = 2 ** 31 - 1
        ans = []
        isNeg = x < 0
        if isNeg:
            x = -x
        
        nonZeroEncountered = False
        
        while x > 0:
            tmp = x % 10
            x //= 10
            if tmp != 0 or nonZeroEncountered:
                ans.append(tmp)
                nonZeroEncountered = True
                
        answer = 0
        for d in ans:
            answer *= 10
            answer += d
            if answer > Max:
                return 0
        
        if isNeg:
            answer = -answer
        
        return answer