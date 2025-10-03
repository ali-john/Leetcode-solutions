class Solution:
    def minOperationsToMakeMedianK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        median = nums[n//2]

        ans = abs(median - k)
        # reduce number on left
        for i in range(n//2):
            if nums[i] > k:
                ans+=abs(nums[i] - k)
        # increase numbers on right.
        for i in range(n//2+1,n):
            if nums[i] < k:
                ans+=abs(nums[i] - k)
        return ans

