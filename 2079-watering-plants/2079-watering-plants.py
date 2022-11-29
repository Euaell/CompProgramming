class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        n = len(plants)
        
        jug = capacity
        steps = 0
        
        for i in range(n):
            if jug < plants[i]:
                jug = capacity
                steps += (2 * i) + 1
            else:
                steps += 1
            
            jug -= plants[i]            
            
        return steps