class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        degree = [0] * numCourses
        
        graph = defaultdict(list)
        
        for p1, p2 in prerequisites:
            degree[p2] += 1
            graph[p1].append(p2)
        
        arr = [set() for _ in range(numCourses)]
        
        que = deque()
        
        for i, d in enumerate(degree):
            if d == 0:
                que.append(i)
        
        while que:
            tmp = que.popleft()
            
            for r in graph[tmp]:
                arr[r].add(tmp)
                arr[r] = arr[r].union(arr[tmp])
                degree[r] -= 1
                if degree[r] == 0:
                    que.append(r)
        
        n = len(queries)
        
        ans = [False] * n
        
        for i in range(n):
            ans[i] = queries[i][0] in arr[queries[i][1]]
            
        return ans