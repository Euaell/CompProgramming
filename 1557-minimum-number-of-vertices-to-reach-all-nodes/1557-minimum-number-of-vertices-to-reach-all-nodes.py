class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        
        x = [0 for i in range(n)]
        
        for i in range(len(edges)):
            x[edges[i][1]] -= 1
        
        ret = []
        
        for i in range(n):
            if x[i] == 0:
                ret.append(i)
        
        return ret