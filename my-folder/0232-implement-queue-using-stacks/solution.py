class MyQueue:

    def __init__(self):
        self.queue1 = []
        self.queue2 = []
        self.pointer = 0
        
    def push(self, x: int) -> None:
        self.queue1.append(x)
        self.queue2.append(x)
        
    def pop(self) -> int:
        val = self.queue2[self.pointer]
        self.pointer+=1
        return val

    def peek(self) -> int:
        return self.queue2[self.pointer]
        
    def empty(self) -> bool:
        return self.pointer >= len(self.queue2)
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
