class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # save the sign
        neg = (dividend < 0) ^ (divisor < 0)
        
        # make bothe divisor and dividend positive
        divisor = abs(divisor)
        dividend = abs(dividend)
        
        answer = 0
        for i in range(31, -1, -1):
            if (divisor << i) <= dividend:
                dividend -= (divisor << i)
                answer += (1 << i)
        
        # add sign to the answer
        if neg:
            return max(-answer, -(1 << 31))
        else:
            return min(answer, (1 << 31) - 1)