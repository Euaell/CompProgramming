class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        n = len(edges)
        
        node1Vis = {}
        node2Vis = {}
        
        tmp1 = node1
        t1 = 0
        tmp2 = node2
        t2 = 0
        
        while tmp1 not in node1Vis:
            node1Vis[tmp1] = t1
            tmp1 = edges[tmp1]
            t1 += 1
            if tmp1 == -1: break
                
        while tmp2 not in node2Vis:
            node2Vis[tmp2] = t2
            tmp2 = edges[tmp2]
            t2 += 1
            if tmp2 == -1: break
               
        ans, dis = -1, inf
        for i in node1Vis.keys():
            if i in node2Vis:
                m = max(node1Vis[i], node2Vis[i])
                if dis > m:
                    ans = i
                    dis = m
                elif dis == m and ans > i:
                    ans = i
        
        return ans