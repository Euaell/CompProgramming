class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        n = len(plants)
        
        l = 0
        r = n - 1
        
        cA = capacityA
        cB = capacityB
        
        refill = 0
        while l <= r:
            if l == r:
                if cA < plants[l] and cB < plants[l]:
                    refill += 1
                l += 1
                break
            
            if cA < plants[l]:
                refill += 1
                cA = capacityA
            
            if cB < plants[r]:
                refill += 1
                cB = capacityB
            
            cA -= plants[l]
            cB -= plants[r]
            
            l += 1
            r -= 1
        
        return refill