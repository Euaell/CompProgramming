class Solution:
    def maxArea(self, h: int, w: int, hCuts: List[int], vCuts: List[int]) -> int:
        
        mod = 1_000_000_007
        
        hCuts.sort()
        vCuts.sort()
        
        maxH = hCuts[0]
        for i in range(1, len(hCuts)):
            maxH = max(maxH, hCuts[i] - hCuts[i - 1])
        maxH = max(maxH, h - hCuts[-1])
        
        maxV = vCuts[0]
        for i in range(1, len(vCuts)):
            maxV = max(maxV, vCuts[i] - vCuts[i - 1])
        maxV = max(maxV, w - vCuts[-1])
        
        return (maxV * maxH) % mod