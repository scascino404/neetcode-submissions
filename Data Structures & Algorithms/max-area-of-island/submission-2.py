class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        max_area = 0
        visited = [[False] * N for _ in range(M)]
        for i in range(M):
            for j in range(N):
                if not grid[i][j] or visited[i][j]:
                    continue
                area = 0
                stack = [(i, j)]
                while stack:
                    row, col = stack.pop()
                    if not grid[row][col] or visited[row][col]:
                        continue
                    area += 1
                    if row > 0:
                        stack.append((row - 1, col))
                    if row < M-1:
                        stack.append((row + 1, col))
                    if col > 0:
                        stack.append((row, col - 1))
                    if col < N-1:
                        stack.append((row, col + 1))
                    visited[row][col] = True
                max_area = max(max_area, area)
        return max_area
