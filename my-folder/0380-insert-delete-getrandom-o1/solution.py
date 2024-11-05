class RandomizedSet:

    def __init__(self):
        self.arr = []
        self.map = {}
        
    def insert(self, val: int) -> bool:
        if val in self.map:
            return False
        
        self.arr.append(val)
        self.map[val] = len(self.arr)-1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.map:
            return False
        else:
            index = self.map[val]
            temp = self.arr[-1]
            self.arr[-1] = self.arr[index]
            self.arr[index] = temp
            self.arr.pop()
            self.map[temp] = index
            del self.map[val]
            return True
            
        
    def getRandom(self) -> int:
        n = len(self.arr)
        index = random.randint(0,n-1)
        return self.arr[index]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
