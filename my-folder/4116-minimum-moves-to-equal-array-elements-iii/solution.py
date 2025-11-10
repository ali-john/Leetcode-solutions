class Solution:
    def minMoves(self, nums: List[int]) -> int:
        m = max(nums)

        ans = 0
        for num in nums:
            ans+= m - num
        return ans
