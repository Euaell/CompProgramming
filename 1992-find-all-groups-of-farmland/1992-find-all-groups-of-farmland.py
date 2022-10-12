class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        n = len(land)
        m = len(land[0])
        
        direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        vis = set()
        
        def isValid(i, j):
            return 0 <= i < n and 0 <= j < m and land[i][j] == 1 and (i, j) not in vis
        
        
        def bfs(i, j):
            
            que = deque()
            
            que.append((i, j))
            
            last = (i, j)
            while que:
                tmp = que.popleft()
                if tmp in vis: continue
                
                vis.add(tmp)
                last = tmp
                
                row, col = tmp
                
                for r, c in direction:
                    if isValid(row + r, col + c):
                        que.append((row + r, col + c))       
                
            return last
        
        ans = []
        for i in range(n):
            for j in range(m):
                if isValid(i, j):
                    er, ec = bfs(i, j)
                    ans.append([i, j, er, ec])
        return ans
            