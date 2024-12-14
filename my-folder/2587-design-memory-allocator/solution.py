class Allocator:

    def __init__(self, n: int):
        self.memory = [float('inf')]*n
        self.table = defaultdict(list)
        

    def allocate(self, size: int, mID: int) -> int:
        n = len(self.memory)
        max_size = 0
        left = 0
        right = 0
        possible = False

        while right<n:
            while right<n and self.memory[right]!=float('inf'):
                right+=1
                left = right

            max_size = max(max_size,(right-left+1))
            if max_size>=size:
                if right<n:
                    possible = True
                    break
            right+=1
        
        if possible:
            for i in range(left,left+size):
                self.memory[i] = mID
                self.table[mID].append(i)
            return left 
        else:
            return -1
        
    def freeMemory(self, mID: int) -> int:
        if mID in self.table:
            l = self.table[mID]
            for i in l:
                self.memory[i] = float('inf')
            size = len(l)
            del self.table[mID]
            return size
        else:
            return 0
            
        


# Your Allocator object will be instantiated and called as such:
# obj = Allocator(n)
# param_1 = obj.allocate(size,mID)
# param_2 = obj.freeMemory(mID)
