class Solution:
    def getSlope(self, p1: List[int], p2: List[int]) -> float:
        # return (rise / run)
        if (p2[0] - p1[0]) == 0:
            return inf
        return (p2[1] - p1[1]) / (p2[0] - p1[0])
    
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n <= 2:
            return n
        
        answer = 0
        for i in range(n):
            # key: slope value: count
            dict = {}
            for j in range(n):
                if j == i:
                    continue
                m = self.getSlope(points[i], points[j])
                if m not in dict:
                    dict[m] = 0
                dict[m] += 1
            
            for val in dict.values():
                answer = max(val + 1, answer)
                
        return answer