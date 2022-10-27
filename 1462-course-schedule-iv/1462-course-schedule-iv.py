class Solution:
    def checkIfPrerequisite(self, n: int, pre: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        adjMatrix = [[False] * n for _ in range(n)]
        
        for p, c in pre:
            adjMatrix[p][c] = True
        
        for intermidate in range(n):
            for p in range(n):
                for c in range(n):
                    adjMatrix[p][c] |= (adjMatrix[p][intermidate] and adjMatrix[intermidate][c])
        
        answer = []
        for p, c in queries:
            answer.append(adjMatrix[p][c])
        
        return answer
    