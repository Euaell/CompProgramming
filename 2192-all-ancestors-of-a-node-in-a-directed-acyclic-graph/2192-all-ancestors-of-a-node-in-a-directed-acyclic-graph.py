class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        adjList = defaultdict(list)
        
        for e1, e2 in edges:
            adjList[e1].append(e2)
        
        ans = [[] for _ in range(n)] 
        
        def dfs(curr, par):
            if curr != par: 
                l = len(ans[curr])
                if l == 0 or ans[curr][l - 1] != par: 
                    ans[curr].append(par)
                else: return
            
            for r in adjList[curr]:
                dfs(r, par)
        
        for i in range(n):
            dfs(i, i)
            
        return ans