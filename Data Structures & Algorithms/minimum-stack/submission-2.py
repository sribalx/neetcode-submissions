class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []

    def push(self, val: int) -> None:
        if self.minstack and val > self.minstack[-1]:
            self.stack.append(val)
        else:
            self.stack.append(val)
            self.minstack.append(val)
        
    def pop(self) -> None:
        if self.stack:
            print(self.stack, self.minstack)
            if self.stack[-1] == self.minstack[-1]:
                self.minstack = self.minstack[0:(len(self.minstack) - 1)]
            self.stack = self.stack[0:(len(self.stack) - 1)]
            
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        if self.minstack:
            return self.minstack[-1]
        else:
            return 0
        
