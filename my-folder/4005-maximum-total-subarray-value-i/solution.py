class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        nums.sort()
        mini = nums[0]
        maxi = nums[-1]

        ans = (maxi - mini) * k
        return ans
