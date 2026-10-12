class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])

        parent = [[(i, j) for j in range(N)] for i in range(M)]
        size = [[1]*N for _ in range(M)]

        def find(p):
            i, j = p
            if parent[i][j] != p:
                parent[i][j] = find(parent[i][j])
            return parent[i][j]

        def union(p, q):
            pi, pj = find(p)
            qi, qj = find(q)

            if pi == qi and pj == qj:
                return

            if size[pi][pj] < size[qi][qj]:
                pi, qi = qi, pi
                pj, qj = qj, pj

            parent[qi][qj] = (pi, pj)
            size[pi][pj] += size[qi][qj]


        # Check the servers connected by row.
        for i in range(M):
            prev = None
            for j in range(N):
                if grid[i][j] == 0:
                    continue
                if not prev:
                    prev = (i, j)
                else:
                    union((i, j), prev)
        
        # Check the servers connected by column.
        for j in range(N):
            prev = None
            for i in range(M):
                if grid[i][j] == 0:
                    continue
                if not prev:
                    prev = (i, j)
                else:
                    union((i, j), prev)

        num_connected = 0
        for i in range(M):
            for j in range(N):
                pi, pj = find((i, j))
                num_connected += size[pi][pj] > 1
        
        return num_connected
            