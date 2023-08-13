class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        INF = math.inf
        MOD = 10**9+7
        road_map = defaultdict(list)
        for u, v, time in roads:
            road_map[u].append((v, time))
            road_map[v].append((u, time))

        ways = [0]*n
        dist = [INF]*n
        ways[0], dist[0] = 1, 0
        heap = [(0, 0)]
        while heap:
            # print(heap)
            d, u = heappop(heap)
            for v, time in road_map[u]:
                if d + time <= dist[v]:
                    if d + time == dist[v]:
                        ways[v] = (ways[v]+ways[u])%MOD
                    else:
                        ways[v] = ways[u]
                        dist[v] = d + time
                        heappush(heap, (d+time, v))
        return ways[n-1]
            