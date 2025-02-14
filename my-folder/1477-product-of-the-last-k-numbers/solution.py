class ProductOfNumbers:

    def __init__(self):
        self.nums = []
        self.prefix = []
    def add(self, num: int) -> None:
        if num==0:
            self.nums = []
        else:
            if len(self.nums)==0:
                self.nums.append(num)
            else:
                self.nums.append(self.nums[-1]*num)

    def getProduct(self, k: int) -> int:
        #print(f'k {k}, nums: {self.nums}')
        n = len(self.nums)
        if len(self.nums)<k: return 0 # it gets flushed
        if len(self.nums)==k: return self.nums[-1]
        else: 
            ans = self.nums[-1]//self.nums[-1-k]
            return ans

        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
