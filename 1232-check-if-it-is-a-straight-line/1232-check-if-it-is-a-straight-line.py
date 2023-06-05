class Solution:
    def calcSlope(self, p1: List[int], p2: List[int]):
        if p2[1] == p1[1]: 
            return inf
        return (p2[0] - p1[0])/(p2[1] - p1[1])
    
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        n = len(coordinates)
        m = self.calcSlope(coordinates[0], coordinates[1])
        
        for i in range(2, n):
            if self.calcSlope(coordinates[0], coordinates[i]) != m:
                return False
        
        return True
