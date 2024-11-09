class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.map = defaultdict(list)
        for i,num in enumerate(self.nums):
            self.map[num].append(i)

    def pick(self, target: int) -> int:
        ll = self.map[target]
        index = random.randint(0,len(ll)-1)
        return ll[index]
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
