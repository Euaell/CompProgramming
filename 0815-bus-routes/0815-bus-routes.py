class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        result = -1
        if len(routes) == 0:
            return result

        if source == target:
            return 0

        #key is the stop number, value is the transferrable bus
        stop_to_routes = {}
        #key is the bus number, value is the transferrable bus
        transportations = {}
        source_routes = set()
        target_routes = set()

        for i in range(len(routes)):
            for j in range(len(routes[i])):
                if not routes[i][j] in stop_to_routes:
                    stop_to_routes[routes[i][j]] = set()

                stop_to_routes[routes[i][j]].add(i)

                if source == routes[i][j]:
                    source_routes.add(i)

                if target == routes[i][j]:
                    target_routes.add(i)

        for i in range(len(routes)):
            for j in range(len(routes[i])):
                if not i in transportations:
                    transportations[i] = set()

                for route in stop_to_routes[routes[i][j]]:
                    if route != i and not route in transportations[i]:
                        transportations[i].add(route)

        queue = []
        visited = [False] * len(routes)

        for source_route in source_routes:
            visited = [False] * len(routes)
            queue.clear()
            queue.append((source_route, 1))
            visited[source_route] = True

            while len(queue) > 0:
                cur = queue.pop(0)
                if cur[0] in target_routes:
                    result = cur[1] if result == -1 else min(cur[1], result)
                    break

                for to_route in transportations[cur[0]]:
                    if not visited[to_route]:
                        queue.append((to_route, cur[1] + 1))
                        visited[to_route] = True

        return result