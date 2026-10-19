class Solution:
    def rotate(self, m: List[List[int]]) -> None:
        N = len(m)

        # Invert rows order
        for i in range(N // 2):
            j = N - (i + 1)
            for k in range(N):
                m[i][k], m[j][k] = m[j][k], m[i][k]

        # Transpose
        for i in range(N):
            for j in range(i+1, N):
                m[i][j], m[j][i] = m[j][i], m[i][j]
