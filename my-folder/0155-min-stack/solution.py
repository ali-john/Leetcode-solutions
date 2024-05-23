class MinStack:
    # Two stack approach. Maintain a min stack to keep track of min value       #encountered so for
    def __init__(self):
        self.stack = deque()
        self.min_stack = deque()
        
    def push(self, val: int) -> None:
        if len(self.stack) == 0 or self.min_stack[-1] >= val:
            self.min_stack.append(val)
            self.stack.append(val)
        else:
            self.stack.append(val)
        
    def pop(self) -> None:
        if self.min_stack[-1] == self.stack[-1]:
            self.min_stack.pop()
            self.stack.pop()
        else:
            self.stack.pop()
        
    def top(self) -> int:
        t = self.stack[-1]
        return t
        
    def getMin(self) -> int:
        m = self.min_stack[-1]
        return m

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
