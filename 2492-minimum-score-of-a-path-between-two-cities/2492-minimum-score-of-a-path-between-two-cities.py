class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        
        Min = inf
        visited = set()
        que = deque()
        
        adjList = defaultdict(list)
        for s, e, d in roads:
            adjList[s].append((e, d))
            adjList[e].append((s, d))
        
        que.append(1)
        while que:
            tmp = que.pop()
            if tmp in visited:
                continue
            visited.add(tmp)
            
            for dest, dis in adjList[tmp]:
                Min = min(Min, dis)
                if dest in visited:
                    continue
                que.append(dest)
       
        return Min
    