from typing import List

class Solution:
    # This solutoion is valid and works fine with O(n^2) time and O(n) extra space complexity
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(9):
            rows = set()
            for col in range(9):
                if board[row][col] == '.':
                    continue
                elif board[row][col] not in rows:
                    rows.add(board[row][col])
                else:
                    return False
        for col in range(9):
            cols = set()
            for row in range(9):
                if board[row][col] == '.':
                    continue
                elif board[row][col] not in cols:
                    cols.add(board[row][col])
                else:
                    return False
        for square in range(9):
            squares = set()
            for i in range(3):
                for j in range(3):
                    row = (square//3) * 3 + i
                    col = (square % 3) * 3 + j
                    if board[row][col] == ".":
                        continue
                    if board[row][col] not in squares:
                        squares.add(board[row][col])
                    else:
                        return False
        return True