from typing import List

class Solution:
     def nextGreaterElements(self, A: List[int]) -> List[int]:
        stack = []
        ret = [-1] * len(A)
        for i in range(len(A) * 2):
            i %= len(A)
            while stack and A[stack[-1]] < A[i]:
                ret[stack.pop()] = A[i]
            stack.append(i)

        return ret