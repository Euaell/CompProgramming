class Solution:
    def constructStr(self, s: str, bitMask) -> str:
        newS = list(s)
        n = len(s)
        for i in range(n):
            if bitMask & (1 << i):
                newS[i] = newS[i].upper()
            else:
                newS[i] = newS[i].lower()
                
        return "".join(newS)
    
    def backTrack(self, s: str, index: int, bitMask, answer):
        if index == len(s):
            answer.append(self.constructStr(s, bitMask))
            return
        
        if s[index].isnumeric():
            self.backTrack(s, index + 1, bitMask, answer)
        else:
            # lower or OFF bit
            self.backTrack(s, index + 1, bitMask & ~(1 << index), answer)
            # upper or ON bit
            self.backTrack(s, index + 1, bitMask | (1 << index), answer)
        
    def letterCasePermutation(self, s: str) -> List[str]:
        answer = []
            
        self.backTrack(s, 0, 0, answer)
        
        return answer
        