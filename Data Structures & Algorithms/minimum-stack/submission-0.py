class MinStack:
    def __init__(self):
        self._stack = []
        self._min_stack = []

    def push(self, val: int) -> None:
        self._stack.append(val)

        if len(self._min_stack) == 0:
            self._min_stack.append(val)
        else:
            min_val = min(self._min_stack[-1], val)
            self._min_stack.append(min_val)

    def pop(self) -> None:
        self._stack.pop()
        self._min_stack.pop()

    def top(self) -> int:
        return self._stack[-1]

    def getMin(self) -> int:
        # Assuming this function always gets
        # called when there's at leat one element
        # in the stack
        return self._min_stack[-1]
