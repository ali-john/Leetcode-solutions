class Solution:
    def concatWithReverse(self, nums: list[int]) -> list[int]:
        for i in range(len(nums)-1, -1, -1):
            nums.append(nums[i])
        return nums

