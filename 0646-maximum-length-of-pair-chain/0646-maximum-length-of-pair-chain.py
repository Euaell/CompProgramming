class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        n = len(pairs)
        
        pairs.sort(key=lambda a: a[1])
        
        ans = 1      
        
        last = pairs[0][1]
        for i in range(1, n):
            if pairs[i][0] > last:
                ans += 1
                last = pairs[i][1]
        
        return ans