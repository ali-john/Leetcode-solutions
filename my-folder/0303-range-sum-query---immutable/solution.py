class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.prefix = []
        prev = 0
        for i in range(len(nums)):
            prev+=nums[i]
            self.prefix.append(prev)

    def sumRange(self, left: int, right: int) -> int:
        if left-1>=0:
            left_sum = self.prefix[left-1]
        else:
            left_sum = 0
        
        right_sum = self.prefix[right]
        return (right_sum-left_sum)

        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
