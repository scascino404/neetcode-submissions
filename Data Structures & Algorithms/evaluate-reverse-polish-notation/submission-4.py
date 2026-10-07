class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def eval(a, b, op):
            if op == '+':
                return a + b
            elif op == '-':
                return a - b
            elif op == '*':
                return a * b
            else: # op == '/'
                return int(a / b)
        
        ops = '+-*/'
        stack = []
        for t in tokens:
            if t in ops:
                b = stack.pop()
                a = stack.pop()
                stack.append(eval(a, b, t))
            else:
                stack.append(int(t))
        
        return stack.pop()
