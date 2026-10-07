class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0
    
    def push(self, val: int) -> None:
        self.stack.append(val)
    
    def pop(self) -> None:
        self.stack.pop()
    
    def top(self) -> int:
        return self.stack[-1]

class MinStack:
    def __init__(self):
        self.stack = Stack()
        self.min_stack = Stack()

    def push(self, val: int) -> None:
        self.stack.push(val)

        if self.min_stack.is_empty():
            self.min_stack.push(val)
        else:
            self.min_stack.push(min(self.min_stack.top(), val))

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()        

    def top(self) -> int:
        return self.stack.top()

    def getMin(self) -> int:
        return self.min_stack.top()