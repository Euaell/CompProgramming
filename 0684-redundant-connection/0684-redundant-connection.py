class Solution:
    def find(self, x, parent):
        if parent[x] != x:
            parent[x] = self.find(parent[x], parent)
            
        return parent[x]
    
    def union(self, x, y, parent, rank):
        if rank[x] >= rank[y]:
            parent[y] = x
            rank[x] += rank[y]
        else:
            parent[x] = y
            rank[x] += rank[y]
    
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        
        parent = [i for i in range(n + 1)]
        rank = [1 for _ in range(n + 1)]
        
        ans = []
        
        for e1, e2 in edges:
            p1 = self.find(e1, parent)
            p2 = self.find(e2, parent)
            if p1 == p2 and p1 != -1:
                ans = [e1, e2]
                
            self.union(p1, p2, parent, rank)
        
        return ans
            