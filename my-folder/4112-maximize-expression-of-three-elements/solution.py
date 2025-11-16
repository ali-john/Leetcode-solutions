class Solution:
    def maximizeExpressionOfThree(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        ans = nums[n - 1] + nums[n - 2] - nums[0]
        return ans
