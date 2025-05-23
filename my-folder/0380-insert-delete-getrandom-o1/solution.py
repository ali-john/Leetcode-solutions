class RandomizedSet:

    def __init__(self):
        self.arr = []
        self.map = defaultdict()

    def insert(self, val: int) -> bool:
        if val in self.map:
            return False

        self.arr.append(val)
        self.map[val] = len(self.arr) - 1
        return True


    def remove(self, val: int) -> bool:
        if not val in self.map:
            return False
        
        else:
            last_element = self.arr[-1]
            index = self.map[val]
            self.arr[-1] = self.arr[index]
            self.arr[index] = last_element
            self.arr.pop()
            self.map[last_element] = index
            del self.map[val]
            return True
        

    def getRandom(self) -> int:
        n = random.randint(0,len(self.arr)-1)
        return self.arr[n]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
