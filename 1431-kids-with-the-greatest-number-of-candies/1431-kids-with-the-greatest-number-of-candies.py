class Solution:
    def kidsWithCandies(self, candies: List[int], e: int) -> List[bool]:
        n = len(candies)
        m = max(candies)
        
        result = [False] * n
        for i in range(n):
            if candies[i] + e >= m:
                result[i] = True
        
        return result
        