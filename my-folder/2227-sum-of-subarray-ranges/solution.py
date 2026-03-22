class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0

        for left in range(n):
            minVal = nums[left]
            maxVal = nums[left]
            for right in range(left+1, n):
                minVal = min(minVal, nums[right])
                maxVal = max(maxVal, nums[right])
                ans += ( maxVal - minVal )
        return ans

