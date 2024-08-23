import heapq
from collections import defaultdict

class FreqStack:
    def __init__(self):
        self.freq = defaultdict(int) 
        self.group = defaultdict(list)  
        self.max_freq = 0  

    def push(self, val: int) -> None:
        self.freq[val] += 1
        f = self.freq[val]
        if f > self.max_freq:
            self.max_freq = f
        self.group[f].append(val)
    
    def pop(self) -> int:
        val = self.group[self.max_freq].pop()
        self.freq[val] -= 1
        
        if not self.group[self.max_freq]:
            self.max_freq -= 1
        
        return val

