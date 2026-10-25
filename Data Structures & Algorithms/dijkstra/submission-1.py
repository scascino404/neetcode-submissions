class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        INF = 100_000

        adj = defaultdict(lambda: [])
        for u, v, w in edges:
            adj[u].append((v, w))

        dist = defaultdict(lambda: INF)
        dist[src] = 0

        Q = [(src, dist[src])]
        while Q:
            u, d = heapq.heappop(Q)
            if d > dist[u]:
                continue # outdated
            
            for v, w in adj[u]:
                if (dv := d + w) < dist[v]:
                    dist[v] = dv
                    heapq.heappush(Q, (v, dv))

        for u in range(n):
            if u not in dist:
                dist[u] = -1
        
        return dict(dist)