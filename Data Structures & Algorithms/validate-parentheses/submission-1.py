class Solution:
    def isValid(self, s: str) -> bool:
        OPEN = '([{'
        CLOSE = ')]}'

        stack = []
        for par in s:
            if par in OPEN:
                stack.append(OPEN.index(par))
            else:
                if not stack:
                    return False
                if stack.pop() != CLOSE.index(par):
                    return False
        return not stack