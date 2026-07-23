from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        r = 0
        r1, r2 = 0, m - 1
        while r1 <= r2:
            r = (r2 + r1) // 2
            if target < matrix[r][0]:
                r2 = r - 1
            elif target > matrix[r][-1]:
                r1 = r + 1
            else:
                break
        if r1 > r2:
            return False

        c1,c2 = 0, n - 1
        while c1 <= c2:
            c = (c1 + c2) // 2
            if matrix[r][c] < target:
                c1 = c + 1
            elif matrix[r][c] > target:
                c2 = c - 1
            else:
                return True

        return False