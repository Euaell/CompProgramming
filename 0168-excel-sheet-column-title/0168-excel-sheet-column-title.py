class Solution:
    def convertToTitle(self, colNum: int) -> str:
        
        ans = []
        
        while colNum > 0:
            colNum -= 1
            ans.append(chr(colNum % 26 + ord('A')))
            colNum //= 26
        
        return "".join(ans[::-1])