class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        suffix = [0]*n
        suffix[-1] = nums[-1]

        for i in range(n-2, -1, -1):
            suffix[i] = min(suffix[i+1], nums[i])
        max_ = float('-inf')
        for i in range(n):
            max_ = max(max_, nums[i])
            if ( max_ - suffix[i] ) <= k:
                return i
        return -1
