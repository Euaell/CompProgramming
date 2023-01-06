class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        n = len(costs)
        costs.sort()
        
        i = 0
        while coins > 0 and i < n:
            if costs[i] <= coins:
                coins -= costs[i]
                i+=1
            else:
                break
            
        return i