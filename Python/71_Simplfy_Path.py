class Solution:
    def simplifyPath(self, path: str) -> str:
        dirs = path.split('/')
        stack = []

        for cur in dirs:
            if cur == '..':
                if stack:
                    stack.pop()
            elif cur != "" and cur != ".":
                stack.append(cur)
        return '/' + '/'.join(stack)
            