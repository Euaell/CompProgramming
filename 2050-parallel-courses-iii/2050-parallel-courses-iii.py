class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        adjList = defaultdict(list)
        ti = time.copy()
        degree = [0] * n
        
        for e1, e2 in relations:
            degree[e2 - 1] += 1
            adjList[e1 - 1].append(e2 - 1)
        
        que = deque()
        for i, d in enumerate(degree):
            if d == 0:
                que.append(i)
        
        ans = 0
        
        while que:
            tmp = que.popleft()
            for r in adjList[tmp]:
                ti[r] = max(ti[r], time[r] + ti[tmp])
                degree[r] -= 1
                if degree[r] == 0:
                    que.append(r)
        
        
        return max(ti)