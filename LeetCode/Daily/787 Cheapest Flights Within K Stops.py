class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        flight_map = defaultdict(list)
        for u, v, cost in flights:
            flight_map[u].append((v, cost))
        min_costs = [math.inf]*n
        min_costs[src] = 0
        # print(flight_map)
        heap = [(0, src, 0)] # (Cost, Node, Stops)
        while heap:
            stops, node, cost  = heappop(heap)
            for v, path_cost in flight_map[node]:
                if stops<=k and cost+path_cost < min_costs[v]:
                    min_costs[v] = cost+path_cost
                    heappush(heap, (stops+1, v, cost+path_cost))
        return -1 if math.isinf(min_costs[dst]) else min_costs[dst]