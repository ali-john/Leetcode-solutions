class LUPrefix:

    def __init__(self, n: int):
        self.n = n
        self.track = [False]*(n+2)
        self._longest = 0

    def upload(self, video: int) -> None:
        self.track[video] = True
            
    def longest(self) -> int:
        while self.track[self._longest + 1]:
            self._longest+=1
        return self._longest 
  
        

# Your LUPrefix object will be instantiated and called as such:
# obj = LUPrefix(n)
# obj.upload(video)
# param_2 = obj.longest()
