class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parentheses_open = {
            "(": ")",
            "{": "}",
            "[": "]"
        }

        parentheses_close = {
            ")": "(",
            "}": "{",
            "]": "["
        }

        for c in s:
            if parentheses_open.get(c) != None:
                stack.append(c)
                continue
            if parentheses_close.get(c) != None:
                if len(stack) > 0 and stack[-1] == parentheses_close.get(c):
                    stack.pop()
                else:
                    return False
        return True if len(stack) == 0 else False