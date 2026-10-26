class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        EMPTY, FRESH, ROTTEN = 0, 1, 2
    
        Q = deque()
        for i in range(M):
            for j in range(N):
                if grid[i][j] == ROTTEN:
                    Q.append((i, j, 0))
        
        minute = 0
        visited = [[False] * N for _ in range(M)]

        while Q:
            i, j, m = Q.popleft()

            if i < 0 or i >= M or \
               j < 0 or j >= N:
               continue
            
            if grid[i][j] == EMPTY or \
               visited[i][j]:
                continue

            minute = max(minute, m)

            Q.append((i+1, j,   m+1))
            Q.append((i-1, j,   m+1))
            Q.append((i,   j+1, m+1))
            Q.append((i,   j-1, m+1))

            visited[i][j] = True

        for i in range(M):
            for j in range(N):
                if (not visited[i][j]) and grid[i][j] == FRESH:
                    return -1

        return minute