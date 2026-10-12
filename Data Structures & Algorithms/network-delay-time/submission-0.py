class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, source: int) -> int:
        INF = 10 ** 6
        
        edges = defaultdict(lambda: set())
        for ui, vi, ti in times:
            edges[ui].add((vi, ti))
        
        dist = defaultdict(lambda: INF)
        dist[source] = 0
        Q = [(dist[ui], ui) for ui in range(1, n+1)]
        heapq.heapify(Q)
        while Q:
            ti, ui = heapq.heappop(Q)
            if ti > dist[ui]:
                continue # outdated entry
            for vi, ti in edges[ui]:
                if (alt := dist[ui] + ti) < dist[vi]:
                    dist[vi] = alt
                    heapq.heappush(Q, (alt, vi))

        max_dist = 0
        for ui in range(1, n+1):
            max_dist = max(max_dist, dist[ui])
        
        return max_dist if max_dist != INF else -1

