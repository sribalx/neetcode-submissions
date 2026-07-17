class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = set()
        operators.add('+')
        operators.add('-')
        operators.add('*')
        operators.add('/')
        
        for token in tokens:
            if token not in operators:
                stack.append(int(token))
            else:
                if token == '+':
                    a = stack[-1]
                    stack.pop()
                    b = stack[-1]
                    stack.pop()
                    c = a + b
                    stack.append(c)
                
                elif token == '-':
                    a = stack[-1]
                    stack.pop()
                    b = stack[-1]
                    stack.pop()
                    c = b - a
                    stack.append(c)
                
                elif token == '*':
                    a = stack[-1]
                    stack.pop()
                    b = stack[-1]
                    stack.pop()
                    c = a * b
                    stack.append(c)
                
                elif token == '/':
                    a = stack[-1]
                    stack.pop()
                    b = stack[-1]
                    stack.pop()
                    c = int(b / a)
                    stack.append(c)
                
            print(stack)
        
        return stack[0]