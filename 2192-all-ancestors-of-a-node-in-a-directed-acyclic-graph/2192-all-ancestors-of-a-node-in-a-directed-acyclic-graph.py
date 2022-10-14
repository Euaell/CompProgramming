class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        adjList = defaultdict(list)
        
        degree = [0] * n
        for e1, e2 in edges:
            degree[e2] += 1
            adjList[e1].append(e2)
        
        ans = [set() for _ in range(n)] 
        
        que = deque()
        
        
        for i, d in enumerate(degree):
            if d == 0: 
                que.append(i)
        
        while que:
            tmp = que.popleft()
            
            for r in adjList[tmp]:
                ans[r].add(tmp)
                ans[r] = ans[r].union(ans[tmp])
                degree[r] -= 1
                if degree[r] == 0:
                    que.append(r)
        
        for i in range(n):
            ans[i] = sorted(ans[i])
            
        return ans