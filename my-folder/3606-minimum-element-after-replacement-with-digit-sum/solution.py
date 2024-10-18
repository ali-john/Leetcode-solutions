class Solution:
    def minElement(self, nums: List[int]) -> int:
        min_val = float("inf")

        for i in range(len(nums)):
            num = str(nums[i])
            total = 0
            for char in num:
                total+=int(char)
            min_val = min(min_val,total)
        return min_val
