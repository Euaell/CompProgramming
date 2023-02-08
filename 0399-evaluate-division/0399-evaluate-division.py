class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # build adjecency list
        adj_list = {}
        for (e, i) in zip(equations, values):
            if e[0] not in adj_list:
                adj_list[e[0]] = []
            adj_list[e[0]].append((e[1], i))

            if e[1] not in adj_list:
                adj_list[e[1]] = []
            adj_list[e[1]].append((e[0], 1 / i))

        n = len(queries)
        ret = [-1] * n

        for i in range(n):
            if queries[i][0] not in adj_list:
                continue
            visited = set()
            que = deque()
            que.append((queries[i][0], 1))

            while que:
                k, v = que.popleft()
                if k == queries[i][1]:
                    ret[i] = v
                    break
                if k in visited:
                    continue
                visited.add(k)
                for b1, b2 in adj_list[k]:
                    que.append((b1, b2 * v))

        return ret