class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        M, N = len(board), len(board[0])

        def find(row, col, idx=0, seen=set()):
            if idx >= len(word):
                return True
            
            if row < 0 or row >= M or \
               col < 0 or col >= N or \
               (row, col) in seen:
               return False

            new_seen = seen.union([(row, col)])
            
            res = False
            if board[row][col] == word[idx]:
                res = res or \
                      find(row+1, col,   idx+1, new_seen) or \
                      find(row-1, col,   idx+1, new_seen) or \
                      find(row,   col+1, idx+1, new_seen) or \
                      find(row,   col-1, idx+1, new_seen)

            
            return res
        
        for row in range(M):
            for col in range(N):
                if find(row, col):
                    return True
        
        return False