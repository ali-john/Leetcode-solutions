class Solution:
    def minAbsoluteDifference(self, nums: list[int]) -> int:
        n = len(nums)
        ans = float('inf')
        for i in range(n):
            if nums[i] == 1:
                for j in range(n):
                    if nums[j] == 2:
                        ans = min(ans, abs(j - i))
        return ans if ans!=float('inf') else -1

