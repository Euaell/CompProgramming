class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        
        carry = 1
        for i in range(n - 1, -1, -1):
            tmp = digits[i] + carry
            digits[i] = tmp % 10
            carry = tmp // 10
        
        if carry:
            return [1] + digits
        
        return digits