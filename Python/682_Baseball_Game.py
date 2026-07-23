from typing import List

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for op in operations:
            if op == '+' and len(stack) >= 2:
                stack.append(stack[-1] + stack[-2])
            elif op == 'D' and len(stack) >= 1:
                stack.append(stack[-1] * 2)
            elif op == 'C' and len(stack) >= 1:
                stack.pop()
            else:
                stack.append(int(op))
        sum = 0
        while len(stack) > 0:
            sum += stack.pop()
        return sum