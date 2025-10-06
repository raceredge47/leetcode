class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        p = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        for index, i in enumerate(s, 1):
            if index == 1 and i in p.keys():
                return False
            closer = p.get(i)
            if closer and len(stack) >=1 and closer == stack[-1]:
                stack.pop(-1)
            else:
                stack.append(i)

        if stack:
            return False
        else:
            return True