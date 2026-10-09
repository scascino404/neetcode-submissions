class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check rows
        for row in range(9):
            seen = [False] * 10
            for column in range(9):
                value = board[row][column]
                if value == '.':
                    continue
                value = int(value)
                if seen[value]:
                    return False
                seen[value] = True

        # Check columns
        for column in range(9):
            seen = [False] * 10
            for row in range(9):
                value = board[row][column]
                if value == '.':
                    continue
                value = int(value)
                if seen[value]:
                    return False
                seen[value] = True

        # Check squares
        for square in range(9):
            seen = [False] * 10
            for row_offset in range(3):
                for column_offset in range(3):
                    row = (square // 3) * 3 + row_offset
                    column = (square % 3) * 3 + column_offset
                    value = board[row][column]
                    if value == '.':
                        continue
                    value = int(value)
                    if seen[value]:
                        return False
                    seen[value] = True

        return True