class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        children = defaultdict(list)
        
        for i in range(len(parent)):
            children[parent[i]].append(i)
        
        glob = [0]
        
        def rec(node) -> int:
            # if leaf
            if len(children[node]) == 0:
                return 1
            
            ans = [0, 0]
            # visit children
            for c in children[node]:    
                if s[c] != s[node]:
                    heapq.heappush(ans, -rec(c))
                else: 
                    rec(c)
            
            firstMax = -heapq.heappop(ans) + 1
            secondMax = -heapq.heappop(ans)
            
            glob[0] = max(glob[0], firstMax, firstMax + secondMax)
            
            return firstMax
        
        
        glob[0] = max(rec(children[-1][0]), glob[0])
            
        return glob[0]