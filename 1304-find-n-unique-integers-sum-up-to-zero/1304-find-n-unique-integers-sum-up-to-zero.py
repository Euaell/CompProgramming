class Solution:
    def sumZero(self, n: int) -> List[int]:
        values = [i + 1 for i in range(n)]
        
        values[-1] = -sum(values[:-1])
        return values