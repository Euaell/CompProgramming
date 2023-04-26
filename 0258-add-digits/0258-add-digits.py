class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return num
        ans = num % 9
                
        return 9 if ans == 0 else ans
    