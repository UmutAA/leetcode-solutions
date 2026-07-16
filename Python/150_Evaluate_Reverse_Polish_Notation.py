from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = list()
        for token in tokens:  
            if self.is_number(token):
                stack.append(int(token))
            else:
                op = token
                match op:
                    case "+":
                        num1 = stack.pop()
                        num2 = stack.pop()
                        stack.append(num1 + num2)
                    case "-":
                        num1 = stack.pop()
                        num2 = stack.pop()
                        stack.append(num2 - num1)
                    case "*":
                        num1 = stack.pop()
                        num2 = stack.pop()
                        stack.append(num1 * num2)
                    case "/":
                        num1 = stack.pop()
                        num2 = stack.pop()
                        stack.append(int(num2 / num1))
        return stack[0]

    def is_number(self, string):
        try:
            int(string)
            return True
        except ValueError:
            return False